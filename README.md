# Community-Pothole-Reporting-and-Detection

## Introduction
This project focuses on detecting potholes using deep learning models, including a fine-tuned VGG16 model and a custom CNN. The goal is to assist in maintaining road safety by identifying potholes from images.

## Technologies Used
- TensorFlow/Keras
- Boto3
- Flask
- AWS S3
  
## Data Collection
- The dataset consists of 8,000 road images collected from Kaggle, containing both pothole and plain road images.

## Model Architecture
- VGG16: Pre-trained model fine-tuned with additional layers.
- Custom CNN: A simple CNN model designed for this task.

## Training
- Accuracy: The VGG16 model achieved 98.48% accuracy in training and 98% in validation.
  
## Web Integration
A simple web page allows users to upload images of potholes, which are then stored in an AWS S3 bucket and used by the model for detection.
