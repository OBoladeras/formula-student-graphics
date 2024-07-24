function newDriver(data) {
    let driver = document.createElement("div");
    driver.classList.add("driver");

    let info = document.createElement("div");
    info.classList.add("info");

    let base = document.createElement("div");
    base.classList.add("base");

    let name = document.createElement("p");
    name.classList.add("name");
    name.innerText = data.name;

    let times = document.createElement("div");
    times.classList.add("times");

    let best = document.createElement("p");
    best.style.color = "rgb(86, 167, 86)";
    best.innerHTML = "B-" + data.best;

    let last = document.createElement("p");
    last.style.color = "rgb(98, 98, 222)";
    last.innerHTML = "L-" + data.last;

    times.appendChild(best);
    times.appendChild(last);

    base.appendChild(name);
    base.appendChild(times);

    let number = document.createElement("div");
    number.classList.add("number");
    number.innerText = data.number;

    info.appendChild(base);
    info.appendChild(number);

    driver.appendChild(info);

    document.getElementById("grid").appendChild(driver);
}


function getDrivers() {
    fetch("/losmnHjnsytTgsbaH6hs8K9o/api/endurance")
        .then(response => response.json())
        .then(data => {
            document.getElementById("grid").innerHTML = "";

            for (let i = 0; i < data.length; i++) {
                newDriver(data[i]);
            }
        });
}

setInterval(getDrivers, 20000);
getDrivers();