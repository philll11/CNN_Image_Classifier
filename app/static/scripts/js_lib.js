function upload(event) {
	var image = document.getElementById('upload-image');
	image.src = URL.createObjectURL(event.target.files[0]);
		
	var image_name = document.getElementById('image-name');
	image_name.textContent = event.target.files[0].name;
};