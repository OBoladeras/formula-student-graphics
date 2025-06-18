function update() {
    setTimeout(() => {
        fetch('/api/vmix')
            .then(response => response.json())
            .then(data => {
                part1(data);


                part2(data);
            });

        update();
    }, 1000);

}

// Change current_team_number to the team number that is currently selected
function part1(data) {
    if (!(current_team_number == data['current_team_number'])) {
        // Current Team Graphic
        current_team_number = data['current_team_number'];
        current_team_scrolling_image = document.getElementById('current_team_scrolling_image');
        current_team_object = document.getElementById('current_team_object');

        if (graphics_status['current_team'] === true) {
            current_team_HideTeam();

            setTimeout(() => {
                if (current_team_scrolling_image.src != `/static/images/current_team/${current_team_number}.png`) {
                    current_team_scrolling_image.src = `/static/images/current_team/${current_team_number}.png`;
                }
                current_team_ShowTeam();
            }, 1900);
        }
        else {
            if (current_team_scrolling_image.src != `/static/images/current_team/${current_team_number}.png`) {
                current_team_scrolling_image.src = `/static/images/current_team/${current_team_number}.png`;
            }
        }
    }
    if (!(current_location == data['location'])) {
        current_location = data['location'];
        current_location_object = document.getElementById('location_object');
        
        if (graphics_status['location'] === true) {
            location_hide();

            setTimeout(() => {
                if (current_location_object.children[1].innerHTML != current_location) {
                    current_location_object.children[1].innerHTML = current_location;
                }
                location_show();
            }, 1900);
        }
        else if (current_location_object.children[1].innerHTML != current_location) {
            current_location_object.children[1].innerHTML = current_location;
        }
    }
}

// Hide or show the team graphic
function part2(data) {
    current_team_object = document.getElementById('current_team_object');
    location_object = document.getElementById('location_object');

    if (!(data['graphics_status']['current_team'] == graphics_status['current_team'])) {
        graphics_status['current_team'] = data['graphics_status']['current_team'];

        if (data['graphics_status']['current_team']) {
            current_team_object.style.display = 'flex';
            current_team_ShowTeam();
        } else {
            current_team_HideTeam();

            setTimeout(() => {
                current_team_object.style.display = 'none';
            }, 1900);
        }
    }

    if (!(data['graphics_status']['location'] == graphics_status['location'])) {
        graphics_status['location'] = data['graphics_status']['location'];

        if (data['graphics_status']['location']) {
            location_object.style.display = 'flex';
            location_show();
        } else {
            location_hide();

            setTimeout(() => {
                location_object.style.display = 'none';
            }, 1900);
        }
    }
}

update();