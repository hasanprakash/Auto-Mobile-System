// document.getElementById("reg").onsubmit = function(e) {
//     // $.ajax({
//     //     type:'POST', 
        
//     // });
// }

function showpause() {
    document.getElementById("pause").style.display = 'block';
    document.getElementById("play").style.display = 'none'
}
function showplay() {
    document.getElementById("pause").style.display = 'none';
    document.getElementById("play").style.display = 'block';
}
function showmute() {
    document.getElementById("mute").style.display = 'block';
    document.getElementById("unmute").style.display = 'none';
}
function showunmute() {
    document.getElementById("mute").style.display = 'none';
    document.getElementById("unmute").style.display = 'block';
}