$(document).on('submit','#messageForm',function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/home/',
        data:{
            name:$('#nameInput').val(),
            email:$('#emailInput').val(),
            message:$('#messageInput').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            alert("created new message")
        }

    })
});