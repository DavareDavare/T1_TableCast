function textarealimit(textarea, rows, chars, rowsleft_id, charsleft_id) {
    var newValue;
    var valueSegments = textarea.value.split('\n');
    if(rows != undefined && valueSegments.length > rows) { // too many rows
        newValue = valueSegments.slice(0, rows).join("\n");
    }
    if(chars != undefined && textarea.value.length > chars) { // too many chars
        if(newValue != undefined) 
            newValue = newValue.substring(0, chars);
        else
            newValue = textarea.value.substring(0, chars);
    }
    if(newValue != undefined) textarea.value = newValue;

    if(rowsleft_id != undefined) {
        if(textarea.value == "") document.getElementById(rowsleft_id).innerHTML = rows;
        else if(rows - valueSegments.length >= 0) document.getElementById(rowsleft_id).innerHTML = rows - valueSegments.length;
    }
    if(charsleft_id != undefined) {
        if(chars != undefined) document.getElementById(charsleft_id).innerHTML = chars - textarea.value.length;
    }

    document.getElementById(fieldId).style.height = document.getElementById(fieldId).scrollHeight+'px';
    setHeight('Text');
}


function goPython(){
    $.ajax({
      url: "./main.py",
     context: document.body
    }).done(function() {
     alert('finished python script');;
    });
}