last = {};
var best = { "fuel": "0", "electric": "0", "race": null };

function newBest(type) {
    item = document.getElementById(type);

    item.children[0].style.width = '3.5rem';
    dataBlock = item.getElementsByClassName('run')[0];

    dataBlock.getElementsByClassName('timeL')[0].style.color = 'var(--best-time)';


    setTimeout(function () {
        item = document.getElementById(type);
        dataBlock = item.getElementsByClassName('run')[0];

        item.children[0].style.width = '0px';
        dataBlock.getElementsByClassName('timeL')[0].style.color = '#fff';
    }, 5000);
}



function getLast() {
    fetch('/losmnHjnsytTgsbaH6hs8K9o/api/last')
        .then(response => response.json())
        .then(data => {
            if (best != data) {
                best = data;
                console.log(data);

                document.getElementById('last').getElementsByClassName('time')[0].innerHTML = data.time;
                document.getElementById('last').getElementsByClassName('number')[0].innerHTML = data.number;
                document.getElementById('last').getElementsByClassName('uni')[0].innerHTML = data.uni;
                document.getElementById('last').getElementsByClassName('name')[0].innerHTML = data.teamname;

                document.getElementById('last').classList.remove('hide');

                setTimeout(function () {
                    document.getElementById('last').classList.add('hide');
                }, 25000);
            }
        });
}

function getBest() {
    globalThis.best = best;

    fetch('/losmnHjnsytTgsbaH6hs8K9o/api/best')
        .then(response => response.json())
        .then(data => {
            race = data.race;
            fuel = data.fuel;
            electric = data.electric;

            if (best['fuel'] != fuel.time || best["race"] != race) {
                newBest('fuel');
                fuelItem = document.getElementById('fuel')
                fuelItem.getElementsByClassName('timeL')[0].innerHTML = fuel.time;
                fuelItem.getElementsByClassName('number')[0].innerHTML = fuel.number;
                fuelItem.getElementsByClassName('uni')[0].innerHTML = fuel.uni;
                fuelItem.getElementsByClassName('name')[0].innerHTML = fuel.name;

                console.log('new best fuel');
                best['fuel'] = fuel.time;
                best['race'] = race;
            }

            if (best['electric'] != electric.time || best["race"] != race) {
                newBest('electric');
                electricItem = document.getElementById('electric')
                electricItem.getElementsByClassName('timeL')[0].innerHTML = electric.time;
                electricItem.getElementsByClassName('number')[0].innerHTML = electric.number;
                electricItem.getElementsByClassName('uni')[0].innerHTML = electric.uni;
                electricItem.getElementsByClassName('name')[0].innerHTML = electric.name;

                console.log('new best electric');
                best['electric'] = electric.time;
                best['race'] = race;
            }
        });
}


setInterval(getBest, 5000);
getBest();