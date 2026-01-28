import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

def correct_perspective(src_img, src_points, dst_points):
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    h, w = src_img.shape[:2]
    corrected_img = cv2.warpPerspective(src_img, matrix, (h, w))
    return corrected_img

class PerspectiveCorrectionNN(nn.Module):
    def __init__(self):
        super(PerspectiveCorrectionNN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(8, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 8)
        )

    def forward(self, x):
        return self.fc(x).view(-1, 2, 4)

def train_nn(nn_model, train_loader, epochs=20, lr=0.001):
    criterion = nn.MSELoss()
    optimizer = optim.Adam(nn_model.parameters(), lr=lr)
    nn_model.train()
    for epoch in range(epochs):
        total_loss = 0
        for data in train_loader:
            inputs, targets = data
            optimizer.zero_grad()
            outputs = nn_model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f'Epoch {epoch + 1}, Loss: {total_loss / len(train_loader)}')

def predict_transformation_matrix(nn_model, input_points):
    input_tensor = torch.tensor(input_points, dtype=torch.float32).view(1, -1)
    nn_model.eval()
    with torch.no_grad():
        predicted_points = nn_model(input_tensor).squeeze().numpy()
    return predicted_points.astype(np.float32)