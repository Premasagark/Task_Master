// //to-do-list

function addTask() {
  var input = document.getElementById("taskInput");
  var task = input.value;
  if (task.trim() !== "") {
    var ul = document.getElementById("taskList");
    var li = document.createElement("li");
    li.innerHTML =
      '<span class="task">' +
      task +
      '</span> <span class="remove" onclick="removeTask(this)">X</span>';
    ul.appendChild(li);
    input.value = "";
    saveTasks();
  } else {
    alert("Please enter a task.");
  }
}

function removeTask(span) {
  var li = span.parentElement;
  li.remove();
  saveTasks();
}

function saveTasks() {
  var tasks = [];
  var lis = document.getElementById("taskList").getElementsByTagName("li");
  for (var i = 0; i < lis.length; i++) {
    tasks.push({
      task: lis[i].querySelector(".task").textContent,
      checked: lis[i].classList.contains("check"),
    });
  }
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
  var tasks = JSON.parse(localStorage.getItem("tasks")) || [];
  var ul = document.getElementById("taskList");
  tasks.forEach(function (taskObj) {
    var li = document.createElement("li");
    li.innerHTML =
      '<span class="task' +
      (taskObj.checked ? " check" : "") +
      '" onclick="toggleCheck(this)">' +
      taskObj.task +
      '</span> <span class="remove" onclick="removeTask(this)">            X</span>';
    ul.appendChild(li);
  });
}

function toggleCheck(span) {
  span.classList.toggle("check");
  saveTasks();
}

loadTasks();

// notes-section

function addNote() {
  var textarea = document.getElementById("noteInput");
  var note = textarea.value;
  if (note.trim() !== "") {
    var noteList = document.getElementById("noteList");
    var div = document.createElement("div");
    div.className = "note";
    div.innerHTML =
      "<p>" +
      note +
      '</p> <span class="remove-note" onclick="removeNote(this)">Delete</span>';
    noteList.appendChild(div);
    textarea.value = "";
    saveNotes();
  } else {
    alert("Please enter a note.");
  }
}

function removeNote(span) {
  var noteDiv = span.parentElement;
  noteDiv.remove();
  saveNotes();
}

function saveNotes() {
  var notes = [];
  var noteDivs = document
    .getElementById("noteList")
    .getElementsByClassName("note");
  for (var i = 0; i < noteDivs.length; i++) {
    notes.push(noteDivs[i].querySelector("p").textContent);
  }
  localStorage.setItem("notes", JSON.stringify(notes));
}

function loadNotes() {
  var notes = JSON.parse(localStorage.getItem("notes")) || [];
  var noteList = document.getElementById("noteList");
  notes.forEach(function (note) {
    var div = document.createElement("div");
    div.className = "note";
    div.innerHTML =
      "<p>" +
      note +
      '</p> <span class="remove-note" onclick="removeNote(this)">Delete</span>';
    noteList.appendChild(div);
  });
}

loadNotes();
