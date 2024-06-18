function update() {
    setTimeout(() => {
        fetch('/api/currentteam')
            .then(response => response.json())
            .then(data => {
                document.querySelector('.number').innerText = data.number;
                document.querySelector('.teamname').innerText = data.name;
                document.querySelector('.uni').innerText = data.uni;

                if (data.flag == 'none') {
                    document.querySelector('.flag').style.display = 'none';
                } else if (document.querySelector('.flag').style.backgroundImage != `url("/static/flags/${data.flag}.png")`) {
                    document.querySelector('.flag').style.backgroundImage = `url("/static/flags/${data.flag}.png")`;
                }
            });
        update();

    }, 5000);
}

update();