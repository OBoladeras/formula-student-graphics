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


document.querySelectorAll('.clickable-row').forEach(row => {
    row.addEventListener('click', function () {
        const radio = this.querySelector('input[type="radio"]');
        radio.checked = true;
        document.querySelectorAll('.clickable-row').forEach(r => r.classList.remove('bg-blue-100'));
        this.classList.add('bg-blue-100');

        current_team_selected = radio.value;

        // Update the graphic preview
        const current_team = document.getElementById('current_team');
        current_team.src = `/static/images/current_team/${current_team_selected}.png`;
    });
});

function toggleGraphic(graphic_name) {
    graphic_Visible = graphic_status[graphic_name];
    graphicVisible = !graphic_Visible;
    graphic_status[graphic_name] = graphicVisible;

    const button = document.getElementById("toggleGraphicButton_" + graphic_name);

    if (graphicVisible) {
        showGraphic(graphic_name);
        button.textContent = "Hide Graphic";
    } else {
        hideGraphic(graphic_name);
        button.textContent = "Show Graphic";
    }
}

function showGraphic(graphic_name) {
    graphic_status = document.getElementById(graphic_name + "_status");

    graphic_status.classList.remove("bg-red-100", "text-red-800");
    graphic_status.classList.add("bg-green-100", "text-green-800");
    text = graphic_status.querySelector("p");
    text.textContent = "Visualizer is active.";


    fetch(`/graphics_status/${graphic_name}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            show: true
        })
    })
}

function hideGraphic(graphic_name) {
    graphic_status = document.getElementById(graphic_name + "_status");
    graphic_status.classList.remove("bg-green-100", "text-green-800");
    graphic_status.classList.add("bg-red-100", "text-red-800");

    text = graphic_status.querySelector("p");
    text.textContent = "Visualizer is not active.";

    fetch(`/graphics_status/${graphic_name}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            show: false
        })
    })
}