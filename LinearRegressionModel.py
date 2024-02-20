import torch
import torch.nn as nn
import torch.optim as optim
# Define a simple linear regression model
class LinearRegression(nn.Module):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(in_features=1, out_features=1)

    def forward(self, x):
        return self.linear(x)

if __name__ == '__main__':

# Sample dataset
    X_train = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
    y_train = torch.tensor([[2.0], [4.0], [6.0], [8.0], [10.0]])

    # Define the model
    model = nn.Linear(in_features=1, out_features=1)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # Training loop
    num_epochs = 1000
    for epoch in range(num_epochs):
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    torch.save(model.state_dict(), 'linear_model.pth')
    # Test the trained model
    X_test = torch.tensor([[6.0]])
    predicted_value = model(X_test)
    print(f'Predicted value for input 6: {predicted_value.item()}')