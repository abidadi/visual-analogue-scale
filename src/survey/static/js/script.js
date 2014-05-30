$("form").submit(function(event) {
    // find all range inputs

    $('form input[type="range"]').each(function() {
        if(!($(this)[0].disabled) && ($(this)[0].value == 0)) { // if value is blank and input is not disabled, then form is invalid
            alert('Please evaluate or check "N/A" for all verbs. ' + $(this)[0].name + ' currently blank.');
            event.preventDefault();
            return false;
        }
    });
});
