function updateElement(thisid, eid){
    /*
    Update an element based on a change on the calling elemrnt.
    */
    var old = ""
    var new = ""
    if(document.getElementById(eid)).val().trim().length > 0){
        oldClass = "hide"
        newClass = ""
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
    document.getElementById(eid).className = document.getElementById(eid).className.replace( /(?:^|\s)old(?!\S)/g , 'new' )
}
