# FastAPI PyTorch Docker Fargate Demo
This is a demo project showcasing the use of FastAPI, PyTorch, Docker, and AWS Fargate for deploying a simple linear regression model.

## Model
The model used in this project is a simple linear regression model with the formula y = 2 * x.
https://drive.google.com/file/d/1IUCfL1uuWOn-MCixitZ0jmAfEEB5KiPV/view?usp=sharing
## Technologies Used
- PyTorch: Used for building and training the linear regression model.
- Docker: Used for containerization of the application.
- FastAPI: Used as the web server for serving the AI model.
- AWS Fargate: Used for deployment of the application.
## How to build DockerImage
- Install Docker
- In Destination folder run this command: `docker build -t docker_image_name .`
## Why whl file is included?
Unfortunately, installing Torch 2.2.0 with the requirements file failed.
This is because fastapi is supported in Python 3.8 and above, and docker couldn't find a stable version in the his environment.
## Deployment
The application is deployed using Amazon CloudFormation and AWS Fargate. The necessary configuration files for deployment are included in the repository.
- Build image

![Image Description](./descrition_images/1.PNG)
- Set up ECR

![Image Description](./descrition_images/2.PNG)
![Image Description](./descrition_images/3.PNG)
- Tag Image

![Image Description](./descrition_images/4.PNG)
- Log in

![Image Description](./descrition_images/5.PNG)
![Image Description](./descrition_images/6.PNG)
- Push Image

![Image Description](./descrition_images/7.PNG)
- Create Cluster

![Image Description](./descrition_images/8.PNG)
![Image Description](./descrition_images/9.PNG)
![Image Description](./descrition_images/10.PNG)
- Define Task

![Image Description](./descrition_images/11.PNG)
![Image Description](./descrition_images/12.PNG)
![Image Description](./descrition_images/13.PNG)
![Image Description](./descrition_images/14.PNG)

![Image Description](./descrition_images/15.PNG)
- Create Service

![Image Description](./descrition_images/16.PNG)
![Image Description](./descrition_images/17.PNG)
![Image Description](./descrition_images/18.PNG)
![Image Description](./descrition_images/19.png)
![Image Description](./descrition_images/20.PNG)
- Confirm the task is running

![Image Description](./descrition_images/21.PNG)
![Image Description](./descrition_images/22.png)
- Test the result

![Image Description](./descrition_images/23.PNG)
![Image Description](./descrition_images/24.PNG)

## Usage
To run the application locally, follow these steps:

### Clone the repository.
Build the Docker image using the provided Dockerfile.
Run the Docker container.
Access the FastAPI web server at http://localhost:8000.
### API Endpoints
/predict/{x}: Given an input x, the API endpoint will return the predicted output y using the trained linear regression model.
## Contributors

Feel free to contribute to this project by creating a pull request. If you have any questions or suggestions, please open an issue.
Please cantact if any issues. aitechguy0105@gmail.com
Thank you for checking out this demo project!