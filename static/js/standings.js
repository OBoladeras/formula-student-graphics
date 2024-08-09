data = []

function createDriver(data, p, race) {
    const driver = document.createElement('div');
    driver.classList.add('driver');

    const position = document.createElement('div');
    position.classList.add('position');
    position.innerText = p; // data.position;
    driver.appendChild(position);

    const img = document.createElement('img');
    console.log(data.flag);
    url = `/static/flags/${data.flag}.png`; // Flag url
    if (url != `/static/flags/.png` && url != `/static/flags/undefined.png`) {
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
    name.innerText = data.name; // Name of the team
    info.appendChild(name);

    const times = document.createElement('div');
    times.classList.add('times');
    info.appendChild(times);

    const last = document.createElement('p');
    const best = document.createElement('p');
    if (race == "endurance") {
        best.style.color = 'rgb(86, 167, 86)';
        best.innerText = 'BEST - ' + data.best; // Best lap time

        last.style.color = 'rgb(98, 98, 222)';
        last.innerText = 'LAST - ' + data.last; // Last lap time
    } else {
        best.innerText = data.uni; // University name
        best.style.fontWeight = 'bold';
    }
    times.appendChild(best);
    times.appendChild(last);

    const lap = document.createElement('div');
    lap.classList.add('lap');
    driver.appendChild(lap);

    const lapHead = document.createElement('p');
    lapHead.classList.add('lapHead');
    lap.appendChild(lapHead);

    const lapValue = document.createElement('p');
    if (race == "endurance") {
        lapHead.innerText = 'LAP';
        lapValue.innerText = data.lap; // Current lap
    } else {
        lapHead.innerText = 'TIME';
        lapValue.innerText = data.time; // Time of the best lap
        lapValue.style.width = '7rem';
    }
    lap.appendChild(lapValue);

    if (race == "endurance") {
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
        classValue.innerText = data.class; // Class of the car
        classLap.appendChild(classValue);
    }

    document.querySelector('.drivers').appendChild(driver);
}

function getDrivers() {
    fetch('/api/standings')
        .then(response => response.json())
        .then(data => {
            race = data[0];
            document.getElementById("raceName").innerHTML = race.charAt(0).toUpperCase() + race.slice(1);

            globalThis.data = data;
        });
}

function displayDriversInBatches(startIndex, batchSize, delay) {
    let endIndex = Math.min(startIndex + batchSize, data.length);

    document.querySelector('.drivers').innerHTML = '';
    for (let i = startIndex; i < endIndex; i++) {
        createDriver(data[i], i, data[0]);
    }

    let nextStartIndex = endIndex;

    if (endIndex >= data.length) {
        nextStartIndex = 1;
    }

    setTimeout(() => {
        document.querySelector('.drivers').innerHTML = '';
        displayDriversInBatches(nextStartIndex, batchSize, delay);
    }, delay);
}

getDrivers();
setInterval(getDrivers, 40000);
setTimeout(() => {
    displayDriversInBatches(1, 6, 10000);
}, 5000);
