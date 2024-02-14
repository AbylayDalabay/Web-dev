let createNewTaskElement=function(taskString){
    let new_task = document.createElement("li");
    new_task.className = "task";

    let outer_label = document.createElement("label");
    outer_label.className = "task-new";

    let inner_span = document.createElement("span");

    let check_boxes = document.createElement("input");
    check_boxes.className = "checkboxes";

    let del_img = document.createElement("img");
    del_img.src = "https://img.icons8.com/plasticine/100/000000/filled-trash.png";
    del_img.className = "delete_img";
    del_img.onclick = deleteTask;


    inner_span.innerText = taskString;
    check_boxes.type = "checkbox";


    outer_label.appendChild(check_boxes);
    outer_label.appendChild(inner_span);
    new_task.appendChild(outer_label);
    new_task.appendChild(del_img);

    return new_task;
}


let addTask = function (){
    let incomplete_items = document.getElementById("myUL");

    let task_name = document.getElementById("input_form");

    if(task_name.value === ''){
        alert("Error!")
    }else{
        let listitem = createNewTaskElement(task_name.value);

        incomplete_items.appendChild(listitem);
    }

    task_name.value = "";

}

let deleteTask=function(){
    let listItem=this.parentNode;

    listItem.remove();
}