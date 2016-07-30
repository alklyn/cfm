function hideUnhideSubmit(thisId, thisForm){
    /*
    Show the submit button only after all the fields have been filled
    */
    var oldClass = "";
    var newClass = "";
    var isFilled = true;
    eid = "open_ticket_div"

    var elements = document.querySelectorAll(".ticket_element")
    var minChars = 2;  //Minimum number of characters
    for (var i = 0; i < elements.length; i++){
        //Check that all the elements have been filled in
        currentID = elements[i].id;
        element = document.getElementById(currentID);
        switch (currentID) {
            case "caller_firstname":
            case "caller_lastname":
                minChars = 2;
                break;

            case "phone_number":
                minChars = 6;
                break;

            case "province":
            case "district":
            case "ward":
                notVal = "0";
                thisForm.submit();
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
            isFilled = (element.value.length >= minChars);
        }
        else {
            isFilled = (element.value != notVal);
        }
        if(!isFilled){
            break;
        }
    }
    if (isFilled){
        // alert('You typed ' + openBtn.value);
        oldClass = "hide";
        newClass = "show";
    }
    else {
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
