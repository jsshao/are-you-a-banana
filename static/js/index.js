$(document).ready(function(){
    $("#uploader").change(function() {
        $("#path").val($("#uploader").val().split('\\').pop());
    });

    $("#browse").click(function(e) {
        $('input[type=file]').click();
    })

    $("#submitButton").click(function() {
        $('#submit').click();
    })
});
