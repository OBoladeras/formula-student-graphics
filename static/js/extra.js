function createDriver(data, p) {
    const driver = document.createElement('div');
    driver.classList.add('driver');

    const position = document.createElement('div');
    position.classList.add('position');
    position.innerText = p + 1;
    driver.appendChild(position);

    const img = document.createElement('img');
    console.log(data.flag);
    url = `/static/flags/${data.flag}.png`;
    if (url != `/static/flags/.png`) {
        img.src = `/static/flags/${data.flag}.png`;
    } else {
        img.src = `/static/flags/Spain.png`;
    }
    driver.appendChild(img);

    const info = document.createElement('div');
    info.classList.add('info');
    driver.appendChild(info);

    const name = document.createElement('p');
    name.classList.add('name');
    name.innerText = data.name;
    info.appendChild(name);

    const times = document.createElement('div');
    times.classList.add('times');
    info.appendChild(times);

    const best = document.createElement('p');
    best.style.color = 'rgb(86, 167, 86)';
    best.innerText = 'BEST - ' + data.best;
    times.appendChild(best);

    const last = document.createElement('p');
    last.style.color = 'rgb(98, 98, 222)';
    last.innerText = 'LAST - ' + data.last;
    times.appendChild(last);

    const lap = document.createElement('div');
    lap.classList.add('lap');
    driver.appendChild(lap);

    const lapHead = document.createElement('p');
    lapHead.classList.add('lapHead');
    lapHead.innerText = 'LAP';
    lap.appendChild(lapHead);

    const lapValue = document.createElement('p');
    lapValue.innerText = data.lap;
    lap.appendChild(lapValue);

    const classLap = document.createElement('div');
    classLap.classList.add('lap');
    classLap.style.marginLeft = '0';
    driver.appendChild(classLap);

    const classHead = document.createElement('p');
    classHead.classList.add('lapHead');
    classHead.classList.add('class');
    classHead.innerText = 'CLASS';
    classLap.appendChild(classHead);

    const classValue = document.createElement('p');
    classValue.innerText = data.class;
    classLap.appendChild(classValue);

    document.querySelector('.drivers').appendChild(driver);
}

function getDrivers() {
    fetch('/losmnHjnsytTgsbaH6hs8K9o/api/extra')
        .then(response => response.json())
        .then(data => {
            document.querySelector('.drivers').innerHTML = '';

            for (let i = 0; i < data.length; i++) {
                createDriver(data[i], i);
            }
        });
}

getDrivers();
setInterval(getDrivers, 10000);