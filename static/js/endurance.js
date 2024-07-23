function getDrivers() {
    grid = document.getElementById('grid');

    fetch('/losmnHjnsytTgsbaH6hs8K9o/api/endurance', {
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

getDrivers();
