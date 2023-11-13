$("#dateSelect").datepicker();
const taskDivs = document.querySelectorAll(".task_txt_div");
const rightBarBG = document.querySelector(".RightBarBG");
var deleteForm = document.getElementById("delete-form");
var saveForm = document.getElementById("save-form");
let taskTitleTextarea = document.getElementById("Task-Title");
let taskDescriptionTextarea = document.getElementById("Task-Description");
let taskListSelect = document.getElementById("select-L");
let taskDueDateInput = document.getElementById("select-D");
let taskProgress = document.getElementById("select-P");
var clicked = false;

taskDivs.forEach(function (taskDiv) {
  taskDiv.addEventListener("click", async function () {
    if (!clicked) {
      clicked = true;
      document.querySelector(".RightBarBG").classList.toggle("show");
    }

    let taskId = taskDiv.getAttribute("data-task-id");

    let response = await fetch(`/index/todo_page/Upcoming/${taskId}/`);
    let data = await response.json();
    // Update the content based on the fetched data
    taskTitleTextarea.value = data.title;
    taskDescriptionTextarea.value = data.description;
    taskListSelect.value = data.list;
    taskProgress.value = data.progress;
    taskDueDateInput.value = data.due_date;
    document
      .getElementById("Delete-Btn")
      .addEventListener("click", function () {
        fetch(`/index/todo_page/delete/${taskId}/upcoming/`);
        console.log("Deleted");
      });
    document.getElementById("RightBarContent").setAttribute("task-id", taskId);

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
        '{% url "Save_Changes" 0 "upcoming" %}'.replace("0", parseInt(taskId)),
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
  });
});
