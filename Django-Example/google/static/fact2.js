
function styling(){
    var y = window.innerHeight;
    var x = window.innerWidth;
    if(x>576 && x>y){
        var lef = (x - 561)/2;
        lef = String(lef)+"px";
        document.getElementById("mainw").style.left = lef;
    }
}

$(document).ready(function(){
    setInterval(styling, 30);
})
