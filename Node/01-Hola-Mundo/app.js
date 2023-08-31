// Las declaraciones var tienen un ámbito global o un ámbito función/local, mientras que let y const tienen un ámbito de bloque.
// Las variables var pueden ser modificadas y re-declaradas dentro de su ámbito; las variables let pueden ser modificadas, pero no re-declaradas; las variables const no pueden ser modificadas ni re-declaradas.
// Todas ellas se elevan a la parte superior de su ámbito. Pero mientras que las variables var se inicializan con undefined, let y const no se inicializan.
// Mientras que var y let pueden ser declaradas sin ser inicializadas, const debe ser inicializada durante la declaración.

let nombre="Ariel";
console.log(nombre);//ariel

nombre = "Juan";
console.log(nombre);//Juan

const nombre1 = 'CompuNerds';
console.log(nombre1);

const nombre2 = 'UTN FRSR';
console.log(nombre2);

console.log('Hola Mundo desde NODE');