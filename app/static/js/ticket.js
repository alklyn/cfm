function processInput(element){
    /*
    Performs various actions depending on the calling element
    -Enable location selector dependent on the calling selector.
    Or unhide/hide the submit button if the fields are all entered/ or any is
    unset.

    element: Thre element that called this function.
    */
    console.log("Element calling processInput: ", element.id);

    switch(element.id){
        case "province":
        case "district":
        case "ward":
            element.form.submit();
            break;
        case "update_type":
            //Show or text area for ticket updates
            showHideTextArea(element, document.getElementById('update'));
            break;
        case "open_ticket":
        case "update_ticket":
            element.disabled = true;  //Prevent double subission
            element.form.submit();
            break;
        default:
            hideUnhideSubmit(element, "submit_div");
    }
}


function hideUnhideSubmit(item, eid){
    /*
    Show the submit button only after all the fields have been filled
    item: the element that called the function
    eid: id of submit button
    */
    var oldClass = document.getElementById(eid).className;
    var newClass = "";
    var isCompleted = true;  //Is true when all the fields are completed

    //testing
    var thisForm = item.form;

    var elements = document.querySelectorAll(".ticket_element")
    var minChars = 2;  //Minimum number of characters
    for (var i = 0; i < elements.length; i++){
        //Check that all the elements have been filled in
        currentID = elements[i].id;
        element = document.getElementById(currentID);
        switch (currentID) {
            case "caller_firstname":
            case "caller_lastname":
            case "village":
                minChars = 2;
                break;

            case "phone_number":
            case "update_details":
                minChars = 8;
                break;

            case "village":
            case "gender":
            case "partner":
            case "programme":
            case "topic":
            case "priority":
            case "agent":
            case "update_type":
                notVal = "0";
                break;

            default:
                //

        }
        var type = element.type.toLowerCase();
        if ((type == "text") || (type == "textarea")){ //Text
            isCompleted = (element.value.length >= minChars);
        }
        else {
            isCompleted = (element.value != notVal);
        }
        if(!isCompleted){
            break;
        }
    }
    console.log("Old class = ", oldClass);
    if (isCompleted){
        console.log("Form complete");
        thisForm.action = "save_ticket";
        newClass = "show";
    }
    else {
        console.log("Form not complete");
        thisForm.action = "";
        newClass = "hide";
    }
    changeCSSClass(eid, oldClass, newClass);
}


function showHideTextArea(element, target){
    /*
     Show the textArea for entering updates if an action
     "Update Ticket"/"Close Ticket" is chosen
    */
    var oldClass = target.className;
    var newClass = "";
    var pHolder = "";
    var updateArea = document.getElementById('update_details');
    var updateArea = document.getElementById('submit_div');
    console.log("Name  = ", updateArea.name)

    switch(element.value){
        case "1":
            pHolder = "Action taken";
            newClass = "show";
            updateArea.placeholder = pHolder;
            break;
        case "2":
            pHolder = "Solution";
            newClass = "show";
            updateArea.placeholder = pHolder;
            break;
        default:
            newClass = "hide";
    }
    console.log("Placeholder after = ", updateArea.placeholder)
    console.log(newClass, " the text area.");
    changeCSSClass(target.id, oldClass, newClass);
}

function changeCSSClass(eid, oldClass, newClass){
    /*
    Purpose: Change or remove a class from an element
    eid: string: id of element
    oldClass: string: old name of class
    newClass: string: new name of class
    */
    // alert("Old class = " + oldClass + ". New class = " + newClass);
    if(newClass != oldClass){
        element = document.getElementById(eid);
        // alert("Class name = " + element.className);
        element.className = element.className.replace( oldClass, newClass );
    }
}


function showHideUpdateButton(){
    /*
    Display the submit button on the "update_ticket" page only when all the
    fields in the form have been filled in.
    */
    var elements = document.querySelectorAll(".ticket_element")
}
