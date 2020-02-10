# CNN_Image_Classifier

## New Zealand Native Bird Classifier
This simple web app takes an image of a common New Zealand native bird and classifies which family it belongs to.

It uses a Convolutional Neural Network with a Resnet34 layer architechure.
It was only trained on 600 images as it leverages the ImageNet library, allowing for fast, low volume training.
Although it is a Neural Network, it does not require a GPU to run and therefore runs using the pytorch CPU distribution.
