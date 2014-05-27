$("form").submit(function(event) {
    // find all range inputs

    $('form input[type="range"]').each(function() {
        if($this.value === 0 && !$this.disabled) { // if value is blank and input is not disabled, then form is invalid
            alert('form not submitted!' + $this + 'is blank');
            event.preventDefault();
        }
    });

});
