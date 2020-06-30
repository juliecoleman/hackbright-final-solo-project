"use strict";


function createAccount () {
    $('#create-account').show();
    $('#log-in').hide(); 
    $('#new-here').hide(); 
};

function showLogIn () {
    $('#create-account').hide();
    $('#log-in').show();
    $('#new-here').hide(); //Note this is not working!!
};


$('[data-toggle="tooltip"]').tooltip({html: true})

$('#password').password();
