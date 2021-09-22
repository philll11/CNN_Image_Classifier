## New Zealand Native Bird Classifier
This simple web app takes an image of a common New Zealand native bird and classifies which family it belongs to.

It uses a Convolutional Neural Network with a Resnet34 layer architechure.
It was only trained on 600 images as it leverages the ImageNet library, allowing for fast, low volume training.
Although it is a Neural Network, it does not require a GPU to run and therefore runs using the pytorch CPU distribution.

## Running the webapp
This app last ran successfully on Python version 3.7.4 - new versions of Python maybe not have a wheel support.

1. Install Python 3.7

2. Create a Python environment:

`python -m venv venv`

3. Activate virtual environment

`venv\Scripts\activate`

4. Gather dependancies, run the below pip command

`pip install flask`

`pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html`

`pip install fastai`

5. Run the Flask app

`Flask run`
