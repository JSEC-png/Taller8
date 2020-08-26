$(document).ready(function () {
    $('#pass2').blur(function () { 
        if ($('#pass2').val() != $('#pass').val()){
            window.alert('Las constraseñas no coinciden, digite los dos ultimos campos nuevamente en orden y haga click sobre cualquier otro elemento')
            $('#btn').css('display','none');
        }
        else{
            $('#btn').css('display','block');
        }
        
    });

    console.log('Hola');

    $('#email').blur(function () { 
        
        if ( $('#email').val().match(/\.+[a-z]/) == null )
        {
            window.alert('El email debe contener .com,.es,.co, etc');
    
        }
    
    });

});