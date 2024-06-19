// Load the todo list from localStorage or initialize an empty array
let todoList = JSON.parse(localStorage.getItem('todoList')) || [];

function renderTodoList() {
  let todoListHTML = '';

  todoList.forEach((todoObject, index) => {
      const { name, dueDate } = todoObject;
      const html = `
        <div>${name}</div>
        <div>${dueDate}</div>
        <button class="delete-todo-button js-delete-todo-button">Delete</button>`;
      todoListHTML += html;
      });

  document.querySelector('.js-todo-list').innerHTML = todoListHTML;

  document.querySelectorAll('.js-delete-todo-button')
      .forEach((deleteButton, index) => {
        deleteButton.addEventListener('click', () => {
          todoList.splice(index, 1);
          saveAndRenderTodoList();
        })
      });
}

document.querySelector('.js-add-todo-button')
  .addEventListener('click', () => {
    addTodo();
  });

function addTodo() {
  const inputElement = document.querySelector('.js-name-input');
  let name = inputElement.value.trim();  // Use trim to remove extra whitespace

  if (!name) {
    name = 'no task selected';
  }

  const dateInputElement = document.querySelector('.js-due-date-input');
  const dueDate = dateInputElement.value.trim();  // Use trim to remove extra whitespace

  todoList.push({ name, dueDate });

  inputElement.value = '';
  dateInputElement.value = ''; // Clear the date input as well

  saveAndRenderTodoList();
}

function saveAndRenderTodoList() {
  localStorage.setItem('todoList', JSON.stringify(todoList));
  renderTodoList();
}


// Initial call to renderTodoList to display any pre-existing todos
saveAndRenderTodoList();
