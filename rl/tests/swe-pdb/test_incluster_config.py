#!/usr/bin/env python3

import os
import sys
from pathlib import Path
from typing import Optional

from kubernetes import client, config
from kubernetes.client import ApiException

import os
print("HTTP_PROXY:", os.environ.get("HTTP_PROXY"))
print("HTTPS_PROXY:", os.environ.get("HTTPS_PROXY"))
print("NO_PROXY:", os.environ.get("NO_PROXY"))



SERVICE_ACCOUNT_DIR = Path("/var/run/secrets/kubernetes.io/serviceaccount")
TOKEN_PATH = SERVICE_ACCOUNT_DIR / "token"
CA_CERT_PATH = SERVICE_ACCOUNT_DIR / "ca.crt"
NAMESPACE_PATH = SERVICE_ACCOUNT_DIR / "namespace"


def read_text_if_exists(path: Path) -> Optional[str]:
    try:
        if path.exists():
            return path.read_text().strip()
    except Exception:
        return None
    return None


def print_env_probe() -> None:
    print("[Probe] KUBERNETES_SERVICE_HOST:", os.environ.get("KUBERNETES_SERVICE_HOST"))
    print("[Probe] KUBERNETES_SERVICE_PORT:", os.environ.get("KUBERNETES_SERVICE_PORT"))
    print("[Probe] ServiceAccount token exists:", TOKEN_PATH.exists())
    print("[Probe] ServiceAccount ca.crt exists:", CA_CERT_PATH.exists())
    current_ns = read_text_if_exists(NAMESPACE_PATH)
    print("[Probe] Current namespace:", current_ns)


def load_config_preferring_incluster() -> str:
    try:
        config.load_incluster_config()
        _maybe_override_host_from_env()
        return "incluster"
    except Exception as incluster_error:
        print("[Info] load_incluster_config failed:", repr(incluster_error))
        print("[Info] Falling back to load_kube_config() ...")
        config.load_kube_config()
        _maybe_override_host_from_env()
        return "kubeconfig"


def test_core_v1_api(namespace: Optional[str] = None) -> None:
    v1 = client.CoreV1Api()
    try:
        namespaces = v1.list_namespace(_request_timeout=10)
        names = [item.metadata.name for item in namespaces.items]
        print(f"[OK] Fetched {len(names)} namespaces:", ", ".join(names[:10]))
    except ApiException as api_error:
        print("[Error] Failed to list namespaces:", api_error)
        raise

    if namespace:
        try:
            pods = v1.list_namespaced_pod(namespace=namespace, limit=5, _request_timeout=10)
            pod_names = [p.metadata.name for p in pods.items]
            print(f"[OK] {namespace}: first {len(pod_names)} pods:", ", ".join(pod_names))
        except ApiException as api_error:
            print(f"[Warn] Failed to list pods in namespace '{namespace}':", api_error)


def _maybe_override_host_from_env() -> None:
    host = os.environ.get("KUBE_TEST_HOST")
    port = os.environ.get("KUBE_TEST_PORT")
    scheme = os.environ.get("KUBE_TEST_SCHEME", "http")
    if not host or not port:
        return
    cfg = client.Configuration.get_default_copy()
    cfg.host = f"{scheme}://{host}:{port}"
    # 当通过 kubectl proxy 使用 HTTP 时，禁用 TLS 校验
    if scheme == "http":
        cfg.verify_ssl = False
        cfg.ssl_ca_cert = None
    client.Configuration.set_default(cfg)


def main() -> int:
    print("=== Kubernetes In-Cluster Config Tester ===")
    print_env_probe()

    prefer = os.environ.get("KUBE_TEST_NAMESPACE") or read_text_if_exists(NAMESPACE_PATH)
    try:
        mode = load_config_preferring_incluster()
        print(f"[Info] Config loaded via: {mode}")
        test_core_v1_api(namespace=prefer)
        print("[Success] Kubernetes client calls succeeded.")
        return 0
    except Exception as error:
        print("[Failure] Kubernetes client test failed:", repr(error))
        return 2


if __name__ == "__main__":
    sys.exit(main())


