function upload(event) {
	var image = document.getElementById('upload-image');
	image.src = URL.createObjectURL(event.target.files[0]);
	
	document.getElementById('submit-btn').disabled = false;
		
	var image_name = document.getElementById('image-name');
	image_name.textContent = event.target.files[0].name;
};

function validate() {
	console.log(document.getElementById('custom-file-input').upload_button.files.length)
	if(document.getElementById('custom-file-input').upload_button.files.length == 0) {
		document.getElementById('submit-btn').disabled = true;
	} else {
		document.getElementById('submit-btn').disabled = false;
	}
}
function reset() {
	document.getElementById('submit-btn').disabled = false;
}