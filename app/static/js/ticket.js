function processInput(element){
    /*
    Performs various actions depending on the calling element
    -Enable location selector dependent on the calling selector.
    Or unhide/hide the submit button if the fields are all entered/ or any is
    unset.
    */
    console.log("Element calling processInput: ", element.id);

    switch(element.id){
        case "province":
        case "district":
        case "ward":
            element.form.submit();
            break;
        case "open_ticket":
            element.disabled = true;  //Prevent double subission
            element.form.submit();
            break;
        default:
            hideUnhideSubmit(element);
    }
}


function hideUnhideSubmit(item){
    /*
    Show the submit button only after all the fields have been filled
    */
    var oldClass = "";
    var newClass = "";
    var isCompleted = true;  //Is true when all the fields are completed
    eid = "open_ticket_div"

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
                minChars = 6;
                break;

            case "village":
            case "gender":
            case "partner":
            case "programme":
            case "topic":
            case "priority":
            case "agent":
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
    if (isCompleted){
        // alert('You typed ' + openBtn.value);
        thisForm.action = "save_ticket";
        oldClass = "hide";
        newClass = "show";
    }
    else {
        thisForm.action = "";
        oldClass = "show";
        newClass = "hide";
    }
    changeCSSClass(eid, oldClass, newClass);
}


function changeCSSClass(eid, oldClass, newClass){
    /*
    Purpose: Change or remove a class from an element
    eid: string: id of element
    old: string: old name of element
    new: string: new name of element
    */
    // alert("Old class = " + oldClass + ". New class = " + newClass);
    element = document.getElementById(eid);
    // alert("Class name = " + element.className);
    element.className = element.className.replace( oldClass, newClass );
}
