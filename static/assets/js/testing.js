
function fun(option) {
    
    console.log(option.innerHTML);
    var arr = []
    arr.push(document.querySelector(".carcolor"));
    arr.push(document.querySelector(".detailscolor"));
    arr.push(document.querySelector(".interiorcolor"));
    arr.push(document.querySelector(".engine"));
    arr.push(document.querySelector(".rim"));
    arr.push(document.querySelector(".spoiler"));
    for(let i=0;i<arr.length;i++) {
        if(arr[i].className == option.id) {
            arr[i].style.display = 'block';
        }
        else{
            arr[i].style.display = 'none';
        }
    }
}
var speed;
var horsepower;
var acceleration;
var handling;
var braking;
var si;
var hpi;
var ai;
var at;
var hi;
var ht;
var s;
var hp;
var a;
var h;
var myVar
function hasan(s, hp, a, h) {
    this.ai = 0.1;
    this.at = 0.1;
    this.hpi = 1;
    this.si = 1;
    this.hi = 1;
    this.ht = 1;
    this.s = s;
    this.hp = hp;
    this.a = a;
    this.h = h;
    var speed = document.querySelector("#speed");
    this.speed = speed;
    this.horsepower = document.querySelector("#horsepower");
    this.acceleration = document.querySelector("#acceleration");
    this.handling = document.querySelector("#handling");
    this.myVar = setInterval(myTimer, 1);
    
    console.log(this.speed);
    // setInterval(function() {
    // for(let i=0;i<info;i++) {
        
    //         speed.innerHTML = i.toString();
        
    //     }
    // }, 3000);
}
function myTimer() {
    this.speed.innerHTML = si.toString();
    this.horsepower.innerHTML = hpi.toString();
    this.acceleration.innerHTML = ai.toString();
    this.handling.innerHTML = hi.toString();
    this.si = this.si + Math.floor(this.s/100);
    this.hpi = this.hpi + Math.floor(this.hp/100);
    // this.ai = this.ai + parseFloat(a).toFixed(2)/100;
    this.at += (this.a/100);
    this.ai = Math.round(this.at*10)/10;

    this.ht += this.h/100;
    this.hi = Math.round(this.ht);
    // this.hi = this.hi + Math.floor(this.h/100);
    if(this.si > this.s/3) {
        this.speed.innerHTML = this.s.toString();
        this.horsepower.innerHTML = this.hp.toString();
        this.acceleration.innerHTML = this.a.toString();
        this.handling.innerHTML = this.h.toString();
        clearInterval(myVar)
    }
}

function prakash(b) {
    this.braking = document.querySelector("#braking");
    braking.innerHTML = b;
}
a = [1, 2]
// function hasan(id) {
//     a[id] = document.getElementById(id);
// }

// let a = 10000;
// export { a };

function mousedown() {
    document.querySelector("#first").innerHTML = document.querySelector("#cc").innerHTML + "<span aria-hidden>_</span>";
    document.querySelector("#second").innerHTML = document.querySelector("#dc").innerHTML + "<span aria-hidden>_</span>";
    document.querySelector("#third").innerHTML = document.querySelector("#ic").innerHTML + "<span aria-hidden>_</span>";
    document.querySelector("#fourth").innerHTML = document.querySelector("#et").innerHTML + "<span aria-hidden>_</span>";
    document.querySelector("#fifth").innerHTML = document.querySelector("#r").innerHTML + "<span aria-hidden>_</span>";
    document.querySelector("#sixth").innerHTML = document.querySelector("#s").innerHTML + "<span aria-hidden>_</span>";
}
function mouseup() {
    document.querySelector("#first").innerHTML = "CAR COLOR" + "<span aria-hidden>_</span>" + "<span aria-hidden class='cybr-btn__glitch'>DETAILS COLOR</span>";
    document.querySelector("#second").innerHTML = "DETAIL COLOR" + "<span aria-hidden>_</span>" + "<span aria-hidden class='cybr-btn__glitch'>DETAILS COLOR</span>";
    document.querySelector("#third").innerHTML = "INTERIOR COLOR" + "<span aria-hidden>_</span>" + "<span aria-hidden class='cybr-btn__glitch'>DETAILS COLOR</span>";
    document.querySelector("#fourth").innerHTML = "ENGINE TYPE" + "<span aria-hidden>_</span>" + "<span aria-hidden class='cybr-btn__glitch'>DETAILS COLOR</span>";
    document.querySelector("#fifth").innerHTML = "RIMS" + "<span aria-hidden>_</span>" + "<span aria-hidden class='cybr-btn__glitch'>DETAILS COLOR</span>";
    document.querySelector("#sixth").innerHTML = "SPOILERS" + "<span aria-hidden>_</span>" + "<span aria-hidden class='cybr-btn__glitch'>DETAILS COLOR</span>";
}


function pricelimitchange() {
    document.getElementById("cost1").innerHTML = document.getElementById("vol").value;
}