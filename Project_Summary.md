# Project Title: Chest X-Ray Image Recognition
### Dataset: Chest X-Ray (Pneumonia,Covid-19,Tuberculosis) (available here: https://www.kaggle.com/datasets/jtiptj/chest-xray-pneumoniacovid19tuberculosis)

# Project Summary:
This project was initially done as part of the course requirements for CS7641: Machine Learning at the Georgia Institute of Technology. The project was primarily carried out using Numpy and Tensorflow. \
\
I have redone this project using OpenCV and Pytorch. The raw images from the '/Data' folder were grayscaled, resized and saved into the '/Data_processed' folder using OpenCV. \
\
The actual images can be found on the Kaggle link posted above. They are not included in this repo due to memory constraints. The processed images were done loaded into the Datloader from  Pytorch. \
\
Transformations were applied to the images to standardize the images and make it efficient for the model to be trained. A simple CNN model was built using the 'nn' module from Pytorch.
