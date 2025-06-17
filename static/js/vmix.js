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

function part1(data) {
    if (current_team_number == data['current_team_number']) {
        return;
    }
    current_team_number = data['current_team_number'];
    current_team_scrolling_image = document.getElementById('current_team_scrolling_image');
    current_team_object = document.getElementById('current_team_object');
    current_team_HideTeam();

    setTimeout(() => {
        if (current_team_scrolling_image.src != `/static/images/current_team/${current_team_number}.png`) {
            current_team_scrolling_image.src = `/static/images/current_team/${current_team_number}.png`;
        }
        current_team_ShowTeam();
    }, 1900);
}

function part2(data) {
    current_team_object = document.getElementById('current_team_object');

    if (data['graphics_status']['current_team'] == graphics_status['current_team']) {
        return;
    }
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


update();




/*

function update() {
    setTimeout(() => {
        fetch('/api/select_team')
            .then(response => response.json())
            .then(data => {
                if (currentNum == data['number']) {
                    return;
                }
                currentNum = data['number'];

                current_team_scrolling_image = document.getElementById('current_team_scrolling_image');
                current_team_object = document.getElementById('current_team_object');
                current_team_HideTeam();

                setTimeout(() => {
                    if (current_team_scrolling_image.src != `/static/images/current_team/${data['number']}.png`) {
                        current_team_scrolling_image.src = `/static/images/current_team/${data['number']}.png`;
                    }
                    current_team_ShowTeam();
                }, 1900);

            });

        fetch('/graphics_status/current_team')
            .then(response => response.json())
            .then(data => {
                current_team_object = document.getElementById('current_team_object');

                if (data['show'] == graphics_status['current_team']['show']) {
                    return;
                }
                graphics_status['current_team']['show'] = data['show'];

                if (data['show'] == true) {
                    current_team_object.style.display = 'flex';

                    current_team_ShowTeam();
                } else {
                    current_team_HideTeam();

                    setTimeout(() => {
                        current_team_object.style.display = 'none';
                    }, 1900);
                }
            });

        update();
    }, 1000);
}

graphics_status = {
    'current_team': {
        'show': true
    }
};

update();

*/