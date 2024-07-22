function sum(a,b,c){
    console.log(a,b,c);
    return a + b + c
}

a = 10;
b = 15;

ans = sum(a, b)
console.log(ans);

function multiply(num1, num2)
{
    return num1 * num2
}

// function yell(text)
// {
//     console.log(text.toUpperCase())
// }

// Alternative way of writing this is 
const yell = function (text){
    console.log(text.toUpperCase())
}
function longerthan(arr1, arr2)
{
    if(arr1.length > arr2.length)
    {
        console.log("arr1 is greater");
    }
    else
    {
        console.log("either both are equal or arr2 is longer");
    }
}

arr1 = [2,5,6,7];
arr2 = [4,5];

longerthan(arr1, arr2);
yell("akshat khatri");
console.log(multiply(9999,24834));


// Arrow functions

// let arrow = (arrowname)=>{
//     console.log(arrowname + "my name is arrow the great")
// }
// arrow("Arrowsssss")


// alternatively we can do something like this 

const divide = (num1,num2)=> num1 / num2;

const whisper = (text) => text.toLowerCase();

