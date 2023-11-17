var categoryColors = {};
var elementsWithSameId = document.querySelectorAll('#List-Info');
  let ListIcons = document.querySelectorAll(".Lists-Icons") 
  for (let i = 0; i < ListIcons.length-1; i++) {
    var aElement = elementsWithSameId[i].querySelector('a');
    var textContent = aElement.textContent;
var computedStyle = window.getComputedStyle(ListIcons[i]);
var color = computedStyle.backgroundColor;
categoryColors[textContent]=color;
}

var tasks = document.querySelectorAll('.Upcoming-Task');

tasks.forEach(function(taskElement) {
var textContent2 = taskElement.querySelectorAll('.infoSup-txts')[1].textContent;
var iconElement = taskElement.querySelectorAll('.infoSup-Icons')[1];
var computedStyle2 = window.getComputedStyle(iconElement);
iconElement.style.backgroundColor = categoryColors[textContent2];
});
