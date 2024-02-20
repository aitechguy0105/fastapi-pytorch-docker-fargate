from fastapi import FastAPI
import torch
from LinearRegressionModel import LinearRegression
app = FastAPI()
model = LinearRegression()
# Load the saved model state dictionary
state_dict = torch.load('linear_model.pth')

# Modify the keys in the state dictionary to match the model's keys
new_state_dict = {}
for k, v in state_dict.items():
    if not k.startswith('linear.'):
        k = "linear." + k
    new_state_dict[k] = v
model.load_state_dict(new_state_dict)
@app.post("/predict/")
async def predict(input_data: float):
    input_tensor = torch.tensor([[input_data]], dtype=torch.float32)
    prediction = model(input_tensor)
    return {"prediction": prediction.item()}
