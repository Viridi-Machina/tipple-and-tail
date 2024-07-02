// django route for javascript to parse logged-in username from project
const user_id = JSON.parse(document.getElementById('username').textContent);

// Query constants
const nameField = document.getElementById("id_booking_name");
const allergyLabel = document.getElementById("id_allergies");

nameField.setAttribute("value", user_id);
