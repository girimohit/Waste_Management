x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(sendLocation);
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

function sendLocation(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
}
