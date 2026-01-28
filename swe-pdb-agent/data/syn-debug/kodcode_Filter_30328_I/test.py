from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from solution import correct_perspective, PerspectiveCorrectionNN, train_nn, predict_transformation_matrix
import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset

def test_correct_perspective():
    src_img = np.random.randint(0, 256, (500, 500, 3), dtype=np.uint8)
    src_points = np.float32([[10, 10], [490, 10], [10, 490], [490, 490]])
    dst_points = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    corrected_img = correct_perspective(src_img, src_points, dst_points)
    assert corrected_img.shape == (500, 500, 3)

def test_perspective_correction_nn():
    nn_model = PerspectiveCorrectionNN()
    assert isinstance(nn_model, PerspectiveCorrectionNN)

def test_predict_transformation_matrix():
    nn_model = PerspectiveCorrectionNN()

    # Assuming the network is already trained
    input_points = np.array([0.1, 0.1, 0.9, 0.1, 0.1, 0.9, 0.9, 0.9], dtype=np.float32)
    predicted_matrix = predict_transformation_matrix(nn_model, input_points)
    assert predicted_matrix.shape == (4, 2)

def test_training_nn():
    nn_model = PerspectiveCorrectionNN()
    
    # Setting up dummy data
    input_vectors = np.random.rand(100, 8).astype(np.float32)
    target_vectors = np.random.rand(100, 4, 2).astype(np.float32)
    
    train_dataset = TensorDataset(torch.tensor(input_vectors), torch.tensor(target_vectors))
    train_loader = DataLoader(train_dataset, batch_size=10, shuffle=True)

    train_nn(nn_model, train_loader, epochs=2)
    
    assert nn_model(torch.tensor(input_vectors[:5])).shape == torch.Size([5, 4, 2])