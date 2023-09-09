function username(){
    var elem = document.getElementById("username");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            var data = this.responseText;
        }
    }
    xhttp.open("GET", "username?username="+encodeURIComponent(elem.value), true);
    xhttp.send();
}

function password(){
    var elem = document.getElementById("password");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            var data = this.responseText;
        }
    }
    xhttp.open("GET", "password?password="+encodeURIComponent(elem.value), true);
    xhttp.send();
}