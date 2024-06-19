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
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.style.display === "block") {
                openDropdown.style.display = "none";
            }
        }
    }
}

// ---------------- Functions for handling messages --------------
document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelector('.send-message').addEventListener('click', function() {
        let sender_id = document.getElementById('sender_id').value;
        let receiver_id = document.getElementById('receiver_id').value;
        let message_content = document.querySelector('.input-message').value;

        send_name(sender_id, receiver_id, message_content);
    });
});

function send_message(sender_id, receiver_id, message_content) {
    let message_to_send = {
        sender_id: sender_id,
        receiver_id: receiver_id,
        message_content: message_content
    };
    console.log(message_to_send);
    console.log(JSON.stringify(message_to_send));

    $.ajax({
        url: "/messages",
        type: 'POST',
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(message_to_send)
    }).done(function () {
        console.log("Message sent");
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log("Error: " + textStatus + " - " + errorThrown);
    });
    console.log("was sent");
}
// ----------- Load chat for users ------------------
function loadChat(sender_id, receiver_id) {
    $.ajax({
        url: `/get_messages_between_users/${sender_id}/${receiver_id}`,
        type: 'GET',
        success: function(response) {
            $('#chat-container').html(response);
            $('#receiver_id').val(receiver_id);
            $('.input-send-btn').show();
        },
        error: function(error) {
            console.error("Error loading chat:", error);
        }
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelector('.send-message').addEventListener('click', function() {
        let sender_id = document.getElementById('sender_id').value;
        let receiver_id = document.getElementById('receiver_id').value;
        let message_content = document.querySelector('.input-message').value;

        document.querySelector('.input-message').value = "";

        send_message(sender_id, receiver_id, message_content);
    });
});