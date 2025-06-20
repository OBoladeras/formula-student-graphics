function location_show() {
    const endTransition = 1.5;
    const allObject = document.getElementById('location_object');
    allObject.classList.add('location_show');

    const audio = new Audio('/static/audios/location.mp3');
    audio.volume = 0.5;
    audio.currentTime = 0;
    audio.play();

    setTimeout(() => {
        audio.currentTime = 0;
        audio.play();
    }, 800);

    setTimeout(() => {
        allObject.children[0].style.width = '113px';
        allObject.children[0].style.height = '42px';
        allObject.children[0].style.transform = 'translate(0, 0)';
        allObject.children[0].style.borderRight = '4px solid white';

        allObject.children[1].style.width = '395.625px';
        allObject.children[1].style.padding = '0 70px 0 15px';

        allObject.classList.remove('location_show');
    }, endTransition * 1000);
}

function location_hide() {
    const endTransition = 1.5;
    const allObject = document.getElementById('location_object');
    allObject.classList.add('location_hide');

    const audio = new Audio('/static/audios/location.mp3');
    audio.playbackRate = 0.5;
    audio.play();

    setTimeout(() => {
        allObject.children[0].style.width = '0';
        allObject.children[0].style.height = '0';
        allObject.children[0].style.transform = 'translate(0, 0)';
        allObject.children[0].style.borderRight = '0';

        allObject.children[1].style.width = '0';
        allObject.children[1].style.padding = '0';

        allObject.classList.remove('location_hide');
    }, endTransition * 1000);
}