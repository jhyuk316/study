var isOn = true;

function toggle() {
  //   const btn = document.getElementById("btn");
  //   const btn = document.querySelector("#btn");

  isOn = !isOn;
  if (isOn) {
    btn.textContent = "ON";
    btn.style.color = "red";
    btn.style.fontWeight = "bold";
  } else {
    btn.textContent = "OFF";
    btn.style.color = "black";
    btn.style.fontWeight = "normal";
  }
}

const rootApp = document.getElementById("root");
rootApp.innerHTML = '<button id="btn" onclick="toggle();">ON</button>';
// rootApp.textContent = '<button id="btn" onclick="toggle();">ON</button>';

const btn = document.querySelector("#btn");

btn.style.width = "400px";
btn.style.fontSize = "40px";
btn.style.backgroundColor = "LightSkyBlue";
// btn.style.border = "1px dotted blue";
btn.style.border = "0px";
btn.style.padding = "20px";
btn.style.color = "red";
btn.style.fontWeight = "bold";
