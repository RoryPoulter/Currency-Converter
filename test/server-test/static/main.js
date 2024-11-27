const ERROR_MESSAGES = {
    1: "Missing amount!",
    2: "Invalid amount: must be a number!",
    3: "Invalid amount: must be greater than 0!",
    4: "Converting to and from same currency!"
};


$(document).ready(function() {
    $('#form').on('submit',function(e){
        $.ajax({
        data : {
            start_currency : $('#start_currency').val(),
            final_currency : $('#final_currency').val(),
            amount : $('#amount').val()
        },
        type : 'POST',
        url : '/'
        })
        .done(function(data){
            if (data.output == null) {
                alert(ERROR_MESSAGES[data.error]);
            } else {
                $('#output').text(data.output).show();
            }
        });
        e.preventDefault();
    });
});