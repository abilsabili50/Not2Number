document.getElementById('formFile').addEventListener('change', function() {
	const submitBtn = document.getElementById('submitBtn');
	const successAlert = document.getElementById('alert');
	const fileInputValue = this.value;

	if(fileInputValue){
		successAlert.classList.remove("hidden");
	}

	// Enable the button if a file has been chosen
	submitBtn.disabled = !fileInputValue;
});