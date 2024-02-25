var formBtn = document.getElementById("register-btn");
var outerDiv = document.getElementById("outer-modal-div");
var innerDiv = document.getElementById("inner-modal-div");
var form = document.getElementById("register-vehicle");

formBtn.addEventListener("click", function (e) {
  e.preventDefault();
  outerDiv.style.display = "flex";
});

outerDiv.addEventListener("click", function (e) {
  outerDiv.style.display = "none";
});

form.addEventListener("click", function (e) {
  e.stopPropagation();  
});
