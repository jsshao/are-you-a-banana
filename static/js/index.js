$(document).ready(function(){
    + function($) {
        'use strict';

        // UPLOAD CLASS DEFINITION
        // ======================

        var dropZone = document.getElementById('drop-zone');
        var uploadForm = document.getElementById('uploadForm');

        var startUpload = function(files) {
            console.log(files)
            var formData = new FormData();
            for (var i = 0; i < files.length; i++) {
              formData.append('input-img', files[i]);
            }

            // now post a new XHR request
            var xhr = new XMLHttpRequest();
            xhr.open('POST', 'upload');
            xhr.onload = function () {
              if (xhr.status === 200) {
                console.log('all done: ' + xhr.status);
                console.log(xhr);
                $('#htmlInput').val(JSON.stringify(xhr.response));
                $('#fakeForm').submit();
              } else {
                console.log('Something went terribly wrong...');
              }
            };

            xhr.send(formData);
        }

        uploadForm.addEventListener('submit', function(e) {
            var uploadFiles = document.getElementById('uploader').files;
            e.preventDefault()
            startUpload(uploadFiles)
        })

        dropZone.ondrop = function(e) {
            e.preventDefault();
            this.className = 'upload-drop-zone';

            startUpload(e.dataTransfer.files)
        }

        dropZone.ondragover = function() {
            this.className = 'upload-drop-zone drop';
            return false;
        }

        dropZone.ondragleave = function() {
            this.className = 'upload-drop-zone';
            return false;
        }

    }(jQuery);

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
