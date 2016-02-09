$(document).ready(function(){
    $(window).bind('beforeunload', function(){
        alert();
        alert($('#test_img').src);
    });
});
