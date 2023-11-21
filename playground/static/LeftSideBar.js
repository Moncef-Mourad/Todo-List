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

  function AddNewList(inputText){

    

   var listsUl = document.getElementById("Lists-List");
   var li = document.createElement("li");
   var a = document.createElement("a");
   var svg = document.createElement("svg");
   svg.setAttribute('class','Lists-Icons');
   svg.setAttribute('style','background: #fff500;');
   a.appendChild(svg);
   a.appendChild(document.createTextNode(inputText));
    li.appendChild(a)
    li.setAttribute('class','li-elements');
    li.setAttribute('id','List-Info')
    listsUl.appendChild(li);

    var liListAdd = document.getElementById('List-Add');
    console.log(liListAdd);
    listsUl.lastChild = liListAdd;
    console.log(listsUl.lastChild);

  }


function HandleKeyPress(event){
   // Check if the pressed key is Enter (key code 13)
    if (event.keyCode === 13) {
      // Do something when Enter key is pressed
      alert('Enter key pressed!');
      AddNewList(document.getElementById('AddNewList').value)
      // You can replace the alert with your desired functionality
    }
}  