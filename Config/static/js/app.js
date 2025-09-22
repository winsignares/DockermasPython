function saludar() {
    let nombre = document.getElementById("nombre")
    let mensaje = nombre.value + " Hola mundo!";
    alertify.alert('Alert Title', mensaje, function(){ 
        alertify.success('Ok'); 
    });

}