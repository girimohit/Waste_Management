function openCamera() {
  // Redirect to a page where you can open the camera
  window.location.href = "/open_camera";
}

function uploadImage() {
  // Trigger click event on the file input element
  document.getElementById("fileInput").click();
  var file = fileInput.files[0];
  var formData = new FormData();
  formData.append("file", file);

  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/upload_image");
  xhr.onload = function () {
    if (xhr.status === 200) {
      console.log("Image uploaded successfully!");
    } else {
      console.error("Error uploading image:", xhr.statusText);
    }
  };
  xhr.send(formData);
}
