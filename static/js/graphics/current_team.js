function current_team_ShowTeam() {
    const endTransition = 1.9;
    const allObject = document.getElementById('current_team_object');
    allObject.classList.add('current_team_show');


    setTimeout(() => {
        red_top = document.getElementById('current_team_red_top');
        white_box = document.getElementById('current_team_white_box');
        container = document.getElementById('current_team_container');
        scrolling_container = document.getElementById('current_team_scrolling_container');

        red_top.style.scale = 1;
        white_box.style.width = '60px';
        container.style.transform = 'rotate(-90deg)';
        scrolling_container.style.width = '529px';
        allObject.style.transform = 'translateX(-65px)';

        allObject.classList.remove('current_team_show');

    }, endTransition * 1000);
}

function current_team_HideTeam() {
    const endTransition = 1.8;
    const allObject = document.getElementById('current_team_object');
    allObject.classList.add('current_team_hide');

    setTimeout(() => {
        red_top = document.getElementById('current_team_red_top');
        white_box = document.getElementById('current_team_white_box');
        container = document.getElementById('current_team_container');
        scrolling_container = document.getElementById('current_team_scrolling_container');

        red_top.style.scale = 0;
        white_box.style.width = '0px';
        container.style.transform = 'rotate(0deg)';
        scrolling_container.style.width = '0px';
        allObject.style.transform = 'translateX(0px)';

        allObject.classList.remove('current_team_hide');

    }, endTransition * 1000);
}