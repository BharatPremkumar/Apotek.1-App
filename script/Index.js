const beholdNr = document.getElementById("beholdNr");
const plukkNr = document.getElementById("plukkNr");
const bane = document.getElementById("bane");
const error = document.getElementById("error");
const form = document.getElementById("myform");

// Add an event listener for the form submit
form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Date object
  const date = new Date();
  let currentDay = String(date.getDate()).padStart(2, "0");
  let currentMonth = String(date.getMonth() + 1).padStart(2, "0");
  let currentYear = date.getFullYear();
  // we will display the date as DD-MM-YYYY
  let currentDate = `${currentDay}-${currentMonth}-${currentYear}`;

  // Time object
  const hours = String(date.getHours()).padStart(2, "0");
  const minutes = String(date.getMinutes()).padStart(2, "0");
  const currentTime = `${hours}:${minutes}`;

  // Create a JavaScript object from the form data
  const data = {
    beholdNr: beholdNr.value,
    plukkNr: plukkNr.value,
    bane: bane.value,
    error: error.value,
    date: currentDate,
    time: currentTime,
  };

  // Make a POST request to the Python script's endpoint
  fetch("http://localhost:5000/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((result) => {
      console.log(result);
    })
    .catch((error) => {
      console.log("Error:", error);
    });
});
