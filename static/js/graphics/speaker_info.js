function speaker_info_show(number) {
    const endTransition = 1.5;
    const allObject = document.getElementById('speaker_info_object' + number);
    allObject.classList.add('speaker_info_show');

    setTimeout(() => {
        allObject.children[0].style.width = '515px';
        allObject.children[1].style.height = '27px';

        allObject.classList.remove('speaker_info_show');
    }, endTransition * 1000);
}

function speaker_info_hide(number) {
    const endTransition = 1.5;
    const allObject = document.getElementById('speaker_info_object' + number);
    allObject.classList.add('speaker_info_hide');

    setTimeout(() => {
        allObject.children[0].style.width = '0px';
        allObject.children[1].style.height = '0px';

        allObject.classList.remove('speaker_info_hide');
    }, endTransition * 1000);
}