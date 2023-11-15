function hola(nombre){
    return new Promise(function(resolve, reject){
        setTimeout(function() {
            console.log("Hola " + nombre);
            resolve(nombre);
        }, 1000);
    });
};

function hablar(nombre){
    return new Promise((resolve, reject)=>{
        setTimeout(function(){
            console.log('bla bla bla bla');
            resolve(nombre);
        }, 1000);
    });
};

function adios(nombre) {
    return new Promise((resolve, reject) => {
        setTimeout(function(){
            console.log("Adios " + nombre);
            // resolve();
            reject('Hay un error...');
        }, 1000);
    });
};


//--- PROCESO PRINCIPAL ---
console.log('Iniciando el proceso....')
console.log(' ')
hola('Nana')
    .then(hablar)
    .then(hablar)
    .then(hablar)
    .then(adios)
    .then((nombre) => {        
        console.log(' ')
        console.log('Terminando el proceso....')
    })
    .catch(error => {
        console.log('Ha habido un error en: ');
        console.log(error);
    });