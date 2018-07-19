

/* javascript */

var hcrss = document.querySelector("span.msgi")||0;
var srch = document.getElementById('search')||0;

if(hcrss) {
 hcrss.onclick=function(){
    console.log('home msg cross click');
    this.parentElement.style.display='none';return false;
 }

}



srch.addEventListener('keypress', function(event) {
        if (event.keyCode == 13) {
            var s = srch.value;
            if(s.length){
            console.log('go search for tags:'+s);
            self.location.href = "/?q="+s; }
            event.preventDefault();
        }
    });