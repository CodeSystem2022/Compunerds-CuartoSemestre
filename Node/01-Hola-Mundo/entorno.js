
let nombre = process.env.NOMBRE || 'SIN NOMBRE'; //proceso + variable de entorno + nombre de la variable
let web = process.env.MI_WEB || 'NO TENGO WEB';

console.log('Hola ' + nombre);
console.log('Mi web es: ' + web);

