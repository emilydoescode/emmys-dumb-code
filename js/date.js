var today = new Date();

var day = today.getDay();
var month = today.getMonth();
var year = today.getFullYear();
var daylist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
var monthlist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

console.log("Today is: " + daylist[day] + ", " + day + " of " + monthlist[month] + ", " + year + ".");
