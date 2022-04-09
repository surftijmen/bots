document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}