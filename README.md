## New Zealand Native Bird Classifier
This simple web app takes an image of a common New Zealand native bird and classifies which family it belongs to.

It uses a Convolutional Neural Network with a Resnet34 layer architechure.
It was only trained on 600 images as it leverages the ImageNet library, allowing for fast, low volume training.
Although it is a Neural Network, it does not require a GPU to run and therefore runs using the pytorch CPU distribution.

## Running the webapp
This app last ran successfully on Python version 3.7.4

First, create a Python environment:

`py -m venv venv`

Then:

`venv\Scripts\activate`

To gather dependancies, run the below pip command:

`pip install -r stable-req.txt`

To run the Flask app:

`Flask run`
