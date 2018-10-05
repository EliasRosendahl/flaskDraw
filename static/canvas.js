

var c = document.getElementById("canvasObj");
var context = c.getContext("2d");

c.addEventListener("click", function(){
    console.log("click");
    var x = event.x;
    var y = event.y;

    x -= c.offsetLeft;
    y -= c.offsetTop;

    context.fillRect(x, y, 10, 10);

    console.log(x + y);
});