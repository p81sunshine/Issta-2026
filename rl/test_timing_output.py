#!/usr/bin/env python3
"""
测试 colorful_print_to_terminal 函数
验证它是否能绕过 stdout 重定向（如 wandb 的捕获）
"""

import sys
import io
from contextlib import redirect_stdout, redirect_stderr

# 直接复制函数实现，避免导入整个包
import click


def colorful_print(string: str, *args, **kwargs) -> None:
    """普通的 colorful_print（会被重定向捕获）"""
    end = kwargs.pop("end", "\n")
    print(click.style(string, *args, **kwargs), end=end, flush=True)


def colorful_print_to_terminal(string: str, *args, **kwargs) -> None:
    """
    直接输出到终端，绕过 stdout/stderr 的重定向（如 wandb 的捕获）。
    这样输出只会显示在终端，不会出现在 wandb 的 output.log 中。
    
    Args:
        string: 要输出的字符串
        *args, **kwargs: 传递给 click.style 的参数
    """
    end = kwargs.pop("end", "\n")
    styled_string = click.style(string, *args, **kwargs)
    
    # 尝试直接写入到终端设备
    try:
        with open("/dev/tty", "w", encoding="utf-8") as tty:
            tty.write(styled_string + end)
            tty.flush()
    except (OSError, IOError):
        # 如果 /dev/tty 不可用（比如在某些环境中），回退到使用原始 stdout
        # sys.__stdout__ 是 Python 保存的原始 stdout，不会被重定向
        if hasattr(sys, "__stdout__") and sys.__stdout__ is not None:
            sys.__stdout__.write(styled_string + end)
            sys.__stdout__.flush()
        else:
            # 最后的回退：使用当前的 stdout（可能会被捕获）
            print(styled_string, end=end, flush=True)


def test_normal_print():
    """测试普通的 colorful_print（会被重定向捕获）"""
    print("\n" + "="*60)
    print("测试 1: 普通的 colorful_print（会被重定向捕获）")
    print("="*60)
    
    # 模拟 wandb 重定向 stdout
    captured_output = io.StringIO()
    
    with redirect_stdout(captured_output):
        colorful_print("这是普通的 colorful_print - 应该被捕获", "red")
        print("这是普通的 print - 也应该被捕获")
    
    captured_text = captured_output.getvalue()
    print(f"捕获到的输出: {repr(captured_text)}")
    print(f"是否被捕获: {len(captured_text) > 0}")
    assert len(captured_text) > 0, "普通输出应该被捕获"
    print("✓ 测试通过：普通输出被正确捕获")


def test_terminal_print():
    """测试 colorful_print_to_terminal（应该绕过重定向）"""
    print("\n" + "="*60)
    print("测试 2: colorful_print_to_terminal（应该绕过重定向）")
    print("="*60)
    
    # 模拟 wandb 重定向 stdout
    captured_output = io.StringIO()
    
    with redirect_stdout(captured_output):
        # 这个应该直接输出到终端，不被捕获
        colorful_print_to_terminal("这是 colorful_print_to_terminal - 应该直接显示在终端", "green")
        print("这是普通的 print - 应该被捕获")
    
    captured_text = captured_output.getvalue()
    print(f"捕获到的输出: {repr(captured_text)}")
    print(f"是否包含 colorful_print_to_terminal 的输出: {'colorful_print_to_terminal' in captured_text}")
    print(f"是否包含普通 print 的输出: {'普通的 print' in captured_text}")
    
    # colorful_print_to_terminal 的输出不应该在捕获的内容中
    # 但普通 print 应该被捕获
    assert "colorful_print_to_terminal" not in captured_text, "colorful_print_to_terminal 的输出不应该被捕获"
    assert "普通的 print" in captured_text, "普通 print 应该被捕获"
    print("✓ 测试通过：colorful_print_to_terminal 成功绕过了重定向")


def test_mixed_output():
    """测试混合使用普通输出和终端输出"""
    print("\n" + "="*60)
    print("测试 3: 混合使用普通输出和终端输出")
    print("="*60)
    
    captured_output = io.StringIO()
    
    with redirect_stdout(captured_output):
        print("普通输出 1 - 会被捕获")
        colorful_print_to_terminal("终端输出 1 - 应该直接显示", "blue")
        print("普通输出 2 - 会被捕获")
        colorful_print_to_terminal("终端输出 2 - 应该直接显示", "yellow")
        print("普通输出 3 - 会被捕获")
    
    captured_text = captured_output.getvalue()
    print(f"\n捕获到的输出:\n{captured_text}")
    
    # 验证：终端输出不应该在捕获中，普通输出应该在
    assert "终端输出" not in captured_text, "终端输出不应该被捕获"
    assert "普通输出" in captured_text, "普通输出应该被捕获"
    print("✓ 测试通过：混合输出正确分离")


def test_simple_time_tracker_simulation():
    """模拟 SimpleTimeTracker 的使用场景"""
    print("\n" + "="*60)
    print("测试 4: 模拟 SimpleTimeTracker 的使用场景")
    print("="*60)
    
    captured_output = io.StringIO()
    
    with redirect_stdout(captured_output):
        # 模拟 LLM 推理时间记录
        colorful_print_to_terminal(
            "[Timing] [2025-11-29 13:54:33] Trajectory 90 - LLM推理: 2.07s "
            "(累计: 2.07s, 总时间: 9.43s, 响应长度: 187, Prompt长度: 586, Action: view)",
            "blue"
        )
        
        # 模拟环境执行时间记录
        colorful_print_to_terminal(
            "[Timing] Trajectory 90 - Step 1 环境执行: 1.77s "
            "(累计: 1.77s, 总时间: 10.28s, Action: view)",
            "yellow"
        )
        
        # 模拟完成信息
        colorful_print_to_terminal(
            "[Timing] Trajectory 90 完成 - 总时间: 10.28s "
            "(环境: 1.77s, LLM: 2.07s, 步数: 1), 原因: ENV_DONE",
            "green"
        )
        
        # 一些普通的日志输出（应该被捕获）
        print("这是普通的日志输出 - 应该被 wandb 捕获")
    
    captured_text = captured_output.getvalue()
    print(f"\n捕获到的输出:\n{captured_text}")
    
    # 验证：Timing 信息不应该在捕获中
    assert "[Timing]" not in captured_text, "Timing 信息不应该被捕获"
    assert "普通的日志输出" in captured_text, "普通日志应该被捕获"
    print("✓ 测试通过：Timing 信息成功绕过重定向")


def main():
    """运行所有测试"""
    print("\n" + "="*60)
    print("开始测试 colorful_print_to_terminal 函数")
    print("="*60)
    
    try:
        test_normal_print()
        test_terminal_print()
        test_mixed_output()
        test_simple_time_tracker_simulation()
        
        print("\n" + "="*60)
        print("所有测试通过！✓")
        print("="*60)
        print("\n📝 测试结果说明：")
        print("  ✓ colorful_print_to_terminal 会直接输出到终端（可以看到彩色输出）")
        print("  ✓ 不会被 stdout 重定向捕获（如 wandb 的 output.log）")
        print("  ✓ 普通 print 和 colorful_print 仍然会被捕获")
        print("\n💡 使用建议：")
        print("  - 在 SimpleTimeTracker 中使用 colorful_print_to_terminal")
        print("  - 这样 timing 信息只会在终端显示，不会污染 wandb 日志")
        print("  - 可以通过 enable_timing_output=False 完全禁用输出")
        
    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

