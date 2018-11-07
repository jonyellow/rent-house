var over = document.getElementsByClassName("op");
var sign_box = document.getElementById("sign_box");
var log_box = document.getElementById("log_box");
sign_box.style.zIndex =  500;
log_box.style.zIndex =  1000;
function sign_hide(){
    sign_box.style.display = 'block';
    over.style.display='block';
}
function succ_zhuce(){
    alert("尼玛,注册成功了!去点击登录.....");
}
function log_hide(){
    log_box.style.display = 'block';
    over.style.display='block';
}
