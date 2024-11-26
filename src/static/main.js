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
        $('#output').text(data.output).show();
        });
        e.preventDefault();
    });
});