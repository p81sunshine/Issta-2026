import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from scipy.optimize import minimize

class VAE(nn.Module):
    def __init__(self, latent_dim):
        super(VAE, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim * 2)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 784),
            nn.Sigmoid()
        )

    def encode(self, x):
        z_mean, z_log_var = self.encoder(x).chunk(2, dim=1)
        return z_mean, z_log_var

    def reparameterize(self, z_mean, z_log_var):
        std = torch.exp(0.5 * z_log_var)
        eps = torch.randn_like(std)
        z = z_mean + eps * std
        return z

    def decode(self, z):
        return self.decoder(z)

# Initialize the VAE model
vae = VAE(latent_dim=2)

# Define the objective function for the Bayesian optimization
def objective_function(z):
    z = torch.tensor(z, dtype=torch.float32)
    decoded_output = vae.decode(z)
    quality_metric = torch.sum(decoded_output ** 2).item()
    return quality_metric

# Optimize in the latent space using scipy's minimize function (BFGS method)
initial_guess = np.random.randn(2)
result = minimize(objective_function, initial_guess, method='BFGS')
optimal_latent_vector = result.x

# Decode the optimal latent vector to obtain the optimal input
optimal_input = vae.decode(torch.tensor(optimal_latent_vector, dtype=torch.float32))