$("#dateSelect").datepicker();
const taskDivs = document.querySelectorAll(".task_txt_div");
const rightBarBG = document.querySelector(".RightBarBG");
var deleteForm = document.getElementById("delete-form");
var saveForm = document.getElementById("save-form");
let taskTitleTextarea = document.getElementById("Task-Title");
let taskDescriptionTextarea = document.getElementById("Task-Description");
let taskListSelect = document.getElementById("select-L");
let taskDueDateInput = document.getElementById("dateSelect");
let taskProgress = document.getElementById("select-P");
var DeleteBtn = document.getElementById("Delete-Btn");
var clicked = false;
let src = '';
if (window.location.pathname.includes("/index/todo_page/RecycleBin")){src = 'RecycleBin';}
else if (window.location.pathname.includes("/index/todo_page/Upcoming")){src = 'Upcoming';}


let upcoming_tasks = document.getElementsByClassName("Upcoming-Task")
let CheckBtns = document.querySelectorAll('.isDone-Icon');
  
  for (let btn of CheckBtns) {
    btn.addEventListener('click', function() {
      // Your event handling code goes here
        var taskId= btn.getAttribute("task_id"); 
        fetch(`${src}/checked/0/`.replace("0", parseInt(taskId)));
          window.location.assign(window.location.href);

  });
}











taskDivs.forEach(function (taskDiv) {
  taskDiv.addEventListener("click", async function () {
    if (!clicked) {
      clicked = true;
      document.querySelector(".RightBarBG").classList.toggle("show");
    }
    var taskId2= taskDiv.getAttribute("data-task-id"); 
    document.getElementById("RightBarContent").setAttribute("task-id", taskId2);



    if (src == 'RecycleBin'){
      DeleteBtn.style.backgroundColor="red";
    }
    else if ( src == 'Upcoming' || src == 'Today' ){

      document.getElementById("Save-Btn").addEventListener("click", function () {
        let updatedTaskData = {
          title: document.getElementById("Task-Title").value,
          description: document.getElementById("Task-Description").value,
          list: document.getElementById("select-L").value,
          due_date: document.getElementById("dateSelect").value,
          progress: document.getElementById("select-P").value,
        };
  
        // Extract the CSRF token from the form
        let csrfToken = document.querySelector(
          "[name=csrfmiddlewaretoken]"
        ).value;
  
        fetch(
          `/index/todo_page/save/0/${src}/`.replace("0",parseInt(taskId2)),
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": csrfToken, // Include the CSRF token in the headers
            },
            body: JSON.stringify(updatedTaskData),
          }
        )
          .then((response) => response.json())
          .then((data) => {
            console.log("Success:", data);
            // Redirect the user based on the source
            if (data.redirect_url) {
              window.location.href = data.redirect_url;
            }
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      });
    }
    else if (src == 'Today'){
      
    }
    else if (src == 'Calendar'){
      
    }


    let response = await fetch(`/index/todo_page/${src}/${taskId2}/`);
    var data = await response.json();
    // Update the content based on the fetched data
    taskTitleTextarea.value = data.title;
    taskDescriptionTextarea.value = data.description;
    taskListSelect.value = data.list;
    taskProgress.value = data.progress;
    taskDueDateInput.value = data.due_date;

    

    DeleteBtn.addEventListener("click", function () {
        fetch(`/index/todo_page/delete/${taskId2}/${src}/`);
        console.log("Deleted");
      });
      
  

  });
});