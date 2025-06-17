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

function update_team() {
    fetch('/api/select_team', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ number: current_team_selected })

    }).then(response => {
        if (response.ok) {
            notification = document.getElementById("notification");
            notification.innerHTML = "Team updated successfully!";
            notification.style.display = "block";
            notification.classList.add("bg-green-500");
            notification.classList.remove("bg-red-500");

            setTimeout(() => {
                notification.style.display = "none";
            }, 3000);
        } else {
            notification = document.getElementById("notification");
            notification.innerHTML = "Failed to update team.";
            notification.style.display = "block";
            notification.classList.add("bg-red-500");
            notification.classList.remove("bg-green-500");

            setTimeout(() => {
                notification.style.display = "none";
            }, 3000);
        }
    }

    )
}