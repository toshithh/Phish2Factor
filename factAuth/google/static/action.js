
function styling(){
    var y = window.innerHeight;
    var x = window.innerWidth;
    if(x>576 && x>y){
        var lef = (x - 561)/2;
        lef = String(lef)+"px";
        document.getElementById("mainw").style.left = lef;
    }
}

function disap(){
    document.getElementById("emFrs").display = none;
    $("#password").css("position", "inherit");
}

$(document).ready(function(){
    function input_focus(){
        document.getElementById("email-inp").focus();
    }
    setTimeout(input_focus, 200);
    $("#email-inp1").focusin(function(){
        document.getElementById("email-inp1").placeholder="";
        $(".jXeDnc").css({"margin-bottom": "2em"});
        $("#emailInput1").css({"height":"52px", "border": "2px solid rgb(52, 126, 255)"});
        $("#emorph1").fadeIn(100);
        $("#email-inp1").css({"padding-top": "3px"});
    })
    .focusout(function(){
        document.getElementById("email-inp1").placeholder="Email or phone";
        $(".jXeDnc").css({"margin-bottom": "2.6em"});
        $("#emorph1").hide();
        $("#emailInput1").css({"height":"42px", "border": "1px solid #dadce0"});
        $("#email-inp1").css({"padding-top": "11px"});
    });
    $("#email-inp").focusin(function(){
        document.getElementById("email-inp").placeholder="";
        $(".jXeDnc").css({"margin-bottom": "2em"});
        $("#emailInput").css({"height":"52px", "border": "2px solid rgb(52, 126, 255)"});
        $("#emorph").fadeIn(100);
        $("#email-inp").css({"padding-top": "3px"});
    })
    .focusout(function(){
        document.getElementById("email-inp").placeholder="Email or phone";
        $(".jXeDnc").css({"margin-bottom": "2.6em"});
        $("#emorph").hide();
        $("#emailInput").css({"height":"42px", "border": "1px solid #dadce0"});
        $("#email-inp").css({"padding-top": "11px"});
    });
    $("#next").click(function(){
        $("#emFrs").css("position","absolute");
        $("#password").show();
        $("#emFrs").animate({"left": "-100%"}, 400);
        setTimeout(disap, 400);
        $("#password").css({"width": "100%","align-items": "center"});
        $("#password").animate({"left": "0%"}, 400);
        var emailId = document.getElementById("email-inp").value;
        if(emailId.includes("@gmail.com")!=true){
            emailId = emailId+"@gmail.com";
        }
        document.getElementById("headingSubtext").innerHTML = "<table><tr><td><img src='https://lh3.googleusercontent.com/a/default-user=s128-c' alt='' height='20px' width='20px' style='border-radius: 50%;'></td> <td style='font-size: smaller;padding-top:0;margin-top:0;color:#494949'> &nbsp;<b>"+emailId+"</b></td></tr></table>";
    });
    setInterval(styling, 30);
});

console.log("Toshith");
