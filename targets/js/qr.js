const qrParams = new URLSearchParams(window.location.search);
var manuf = encodeURIComponent(qrParams.get("manf"));
var prods = encodeURIComponent(qrParams.get("prod"));

document.getElementById("prod-preview").src = `preview/index.html?man=${manuf}&prod=${prods}`;
document.getElementById("drone-welcome").innerHTML = `Congratulations on puchasing your new ${manuf} drone!`;