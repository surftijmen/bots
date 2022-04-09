document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);
let page = document.getElementById("copy-page");
let input = document.getElementById("input");
page.addEventListener("click", ()=>{eel.setPageContent(input.value)}, false);

let pagetext = document.getElementById("text");

eel.expose(copyPage);
eel.expose(prompt_alerts);

function prompt_alerts(description) {
  alert(description);
}

function copyPage(content) {
  console.log(content)
  pagetext.innerHTML = content;
}