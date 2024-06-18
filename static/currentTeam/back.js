function searchTable() {
    var input = document.getElementById("searchInput");
    var filter = input.value.toLowerCase();

    var table = document.querySelector("table");
    var rows = table.getElementsByTagName("tr");

    for (var i = 0; i < rows.length; i++) {
        index = document.getElementById("columnSelect").selectedIndex;
        var nameColumn = rows[i].getElementsByTagName("td")[index + 1];

        if (nameColumn) {
            var name = nameColumn.textContent || nameColumn.innerText;
            if (name.toLowerCase().indexOf(filter) > -1) {
                rows[i].style.display = "";
            } else {
                rows[i].style.display = "none";
            }
        }
    }
}

function update() {
    var selectedTeam = document.querySelector('input[name="selectedTeam"]:checked');

    var dataa = selectedTeam.parentElement.parentElement;

    var number = dataa.children[1].innerText;
    var name = dataa.children[2].innerText;
    var uni = dataa.children[3].innerText;
    var flag = dataa.children[4].innerText;

    fetch('/api/currentteam', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            number: number,
            name: name,
            uni: uni,
            flag: flag
        })
    })
        .then(response => response.json())
        .then(data => {
            if (data.message == 'success') {
                window.location.reload();
            } else {
                alert(data.message);
            }
        })
        .catch(error => {
            alert('Error: ' + error);
        });
}