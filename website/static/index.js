$(function() {
    $('#sendBtn').bind('click', function() {
        var value = $('#msg').val();
        console.log(value);
        $.getJSON('/run', function(data) {
                //do nothing
                console.log("buna");
            });
        return false;
    });
});

function validate(name) {
    if(name.length >= 2) {
        return true;
    }
    return false;
}
