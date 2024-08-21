# Community-Pothole-Reporting-and-Detection

## Introduction
This project focuses on detecting potholes using deep learning models, including a fine-tuned VGG16 model and a custom CNN. The goal is to assist in maintaining road safety by identifying potholes from images.

## Technologies Used
TensorFlow/Keras: For model development and training.
Boto3: For integrating with AWS S3 to store images uploaded through a web page.
Google Colab: For training and experimentation.
Flask: For building the simple web page for image uploads.
Data Collection
The dataset consists of 8,000 road images collected from Kaggle, containing both pothole and non-pothole images.

## Data Preprocessing
Resizing: Images resized to 224x224 pixels.
Normalization: Pixel values scaled between 0 and 1.
Augmentation: Techniques like rotation, flipping, and zooming were applied to enhance model performance.
## Model Architecture
VGG16: Pre-trained model fine-tuned with additional layers.
Custom CNN: A simple CNN model designed for this task.
## Training and Evaluation
Accuracy: The VGG16 model achieved 98.48% accuracy in training and 98% in validation.
Optimization: Used Adam optimizer, early stopping, and learning rate reduction for model training.
## Web Integration
A simple web page allows users to upload images of potholes, which are then stored in an AWS S3 bucket and used by the model for detection.
