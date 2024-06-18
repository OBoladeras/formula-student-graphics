function update() {
    setTimeout(() => {
        fetch('/api/currentteam')
            .then(response => response.json())
            .then(data => {
                document.querySelector('.number').innerText = data.number;
                document.querySelector('.teamname').innerText = data.name;
                document.querySelector('.uni').innerText = data.uni;
                document.querySelector('.flag').style.backgroundImage = `url('static/flags/${data.flag}.png')`;
            });
        update();

    }, 5000);
}

update();