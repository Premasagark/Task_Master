function addTodo() {
  let todo = $("#todoInput").val();
  if (todo.trim() !== "") {
    $.ajax({
      type: "POST",
      url: "/store/save/to-do",
      data: { todo: todo },
      dataType: "JSON",
      success: function (response) {
        console.log(response);
        appendtodo(todo);
      },
    });
  }
}

function appendtodo(given_todo) {
  console.log(given_todo);
  let temp = `<div class="todo-msg"><span class="task">${given_todo}
    </span> <span class="remove" onclick="removeTodo(this, '${given_todo}')"> X </span></div>`;
  $("#todoList").append(temp);
}

function removeTodo(span, todo) {
  console.log(todo);
  $.ajax({
    type: "POST",
    url: "/store/rm/to-do",
    data: { todo: todo },
    dataType: "json",
    success: function (response) {
      window.location.reload();
      //   console.log(response);
      // var li = span.parentElement;
      // li.remove();
    },
  });
}

//task

function addTask() {
  let task = $("#taskInput").val();
  if (task.trim() !== "") {
    $.ajax({
      type: "POST",
      url: "/store/save/task",
      data: { task: task },
      dataType: "JSON",
      success: function (response) {
        console.log(response);
        appendtask(task);
      },
    });
  }
}

function appendtask(given_task) {
  console.log(given_task);
  let temp = `<div class="todo-msg"><span class="task">
  <p>${given_task}
  </p> <span class="remove-note" onclick="removeTask(this,'${given_task}')">Delete</span>`;
  $("#taskList").append(temp);
}

function removeTask(span, task) {
  console.log(task);
  $.ajax({
    type: "POST",
    url: "/store/rm/task",
    data: { task: task },
    dataType: "json",
    success: function (response) {
      window.location.reload();
      //   console.log(response);
      // var li = span.parentElement;
      // li.remove();
    },
  });
}

//taskP
function addTaskP() {
  let task = $("#taskInput").val();
  if (task.trim() !== "") {
    $.ajax({
      type: "POST",
      url: "/store/save/task",
      data: { task: task },
      dataType: "JSON",
      success: function (response) {
        console.log(response);
        appendtaskP(task);
      },
    });
  }
}

function appendtaskP(given_task) {
  console.log(given_task);
  let temp = `<div id="taskList">
  <div class="note">
      <p id="">${given_task}</p>
      <button class=" delete-btn" onclick="removeTask(this, '${given_task}')">×</button>
  </div>`;
  $("#taskList").append(temp);
}
