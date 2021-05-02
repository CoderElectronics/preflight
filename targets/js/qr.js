const qrParams = new URLSearchParams(window.location.search);

var itemid = encodeURIComponent(qrParams.get("item"));

fetch('/targets/tr.json')
  .then(response => response.json())
  .then(data => loadArray(data))

function loadArray(dataarray) {
    dataarray.forEach(function (item, index) {
        if (itemid == item[4]) {
            document.getElementById("prod-preview").src = `preview/index.html?man=${item[1]}&prod=${item[0]}`;
            document.getElementById("drone-welcome").innerHTML = `Congratulations on puchasing your new ${item[1]} drone!`;
        }
    });
}