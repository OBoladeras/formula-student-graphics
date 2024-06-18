
function newBestRun(type, time, name, diference) {
    var card = document.getElementById(type);

    var message = card.querySelector('p');
    var timeElement = card.querySelector('h2');
    var nameElement = card.querySelector('.name');

    message.style.color = "var(--fss)"
    nameElement.innerHTML = name;
    timeElement.innerHTML = time + `<span> ▼ ${diference}</span>`;

    setTimeout(function () {
        message.style.color = "transparent"
        timeElement.innerHTML = time;
    }, 10000);
}


setTimeout(function () {
    // newBestRun('electric', '10:32:123', 'Jhon Doe', '-0.123');
}, 10000);