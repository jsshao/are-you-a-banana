$(document).ready(function(){
    $("#uploader").change(function(e) {
        var files = e.target.files;
        var list = "";
        for (var i = 0; i < files.length; i++) {
          list += files[i].name + ", "
        }
        $("#path").val(list);
    });

    $("#browse").click(function(e) {
        $('input[type=file]').click();
    })

    $("#submitButton").click(function() {
        $('#submit').click();
    })
});
