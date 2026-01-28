import torch
import torch.nn as nn
import torch.optim as optim

class CustomAttention(nn.Module):
    def __init__(self, input_dim, attention_dim, output_dim):
        super(CustomAttention, self).__init__()
        
        self.query = nn.Linear(input_dim, attention_dim)
        self.key = nn.Linear(input_dim, attention_dim)
        self.value = nn.Linear(input_dim, attention_dim)
        self.out = nn.Linear(attention_dim, output_dim)

    def forward(self, x):
        # x : (batch_size, sequence_length, input_dim)
        Q = self.query(x)  # (batch_size, sequence_length, attention_dim)
        K = self.key(x)  # (batch_size, sequence_length, attention_dim)
        V = self.value(x)  # (batch_size, sequence_length, attention_dim)
        
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (K.size(-1) ** 0.5)  # (batch_size, sequence_length, sequence_length)
        attention_weights = torch.nn.functional.softmax(scores, dim=-1)  # (batch_size, sequence_length, sequence_length)
        
        attended_values = torch.matmul(attention_weights, V)  # (batch_size, sequence_length, attention_dim)
        out = self.out(attended_values)  # (batch_size, sequence_length, output_dim)
        
        return out.mean(dim=1)

class SimpleModel(nn.Module):
    def __init__(self, input_dim, attention_dim, output_dim):
        super(SimpleModel, self).__init__()
        self.attention = CustomAttention(input_dim, attention_dim, output_dim)
        self.fc = nn.Linear(output_dim, output_dim)

    def forward(self, x):
        x = self.attention(x)
        x = self.fc(x)
        return x

# Example usage with synthetic dataset:
def main():
    input_dim = 32
    attention_dim = 16
    output_dim = 32
    x_train = torch.randn(100, 10, input_dim)
    y_train = torch.randn(100, output_dim)

    model = SimpleModel(input_dim, attention_dim, output_dim)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(10):
        optimizer.zero_grad()
        output = model(x_train)
        loss = criterion(output, y_train)
        loss.backward()
        optimizer.step()
        print(f'Epoch {epoch + 1}, Loss: {loss.item()}')

if __name__ == "__main__":
    main()