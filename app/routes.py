from flask import request, redirect, render_template
from app import app

import io
from fastai.vision import (
	open_image,
	load_learner
	)
from fastai.torch_core import defaults
import torch

def config_model():
    defaults.device = torch.device('cpu')
    model = load_learner('C:/Users/lennyphilips/Documents/image_classifier/app')
    return model

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():

	if request.method == 'POST':
		if request.files:
			file = request.files['image']
			print(file)            
			bytes = file.read()
			byteStream = io.BytesIO(bytes)


			model = config_model()
			image = open_image(byteStream)

			pred_class,label,prob = model.predict(image)
			
			#classes = [x for x in zip(model.data.classes, prob.tolist())]
			
			#print()
			
			return render_template('result.html', 
				result=str(pred_class), 
				classes=model.data.classes,
				likeliness=prob.tolist()
			)
			#return redirect(request.url)
	return render_template('index.html')
	

