from solution import *
import math

def test_all():
    torch.manual_seed(10)
    P1 = torch.distributions.Normal(loc=0.0, scale=1.0)
    Q1 = torch.distributions.Normal(loc=0.1, scale=1.0)
    assert torch.allclose(torch.distributions.kl_divergence(
    q=Q1, p=P1), kl_div(q=Q1, p=P1), atol=1e-2)

    P2 = torch.distributions.Bernoulli(probs=torch.tensor([0.5]))
    Q2 = torch.distributions.Bernoulli(probs=torch.tensor([0.6]))
    assert torch.allclose(torch.distributions.kl_divergence(
    q=Q2, p=P2), kl_div(q=Q2, p=P2), atol=1e-2)

    P3 = torch.distributions.Geometric(probs=torch.tensor([0.5]))
    Q3 = torch.distributions.Geometric(probs=torch.tensor([0.6]))
    assert torch.allclose(torch.distributions.kl_divergence(
    q=Q3, p=P3), kl_div(q=Q3, p=P3), atol=1e-2)

    # check if the estimator is working
    P4 = torch.distributions.Normal(loc=0.0, scale=1.0)
    Q4 = torch.distributions.Normal(loc=0.0, scale=1.0)
    assert kl_div(q=Q4, p=P4) == 0.0

    P5 = torch.distributions.Normal(loc=0.0, scale=1.0)
    Q5 = torch.distributions.Normal(loc=0.0, scale=2.0)
    assert kl_div(q=Q5, p=P5) > 0.0
    assert kl_div(q=Q5, p=P5, num_samples=10) < kl_div(
    q=Q5, p=P5, num_samples=100000)
    assert kl_div(q=Q5, p=P5, num_samples=10) > kl_div(q=Q5, p=P5, num_samples=11)
    assert kl_div(q=Q5, p=P5, num_samples=100) < kl_div(
    q=Q5, p=P5, num_samples=1000)
    assert kl_div(q=Q5, p=P5, num_samples=100) < kl_div(
    q=Q5, p=P5, num_samples=10000)