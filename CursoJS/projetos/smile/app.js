function init() {
    let ctx = document.getElementById("canvas").getContext('2d');
    ctx.beginPath();
    ctx.strokeStyle = "rgb(200, 0, 0)";
    ctx.arc(200, 200, 50, 0, Math.PI, false);
    ctx.fillStyle = "rgb(200,0,200)";
    ctx.closePath();
    ctx.fill();
    ctx.strokeStyle="rgb(255,0,0)";
    ctx.lineWidth=5;
    ctx.stroke();
}