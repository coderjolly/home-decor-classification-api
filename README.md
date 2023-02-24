## Object Classification API

 - This repository contains a rudimentary level flask API that is dockerized to return an answer whether the image uploaded is a bed, chair or sofa using a saved model with best accuracy.
 - Keras saves models in this format as it can easily store the weights and model configuration in a single file so that it can be used for prediction further. 
 
 - [ ] The model for classification on the dataset is enclosed under _____.ipnb and is saved at best configuration in an h5 file format.
 - [ ] An API access model is built using Flask that takes image as an input and returns the predicted label or category as output.
 - [ ] A dockerfile has been created which in turn creates a docker image for the above mentioned task.

## Steps to Run

 1. Make sure you have docker present on your system if not, use the documentation to install from [here.](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
 2. Clone this repo and reach inside the fulhaus-api folder using `cd fulhaus-api`
 3. Use `docker build -t flaskapp .` to build the dockefile for an image.
 4. After the image building is complete, use `docker run -p 5000:5000 flaskapp` to run the image and expose port 5000. (Ignore Tensorflow warnings)
 5. Now as the docker images is running with exposing the port at 5000, we can use Postman to hit the API.
 6. Using the address `0.0.0.0:5000/classification` in Postman and with Body form-data as file, we will can choose to upload an image from there. Please see the image below for reference.

 ![Reference for image uploading ](/ss1.png) 

 7. Keeping option as `POST`, send the request keeping the upload image in the form-data.
 8. Accordingly, wait for the response that is predicted/classified in the response section as Bed, Chair or Sofa.
