
//come back in x year(s)
var current_year = new Date();
var current_year = current_year.getFullYear();

var username = prompt("Enter name: ");
var year_of_birth = prompt("Enter year of birth: ");
var age = current_year - year_of_birth;

if (age >= 18){
    window.alert("You are eligible, please apply.");
}else {
        var ok_year = 18 - age;
    window.alert("You are not eligible, come back in " + ok_year + " year(s)!");
}

/// Come back in year(x)
var current_year = new Date();
var current_year = current_year.getFullYear();

var username = prompt("Enter name: ");
var year_of_birth = prompt("Enter year of birth: ");
var age = current_year - year_of_birth;

if (age >= 18){
    window.alert("You are eligible, please apply.");
}else {
		var ok_year = 18 - age;
		var ok_year = current_year + ok_year;
    window.alert("You are not eligible, come back in " + ok_year +"!");
}