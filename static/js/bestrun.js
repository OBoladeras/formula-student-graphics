function newBest(type, data) {
    item = document.getElementById(type);

    item.children[0].style.width = '3.5rem';

    dataBlock = item.getElementsByClassName('run')[0];

    dataBlock.getElementsByClassName('time')[0].innerHTML = data.time;
    dataBlock.getElementsByClassName('number')[0].innerHTML = data.number;
    dataBlock.getElementsByClassName('uni')[0].innerHTML = data.uni;
    dataBlock.getElementsByClassName('name')[0].innerHTML = data.teamname;

    dataBlock.getElementsByClassName('time')[0].style.color = 'var(--best-time)';

    setTimeout(function () {
        item.children[0].style.width = '0px';
        dataBlock.getElementsByClassName('time')[0].style.color = '#fff';
    }, 5000);
}


data = {
    'time': '10:33.000',
    'number': '52',
    'uni': 'New Name Example',
    'teamname': 'New Team Example'
};

setTimeout(function () {
    newBest('hybrid', data);
}, 5000);
