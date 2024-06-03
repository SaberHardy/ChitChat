function toggleDropdown() {
    var dropdown = document.getElementById("dropdownMenu");
    console.log(dropdown);
    if (dropdown.style.display === "none" || dropdown.style.display === "") {
        dropdown.style.display = "block";
    } else {
        dropdown.style.display = "none";
    }
}

// Hide the dropdown menu when clicking outside of it
window.onclick = function(event) {
    if (!event.target.matches('.user-logo-img')) {
    console.log("tihi", event.target.matches('.user-logo-img'))
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.style.display === "block") {
                openDropdown.style.display = "none";
            }
        }
    }
}