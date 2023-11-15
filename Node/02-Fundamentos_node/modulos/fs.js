//file system
const fs = require('fs');

//Primero leemos el archivo.txt
function leet(ruta, cb){
    fs.readFile(ruta, (err, data) => {
        cb(data.toString());
    })
}


//Segundo escribirmos el archivo1.txt creandolo
function escribir(ruta, contenido, cb){
    fs.writeFile(ruta, contenido, function (err){
        if(err){
            console.log('No se ha podido escribir', err);
        } else {
            console.log('Se ha escrito correctamente');
        }
    })
}

escribir(`${__dirname}/archivo1.txt`, 'Reescribimos el archivo' ,console.log);
// leet(`${__dirname}/archivo.txt`, console.log);


//Tecero eliminamos el archivo1.txt
function borrar(ruta, cb){
    fs.unlink(ruta, cb);
}

borrar(`${__dirname}/archivo1.txt`, console.log);