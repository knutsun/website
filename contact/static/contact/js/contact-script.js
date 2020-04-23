function validation(){


    var subject = document.getElementById('subject').value;
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    var error_message = document.getElementById('error_message');
    var subject_error = document.getElementById('subject_error');
    var name_error = document.getElementById('name_error');
    var email_error = document.getElementById('email_error');
    var message_error = document.getElementById('message_error');
    var text;


    var bool = true;


    if(subject.length < 3){
        text = "Enter a valid subject";
        subject_error.innerHTML = text;
        subject_error.style.color = 'red';
        subject_error.style.fontSize = 'medium';


        bool = false;

    }

    else if(subject.length >= 3){
        text = "";
        subject_error.innerHTML = text;

    }

    if(name.length < 3){
        text = "Enter a valid name";
        name_error.innerHTML = text;
        name_error.style.color = 'red';
        name_error.style.fontSize = 'medium';

        bool = false;

    }
    else if(name.length >= 3){
        text = "";
        name_error.innerHTML = text;
    }


    if(email.length < 6){
        text = "Enter a valid email";
        email_error.innerHTML = text;
        email_error.style.color = 'red';
        email_error.style.fontSize = 'medium';


        bool = false;
    }

    else if(email.length > 5){
        text = "";
        email_error.innerHTML = text;
    }

    else if(message.length < 3){
        text = "Enter a valid name";
        message_error.innerHTML = text;
        message_error.style.color = 'red';
        message_error.style.fontSize = 'medium';


    }

    return bool;

}
