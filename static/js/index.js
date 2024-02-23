$(document).ready(function () {
  $("#seg-guide-btn").click(function () {
    $.ajax({
      url: "http://127.0.0.1:5000/guide",
      type: "GET",
      success: function (response) {
        console.log("Seg Loaded");
        $("#data-container").html(response);
        // Change the URL in the browser tab using History API
        window.history.pushState(null, null, "/guide");
      },
    });
  });
});

$(document).ready(function () {
    
})