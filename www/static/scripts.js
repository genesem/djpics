

/* javascript */



var hcrss = document.querySelector("span.msgi")||0;

if(hcrss) {
 hcrss.onclick=function(){
    console.log('home msg cross click');
    this.parentElement.style.display='none';return false;
 }

}

