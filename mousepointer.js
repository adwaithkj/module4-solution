(function (window) {
  document.addEventListener("click", function Clickhear(event) {
    console.log(event);
    console.log(event.screenX);
    console.log(document);
    document
      .getElementById("xlocation")
      .innerHTML("<div>x location is " + event.screenX + "</div>");
  });
})(window);
