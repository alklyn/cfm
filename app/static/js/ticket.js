function updateOpenDiv(thisid){
    /*
    Update the div containing the create_ticket button based on a change
    on the calling element.
    */
    var oldClass = "";
    var newClass = "";
    eid = "open_ticket_div";
    openBtn = document.getElementById(thisid)
    if(openBtn.value.length > 4){
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
