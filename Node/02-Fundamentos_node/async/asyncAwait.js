async function hola(nombre){
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
            resolve();
            // reject('Hay un error...'); en caso de que haya un error
        }, 1000);
    });
};


// await hola('Lulu'); esta mal la sintaxis. 
// await solo es válido dentro de una función asincrona
async function main(){
    let nombre = await hola('Lulu');
    await hablar();
    await hablar();
    await hablar();
    await hablar();
    await adios(nombre);
    console.log('Terminamos el proceso...')
}


console.log('Empezamos el proceso...')
main();