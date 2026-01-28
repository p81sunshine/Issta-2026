import time

from tenacity import (
    retry,
    retry_if_result,
    stop_after_attempt,
    wait_random_exponential,
)

from debug_gym.gym.entities import Observation
from debug_gym.gym.tools.tool import EnvironmentTool
from debug_gym.gym.tools.toolbox import Toolbox


def _is_timeout_or_retryable_error(result) -> bool:
    """Check if eval result indicates a timeout or retryable error.
    
    Returns True if the result should trigger a retry.
    """
    # If result is an Observation, check its content
    if isinstance(result, Observation):
        output = result.observation.lower()
    # If result is an EvalOutput, check its output
    elif hasattr(result, "output"):
        output = result.output.lower()
    else:
        return False
    
    # Check for timeout or transient errors that should be retried
    retryable_indicators = [
        "timeout expired",
        "timeout",
        "connection reset",
        "connection refused",
        "temporary failure",
    ]
    return any(indicator in output for indicator in retryable_indicators)


@Toolbox.register()
class EvalTool(EnvironmentTool):
    name: str = "eval"
    description = "Evaluate the current code against pre-defined test cases."
    arguments = {}

    def use(self, environment) -> Observation:
        """Use the eval tool without retry mechanism."""
        eval_output = environment.eval()
        return Observation(self.name, eval_output.output)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_random_exponential(multiplier=0.5, min=0.5, max=5.0),
        retry=retry_if_result(_is_timeout_or_retryable_error),
        reraise=True,
    )
    def _eval_with_retry(self, environment) -> Observation:
        """Evaluate with retry logic for timeout and transient errors.
        
        This method will retry up to 3 times if the eval output indicates
        a timeout or other retryable error. Only used during env reset.
        """
        eval_output = environment.eval()
        observation = Observation(self.name, eval_output.output)
        # Return the observation; retry_if_result will check if it should retry
        return observation

    def on_env_reset(self, environment, **kwargs):
        super().on_env_reset(environment, **kwargs)
        # Use retry mechanism for eval on reset only
        return self._eval_with_retry(environment)

    def on_rewrite_success(self, environment, **kwargs):
        if environment.auto_eval_on_rewrite:
            # No retry for eval after rewrite
            return self(environment)
        return None
