function getPosition(id, pos) {
    const element = document.getElementById(id);
    const rect = element.getBoundingClientRect();

    if (pos === 'left') {
        return rect.left;
    } else if (pos === 'right') {
        return rect.right;
    }
}


function update() {
    setTimeout(() => {
        fetch('/api/currentteam')
            .then(response => response.json())
            .then(data => {
                if (currentNum == data.number) {
                    return;
                }
                currentNum = data.number;
                var car = document.getElementById('car');
                const pushedDiv = document.getElementById('pushedDiv');

                car.style.transform = "translateX(150vw)";
                setTimeout(() => {
                    pushedDiv.style.transform = "translateX(150vw)";
                }, 750);


                setTimeout(() => {
                    car.style.transition = 'transform 0s linear';
                    car.style.transform = 'rotateY(180deg)';
                    car.style.transition = 'transform 4s linear';

                    document.querySelector('.number').innerText = data.number;
                    document.querySelector('.teamname').innerText = data.name;
                    document.querySelector('.uni').innerText = data.uni;

                    if (data.flag == 'none') {
                        document.querySelector('.flag').style.display = 'none';
                    } else if (document.querySelector('.flag').style.backgroundImage != `url("/static/flags/${data.flag}.png")`) {
                        document.querySelector('.flag').style.backgroundImage = `url("/static/flags/${data.flag}.png")`;
                    }
                }, 4000);
            });
        update();
    }, 5000);
}

function wait4Movement() {
    const car = document.getElementById('car');
    const pushedDiv = document.getElementById('pushedDiv');
    setTimeout(() => {
        var carPosition = getPosition('car', 'right');
        var pushedPosition = getPosition('pushedDiv', 'left');

        if (carPosition > pushedPosition) {
            console.log('carPosition', carPosition);
            console.log('pushedPosition', pushedPosition);
            pushedDiv.style.animation = "push 3s linear";
            pushedDiv.style.transform = `translateX(${carPosition}px)`;
        } else {
            wait4Movement();
        }
    }, 200);
}


update();
