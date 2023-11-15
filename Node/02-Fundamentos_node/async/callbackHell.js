function hola(nombre, miCallback){

    setTimeout(function() {
        console.log("Hola " + nombre);
        miCallback(nombre);
    }, 1000);
}

function hablar(callbackHablar){
    setTimeout(function(){
        console.log('bla bla bla bla');
        callbackHablar();
    }, 1000);
}

function adios(nombre, otroCallback) {
    setTimeout(function(){
        console.log("Adios " + nombre);
        otroCallback();
    }, 1500);
}

//función recursiva.
function conversacion(nombre, veces, callback){
    if(veces > 0){        
        hablar(function(){
            conversacion(nombre, --veces, callback);
        });
    } else {
        callback(nombre, callback);
    };
};




//--- PROCESO PRINCIPAL ---
console.log("Inicia proceso...");

// ↓ Esta opción no es eficiente ↓
// hola('Pepito', function(nombre) {
//     hablar(function(){
//         hablar(function(){
//             adios(nombre, function(){
//                 console.log("Termina el proceso...")            
//             });
//         });
//     });
// });

// Opción eficiente del código de arriba
hola('José', function(nombre){
    conversacion(nombre, 4, function(){
        console.log("Termina el proceso...")  
    }); 
});
