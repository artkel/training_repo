function addTask() {
    const taskInput = document.getElementById('taskInput');
    const taskList = document.getElementById('taskList');
    
    if (taskInput.value.trim() !== "") {
        const listItem = document.createElement('li');
        listItem.className = 'task-item'; // Apply the CSS class
        listItem.textContent = taskInput.value;
        
        const deleteButton = document.createElement('button');
        deleteButton.textContent = "Delete";
        deleteButton.onclick = function() {
            taskList.removeChild(listItem);
        };
        
        listItem.appendChild(deleteButton);
        taskList.appendChild(listItem);
        
        taskInput.value = "";  // Clear the input field
    }
}
