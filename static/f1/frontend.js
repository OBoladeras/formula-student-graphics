function createDriver(driver) {
    var driverDiv = document.createElement('div');
    driverDiv.className = 'driver';

    var position = document.createElement('h2');
    position.className = 'position';
    position.textContent = driver.position;

    var logo = document.createElement('img');
    logo.src = "/static/f1/logos/" + driver.logo;
    logo.alt = 'logo';

    var name = document.createElement('h2');
    name.textContent = driver.name;
    name.className = 'name';

    var time = document.createElement('h3');
    time.textContent = driver.time;
    time.className = 'time';

    driverDiv.appendChild(position);
    driverDiv.appendChild(logo);
    driverDiv.appendChild(name);
    driverDiv.appendChild(time);

    return driverDiv;
}

function getDrivers() {
    grid = document.getElementById('grid');

    fetch('/losmnHjnsytTgsbaH6hs8K9o/api/f1', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    }).then(response => response.json())
        .then(data => {
            for (var i = 0; i < data.drivers.length; i++) {
                grid.appendChild(createDriver(data.drivers[i]));
            }
        })
}

function updateTimer(targetTime) {
    timer = document.getElementById('timer');

    var currentTime = new Date();
    var remainingTime = targetTime - currentTime;
    console.log(remainingTime);

    if (remainingTime <= 0) {
        clearInterval(timerInterval);
        document.getElementById("timer").textContent = "Time's up!";
        return;
    }

    // var hours = Math.floor(remainingTime / (1000 * 60 * 60));
    var minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

    minutes = minutes.toString().padStart(2, '0');
    seconds = seconds.toString().padStart(2, '0');

    document.getElementById("timer").textContent = minutes + ":" + seconds;

    setTimeout(() => {
        updateTimer(targetTime);
    }, 1000);
}


/*
fetch('/losmnHjnsytTgsbaH6hs8K9o/api/f1', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
    },
}).then(response => response.json())
    .then(data => {
        timer = document.getElementById('timer');

        var timeParts = data.endTime.split(":");
        var hours = timeParts[0];
        var minutes = timeParts[1];

        var targetTime = new Date();
        targetTime.setHours(hours);
        targetTime.setMinutes(minutes);
        targetTime.setSeconds(0);
        targetTime.setMilliseconds(0);

        updateTimer(targetTime);
    })

*/

getDrivers();
