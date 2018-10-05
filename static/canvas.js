

var c = document.getElementById("canvasObj");
var context = c.getContext("2d");

c.addEventListener("click", function(){
    //store original imgData to compare the difference
    //TODO : should take previous imgDataNew 
    var imgDataOld = context.getImageData(0, 0, 720, 480);

    var x = event.x;
    var y = event.y;

    x -= c.offsetLeft;
    y -= c.offsetTop;

    context.fillRect(x, y, 10, 10);
    
    var imgDataNew = context.getImageData(0, 0, 720, 480);
    var imgDataDiff = {data: {}};

    for (let index = 0; index < imgDataNew.data.length; index++) {
        if(imgDataOld.data[index] !== imgDataNew.data[index]){
            imgDataDiff.data[index] = imgDataNew.data[index];
        }
    }
});