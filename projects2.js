document.getElementById('name').value = 'A&E';
document.getElementById('input').value = '2015';
document.getElementById('size').value = '720';
document.getElementById('architect').value = 'T Arquitectura ';
document.getElementById('location').value = 'CDMX';
document.getElementById('pm').value = '-';
var categoryLength = document.getElementById('category').options.length;
var elemCategory = document.getElementById('category');
var categories = ['entretenimiento', 'televisión'];
for(var i = 0; i < categoryLength; i++) {
elemCategory.options[i].selected = categories.indexOf(elemCategory.options[i].value) >= 0;
};
