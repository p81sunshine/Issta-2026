from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import VAE, objective_function
import torch
import numpy as np

def test_vae_initialization():
    vae = VAE(latent_dim=2)
    assert isinstance(vae.encoder, nn.Sequential)
    assert isinstance(vae.decoder, nn.Sequential)

def test_objective_function():
    vae = VAE(latent_dim=2)
    latent_vector = np.random.randn(2)
    quality = objective_function(latent_vector)
    assert isinstance(quality, float)
    assert quality <= 0

def test_optimal_latent_vector():
    vae = VAE(latent_dim=2)
    initial_guess = np.random.randn(2)
    result = minimize(objective_function, initial_guess, method='BFGS')
    assert result.success
    assert isinstance(result.x, np.ndarray)
    assert len(result.x) == 2

def test_decoded_optimal_input():
    vae = VAE(latent_dim=2)
    initial_guess = np.random.randn(2)
    result = minimize(objective_function, initial_guess, method='BFGS')
    optimal_latent_vector = result.x
    optimal_input = vae.decode(torch.tensor(optimal_latent_vector, dtype=torch.float32))
    assert optimal_input.shape == (784,)