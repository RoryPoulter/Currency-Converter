const ERROR_MESSAGES = {
    1: "Converting to and from same currency!"
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
            if (data.error != null) {
                alert(ERROR_MESSAGES[data.error]);
            } else {
                $('#output').text(data.output).show();
                $('#start_to_final').text(data.start_to_final).show();
                $('#final_to_start').text(data.final_to_start).show();
            }
        });
        e.preventDefault();
    });
});