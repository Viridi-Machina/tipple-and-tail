const nameField = document.getElementById("id_booking_name");
const user_id = JSON.parse(document.getElementById('username').textContent);


console.log(user_id);
console.log(nameField);

nameField.setAttribute("value", user_id);