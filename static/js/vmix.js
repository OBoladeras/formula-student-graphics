function update() {
    setTimeout(() => {
        fetch('/api/select_team')
            .then(response => response.json())
            .then(data => {
                if (currentNum == data['number']) {
                    return;
                }
                currentNum = data['number'];

                update_current_team();
            });
        update();
    }, 1000);
}

update();


function update_current_team() {
    current_team_scrolling_image = document.getElementById('current_team_scrolling_image');
    current_team_object = document.getElementById('current_team_object');
    current_team_HideTeam();

    setTimeout(() => {
        if (current_team_scrolling_image.src != `/static/images/current_team/${data['number']}.png`) {
            current_team_scrolling_image.src = `/static/images/current_team/${data['number']}.png`;
        }
        current_team_ShowTeam();
    }, 1900);
}