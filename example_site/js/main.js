const date = new Date();
const dateString = `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()}`;
document.getElementById('date').innerText = dateString;