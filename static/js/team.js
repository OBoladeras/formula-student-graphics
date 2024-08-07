function update() {
    setTimeout(() => {
        fetch('/losmnHjnsytTgsbaH6hs8K9o/api/team')
            .then(response => response.json())
            .then(data => {
                if (currentNum == data.number) {
                    return;
                }
                currentNum = data.number;

                document.querySelector('.teamname').innerText = data.name;
                document.querySelector('.uni').innerText = data.uni;
                document.querySelector('.number').innerText = data.number;

                carPhoto = document.getElementById('carPhoto');

                if (carPhoto.src != `/static/cars/${data.number}.png`) {
                    carPhoto.src = `/static/cars/${data.number}.png`;
                }

                if (data.flag == 'none') {
                    document.querySelector('.flag').style.display = 'none';
                } else if (document.querySelector('.flag').style.backgroundImage != `url("/static/flags/${data.flag}.png")`) {
                    document.querySelector('.flag').style.backgroundImage = `url("/static/flags/${data.flag}.png")`;
                }
            });
        update();
    }, 100);
}

update();
