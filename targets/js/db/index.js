
function getCells(data, type) {
    return data.map(cell => `<${type}>${cell}</${type}>`).join('');
}

function createBody(data) {
    return data.map(row => `<tr>${getCells(row, 'td')}</tr>`).join('');
}

fetch('/targets/tr.json')
  .then(response => response.json())
  .then(data => document.getElementById("dbbody").insertAdjacentHTML('beforeend', createBody(data)))