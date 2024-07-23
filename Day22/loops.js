const array = [1, 2, 3, 4, 5];

// for loop
console.log("for loop:");
for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}

// while loop
console.log("while loop:");
let j = 0;
while (j < array.length) {
    console.log(array[j]);
    j++;
}

// do-while loop
console.log("do-while loop:");
let k = 0;
do {
    console.log(array[k]);
    k++;
} while (k < array.length);

// for...of loop
console.log("for...of loop:");
for (const value of array) {
    console.log(value);
}

// for...in loop (typically used for objects)
console.log("for...in loop:");
const obj = { a: 1, b: 2, c: 3 };
for (const key in obj) {
    console.log(`${key}: ${obj[key]}`);
}

// Array.prototype.forEach method
console.log("Array.prototype.forEach:");
array.forEach(value => {
    console.log(value);
});
