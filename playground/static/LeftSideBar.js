// Function to open the options frame
function openOptionsFrame() {
    document.getElementById('options-frame').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
  }

  // Function to close the options frame
  function closeOptionsFrame() {
    document.getElementById('options-frame').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
  }

  // Event listener to open the options frame when the trigger is clicked
  document.getElementById('options-trigger').addEventListener('click', openOptionsFrame);

  // Event listener to close the options frame when clicking away from it
  document.getElementById('overlay').addEventListener('click', closeOptionsFrame);

function AddNewList(inputText) {
  // Create elements
  var li = document.createElement("li");
  var a = document.createElement("a");
  var svg = document.createElement("svg");
  
  // Set attributes for SVG element
  svg.setAttribute('class', 'Lists-Icons');
  
  // Append elements to create the new list item
  a.appendChild(svg);
  a.appendChild(document.createTextNode(inputText));
  li.appendChild(a);
  li.setAttribute('class', 'li-elements');
  li.setAttribute('id', 'List-Info');

  // Get the parent ul element
  var listsUl = document.getElementById("Lists-List");

  // Get the reference element (AddNewList text field)
  var referenceElement = document.getElementById("List-Add");

  // Insert the new list item before the reference element
  listsUl.insertBefore(li, referenceElement);
}

function HandleKeyPress(event){
  
   // Check if the pressed key is Enter (key code 13)
    if (event.keyCode === 13) {
      var AddNewListValue = document.getElementById('AddNewList').value
      var Color = document.getElementById('colorPicker').value;
      // AddNewList(AddNewListValue);
      var encodedColor = encodeURIComponent(Color);
      fetch(`/index/todo_page/AddNewList/${AddNewListValue}/${encodedColor}/`).then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
      console.log("Refreshing...");
      location.reload();
    }
}  