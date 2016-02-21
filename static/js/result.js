$(document).ready(function(){
  console.log($('img')[0].id);
});

$(window).on('beforeunload', function() {
  var images = $('img');
  for (var i = 0; i < images.length; i++)
    $.ajax({
      url: "/delete/" + images[i].id,
      type: 'POST'
    });
});
