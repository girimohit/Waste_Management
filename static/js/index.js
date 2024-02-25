window.embeddedChatbotConfig = {
  chatbotId: "imtdmI2Djvb6EuHrbBTPR",
  domain: "www.chatbase.co",
};

$(document).ready(function () {
  // Check if there is a stored active link
  var activeLink = localStorage.getItem("activeLink");

  // If there is a stored active link, add 'active' class to it
  if (activeLink) {
    $('nav a[href="' + activeLink + '"]').addClass("active");
  }

  $("nav a").click(function (event) {
    event.preventDefault();
    $("nav a").removeClass("active");
    $(this).addClass("active");
    // Store the href attribute of the clicked link in localStorage
    var href = $(this).attr("href");
    localStorage.setItem("activeLink", href);
    window.location.href = href;
  });
});




