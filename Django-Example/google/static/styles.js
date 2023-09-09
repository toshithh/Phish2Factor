function page_load(ele){
    $("#"+ele).focus();
    Trfm(ele);
}

function Trfm_trig(ele){
    window.setInterval(Trfm, 50, ele);
}

function Trfm(ele){
    var unm = document.getElementById(ele);
    if (ele=='username'){
        var phold = document.getElementById("unm-placeholder");
    }else{
        var phold = document.getElementById("pass-placeholder");
    }
    
    if (unm === document.activeElement){
        phold.classList.add("trfm");
    }
    else{
        if (unm.value == ""){
            phold.classList.remove("trfm");
        }
    }
}

function unm_next(){
    $("#use").hide();
    $("#pass").show();
}

function submit(){
    elem = document.getElementById("username");
    window.location.href="fact2?username="+encodeURIComponent(elem.value);
}