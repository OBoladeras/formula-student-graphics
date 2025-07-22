var best = { "fuel": "0", "electric": "0", "race": null };


function getBest() {
    globalThis.best = best;

    fetch('/api/best')
        .then(response => response.json())
        .then(data => {
            race = data.race;
            fuel = data.fuel;
            electric = data.electric;
            console.log('best data', data);

            if (best['fuel'] != fuel.time || best["race"] != race) {
                best_time_university_cv = document.getElementById('best_time_university_cv');
                best_time_time_cv = document.getElementById('best_time_time_cv');
                best_time_car_number_cv = document.getElementById('best_time_car_number_cv');
                best_time_team_cv = document.getElementById('best_time_team_cv');

                best_time_university_cv.innerHTML = fuel.uni;
                best_time_time_cv.innerHTML = fuel.time;
                best_time_car_number_cv.innerHTML = fuel.number;

                best_time_team_cv.src = "../../static/icons/team_parts/" + fuel.number + ".png";


                best['fuel'] = fuel.time;
                best['race'] = race;
            }

            if (best['electric'] != electric.time || best["race"] != race) {
                best_time_university_ev = document.getElementById('best_time_university_ev');
                best_time_time_ev = document.getElementById('best_time_time_ev');
                best_time_car_number_ev = document.getElementById('best_time_car_number_ev');
                best_time_team_ev = document.getElementById('best_time_team_ev');

                best_time_university_ev.innerHTML = electric.uni;
                best_time_time_ev.innerHTML = electric.time;
                best_time_car_number_ev.innerHTML = electric.number;

                best_time_team_ev.src = "../../static/icons/team_parts/" + electric.number + ".png";

                best['electric'] = electric.time;
                best['race'] = race;
            }
        });
}


setInterval(getBest, 5000);
getBest();