// const newTaskInput = document.getElementById('new-task');
//         const addTaskButton = document.getElementById('add-task');
//         const taskList = document.getElementById('task-list');

//         addTaskButton.addEventListener('click', () => {
//             const taskText = newTaskInput.value.trim();
//             if (taskText) {
//                 const taskItem = document.createElement('li');
//                 taskItem.className = 'task';
//                 taskItem.innerHTML = `
//                     <input type="checkbox" class="done">
//                     <span>${taskText}</span>
//                     <button class="delete-button">Delete</button>
//                 `;

//                 const doneCheckbox = taskItem.querySelector('.done');
//                 const deleteButton = taskItem.querySelector('.delete-button');

//                 doneCheckbox.addEventListener('change', () => {
//                     taskItem.classList.toggle('completed', doneCheckbox.checked);
//                 });

//                 deleteButton.addEventListener('click', () => {
//                     taskList.removeChild(taskItem);
//                 });

//                 taskList.appendChild(taskItem);
//                 newTaskInput.value = '';
//             }
//         });











// const newTaskInput = document.getElementById('new-task');
// const addTaskButton = document.getElementById('add-task');
// const todoForm = document.getElementById('todo-form');
// const dateCreatedInput = document.getElementById('date-created');
// const taskList = document.getElementById('task-list'); // Add this line to define taskList

// addTaskButton.addEventListener('click', (event) => {
//     event.preventDefault();  // Prevent the default form submission

//     const taskText = newTaskInput.value.trim();
//     const selectedDate = dateCreatedInput.value;

//     if (taskText && selectedDate) {
//         // Create a new task list item and add it to the task list (similar to your existing code)
//         const taskItem = document.createElement('li');
//         taskItem.className = 'task';
//         taskItem.innerHTML = `
//             <input type="checkbox" class="done">
//             <span>${taskText}</span>
//             <span class="task-date">${selectedDate}</span>  <!-- Display the selected date -->
//             <button class="delete-button">Delete</button>
//         `;

//         const doneCheckbox = taskItem.querySelector('.done');
//         const deleteButton = taskItem.querySelector('.delete-button');

//         doneCheckbox.addEventListener('change', () => {
//             taskItem.classList.toggle('completed', doneCheckbox.checked);
//         });

//         deleteButton.addEventListener('click', () => {
//             taskList.removeChild(taskItem);
//         });

//         taskList.appendChild(taskItem);
//         newTaskInput.value = '';
//         dateCreatedInput.value = ''; // Clear the date input

//         // Trigger the form submission
//         todoForm.submit();
//     }
// });

