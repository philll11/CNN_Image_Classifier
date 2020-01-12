from flask import request, render_template
from app import app

import io
from fastai.vision import open_image, load_learner
from fastai.torch_core import defaults, Path
import torch


PATH = Path(__file__).parent

def config_model():
    defaults.device = torch.device('cpu')
    model = load_learner(PATH/'models')
    return model

@app.route('/', methods=['GET', 'POST'])
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
			
			
			return render_template('result.html', 
				result=str(pred_class), 
				classes=model.data.classes,
				likeliness=prob.tolist()
			)
			#return redirect(request.url)
	return render_template('index.html')


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)

