// // // // #### 2022-07-21

// // //// ######### Functions

// // //// Defining a functions

// // const square = function(x) {
// //     return x * x;
// // };

// // console.log(square(12)); // 144

// // console.log();

// // const makeNoise = function() {
// //     console.log("Pling!");
// // };

// // makeNoise(); // Pling!

// // console.log();

// // const power = function(base, exponent) {
// //     let result = 1;
// //     for(let count = 0; count < exponent; count++) {
// //         result *= base;
// //     }

// //     return result;
// // };

// // console.log(power(2, 10)); // 1024

// // console.log();

// // //// Bindings and Scopes

// // // Note: pre-2015 JS var keyword is visibile throughout 
// // // the whole function that they appear or 
// // // throughout the global scope.

// // let x = 10;
// // if(true) {
// //     let y = 20;
// //     var z = 30;

// //     console.log(x + y + z); // 60
// // }

// // // y is not visible here
// // console.log(x + z); // 40

// // console.log();

// // // bindings with same name
// // const halve = function(n) {
// //     return n / 2;
// // };

// // let n = 10;
// // console.log(halve(100)); // 50
// // console.log(n); // 10

// // console.log();

// // //// Nested Scope
// // const hummus = function(factor) {
// //     const ingredient = function(amount, unit, name) {
// //         let ingredientAmount = amount * factor;
// //         if(ingredientAmount > 1) {
// //             unit += "s";
// //         }

// //         console.log(`${ingredientAmount} ${unit} ${name}`); // or
// //         // console.log(ingredientAmount + " " + unit + " " + name); 
// //     };

// //     ingredient(1, "can", "chickpeas");
// //     ingredient(0.25, "cup", "tahini");
// //     ingredient(0.25, "cup", "lemon juice");
// //     ingredient(1, "clove", "garlic");
// //     ingredient(2, "tablespoon", "olive oil");
// //     ingredient(0.5, "teaspoon", "cumin");
// // };

// // console.log(hummus(13));

// // console.log();

// // // // #### 2022-07-23

// // //// Functions as Values

// // // let launchMissiles = function() {
// // //     missileSystem.launch("now");
// // // };

// // // if(safeMode) {
// // //     launchMissiles = function() {/* do nothing */}
// // // }



// // //// Declaration of Notation

// // function squareNotation(x) {
// //     return x * x;
// // }

// // console.log(squareNotation(13)); // 169

// // console.log();

// // console.log("The future says:", future());

// // function future() {
// //     return "You'll never have flying cars";
// // }

// // console.log();

// // //// Arrow functions

// // const powerArrow = (base, exponent) => {
// //     let result = 1;
// //     for(let count = 0; count < exponent; count++) {
// //         result *= base;
// //     }

// //     return result;
// // };

// // console.log(powerArrow(2, 8)); // 256

// // console.log();

// // // if there is only one parameter name, omit the parenthesis around the parameter list.

// // const square1 = (x) => { return x * x };
// // const square2 = x => x * x;

// // console.log(square1(3));
// // console.log(square2(4));

// // console.log();

// // // if arrow function has no parameters at all
// // const horn = () => {
// //     console.log("Toot");
// // };

// // horn();

// // console.log();

// // // // #### 2022-07-24

// // //// The Call Stack

// // function greet(who) {
// //     console.log("Hello " +  who);
// // }
// // greet("Harry");
// // console.log("Bye");

// // // // schematic flow of control

// // // not in function
// // //     in greet
// // //         in console.log
// // //     in greet
// // // not in function
// // //     in console.log
// // // not in function

// // console.log();

// // function chicken() {
// //     return egg();
// // }

// // function egg() {
// //     return chicken();
// // }

// // // console.log(chicken() + " came first"); // Uncaught RangeError: Maximum stack size exceeded


// // console.log();

// // //// Optional Arguements

// // function squareOptional(x) {
// //     return x * x;
// // }

// // console.log(squareOptional(4, true, "hedgehog")); 
// // // ignores extra argument based on the given parameters of the function

// // console.log();

// // function minus(a, b) {
// //     // if(b === undefined) {
// //     //     return -a;
// //     // } else {
// //     //     return a - b;
// //     // }
    
// //     // shorthand
// //     if(b === undefined) return -a;
// //     else return a - b;
// // }

// // console.log(minus(10)); // -10
// // console.log(minus(10, 5)); // 5

// // console.log();

// // function powerOptional(base, exponent = 2) {
// //     let result = 1;
// //     let count = 0;
// //     while(count < exponent) {
// //         result *= base;
// //         count++;
// //     }

// //     return result;
// // }

// // console.log(powerOptional(4)); // 16
// // console.log(power(2, 6)); // 64

// // console.log();

// // console.log("C", "O", 2); // Rest parameters on page 74

// // console.log();

// // //// Closure

// // function wrapValue(n) {
// //     let local = n;
// //     return() => local;
// // }

// // let wrap1 = wrapValue(1);
// // let wrap2 = wrapValue(2);

// // console.log(wrap1()); // 1
// // console.log(wrap2()); // 2

// // console.log();

// // function multiplier(factor) {
// //     return number => number * factor;
// // }

// // let twice = multiplier(2);
// // console.log(twice(5)); // 10;


// // // // #### 2022-07-26

// //// Recursion

// function powerRecursion(base, exponent) {
//     if(exponent == 0) {
//         return 1;
//     } else {
//         return base * powerRecursion(base, exponent - 1);
//     }
// }

// console.log(powerRecursion(2, 3)); // 8

// // if exponent == 0
// console.log(powerRecursion(2, 0)); // 1

// console.log();

// function findSolution(target) {
//     function find(current, history) {
//         if(current == target) {
//             return history;
//         } else if(current > target) {
//             return null;
//         } else {
//             // template literal solution
//             return find(current + 5, `(${history} + 5)`) ||
//                     find(current * 3, `(${history} * 3)`);

//             // // non-template literal
//             // return find(current + 5, "(" + history + " + 5)") ||
//             //         find(current * 3, "(" + history + " * 3)");
//         }
//     }
//     return find(1, "1");
// }


// console.log(findSolution(24)); // (((1 * 3) + 5) * 3)


// // // emphasis
// // find(1, "1")
// //     find(6, "(1 + 5)")
// //         find(11, "((1 + 5) + 5)")
// //             find(16, "(((1 + 5) + 5) + 5)")
// //             too big
// //             find(33, "(((1 + 5) + 5) * 3)")
// //             too big
// //         find(18, "((1 + 5) * 3)")
// //         too big
// //     find(3, "(1 * 3)")
// //     find(8, "((1 * 3) + 5)")
// //         find(13, "(((1 * 3) + 5) + 5)")
// //         found!

// // if start === target

// // return history //(to findSolution. let's call it "H")
// // return H to console.log() // prints 1
// // else if start > target

// // return null //(to findSolution, let's call it N)
// // return N to console.log() // prints null
// // otherwise if start is lesser than target, return A || B

// // A = find(start + 5, "(" + history + " + 5)")
// // B = find (start * 3, "(" + history + " * 3)")
// // meaning return A if A is truthy otherwise return B; A or B are evaluated before the function returns.

// // let's go through it step by step :

// // find will be invoked again and again with start parameter incremented by 5 ie :

// // return find(1, "1")    //  start = 1,   history = "(1 + 5)"    
// // return find(6, history)   //   start = 6,   history = "(1 + 5 ) + 5"   
// // return find(11, history)    //  start = 11,   history = "(1 + 5) + 5 ) + 5"   
// // return find(16, history)    //  start = 16,   history = "(1 + 5) + 5 ) + 5 ) + 5"   
// // return find(21, history) start = 21,   history = "(1 + 5) + 5 ) + 5 ) + 5 ) + 5"   
// // now the next value will be 26. since 26 > 22, "find" will return B instead

// // return find(63, history) start = 21 * 3 =  63,      
// // //since 63 > 24,  "null" is returned where start = 16,    
// // start is 16 and not 63 because it is a parameter. It is not changed and knows nothing about the incrementation 
// // by 5 that occurred during the invocation.

// // find(21*3, history) , 48 > 24 so return null where start = 11
// // find(11 *3, history) , 33 > 24 so return null where start = 6
// // find(6*3, history) , start = 18 and 18 < 24 so A will be truthy start will be incremented by 5
// // return find( 18 + 5, history)
// // return find (23 + 5, history) 28 > 24, A is null, B is evaluated

// // ... and so on and so on until start is equal 24


// // // // #### 2022-07-29

// //// Growing Functions

// function printFarmInventory(cows, chickens) {
//     let cowString = String(cows);
    
//     while(cowString.length < 3) {
//         cowString = "0" + cowString;
//     }
//     console.log(`${cowString} Cows`);

//     let chickenString = String(chickens);

//     while(chickenString.length < 3) {
//         chickenString = "0" + chickenString;
//     }
//     console.log(`${chickenString} Chickens`)
// }

// printFarmInventory(7, 11);

// console.log();

// function printZeroPaddedWithLabel(number, label) {
//     let numberString = String(number);

//     while(numberString.length < 3) {
//         numberString = "0" + numberString;
//     }
//     console.log(`${numberString} ${label}`);
// }

// function printFarmInventory2(cows, chickens, pigs) {
//     printZeroPaddedWithLabel(cows, "Cows");
//     printZeroPaddedWithLabel(chickens, "Chickens");
//     printZeroPaddedWithLabel(pigs, "Pigs");
// }

// printFarmInventory2(7, 11, 3);

// console.log();

// function zeroPad(number, width) {
//     let string = String(number);
    
//     while(string.length < width) {
//         string = "0" + string;
//     }

//     return string;
// }

// function printFarmInventory2(cows, chickens, pigs) {
//     console.log(`${zeroPad(cows, 3)} Cows`);
//     console.log(`${zeroPad(chickens, 3)} Chickens`);
//     console.log(`${zeroPad(pigs, 3)} Pigs`);
// }

// printFarmInventory2(7, 16, 3);

// console.log();

// //// Functions and Side Effects
// // View Eloquent Javascript Page 94


// //// Summary

// // Define f to hold a function value
// const f = function(a) {
//     console.log(a + 2);
// };

// // Declare g to be a function
// function g(a, b) {
//     return a * b * 3.5;
// }

// // A less verbos function value
// let h = a => a % 3


// ////// #######################################
// ////// #### EXERCISE
// ////// #######################################


//// ###### Minimum

// Chapter 2 introduced the standard function Math.min, which returns its
// smallest argument (see “Return Values” on page 27). We can build
// something like that now. Write a function min that takes two arguments
// and returns their minimum.

function minValue(val1, val2) {
    return Math.min(val1, val2);
}

console.log(minValue(233, 1 + 33 * 2)); // 67

console.log();


//// ###### Recursion

// We’ve seen that % (the remainder operator) can be used to test whether
// a number is even or odd by using % 2 to see whether it’s divisible by two.
// Here’s another way to define whether a positive whole number is even
// or odd:
// Zero is even.
// One is odd.
// For any other number N, its evenness is the same as N –2.
// Define a recursive function isEven corresponding to this description.
// The function should accept a single parameter (a positive, whole
// number) and return a Boolean.
// Test it on 50 and 75. See how it behaves on –1. Why? Can you think
// of a way to fix this?

function isEven(n) {
    if(n === 0) {
        return true;
    } else if(n === 1) {
        return false;
    } else if(n < 0) {
        return isEven(-n);
    } else {
        return isEven(n - 2);
    }
}

console.log(isEven(50));
console.log(isEven(75));
console.log(isEven(-1));


console.log();



//// ###### Bean Counting

// You can get the Nth character, or letter, from a string by writing
// "string"[N]. The returned value will be a string containing only one
// character (for example, "b"). The first character has position 0, which
// causes the last one to be found at position string.length - 1. In other
// words, a two-character string has length 2, and its characters have
// positions 0 and 1.
// Write a function countBs that takes a string as its only argument and
// returns a number that indicates how many uppercase “B” characters
// there are in the string.
// Next, write a function called countChar that behaves like countBs,
// except it takes a second argument that indicates the character that is to
// be counted (rather than counting only uppercase “B” characters).
// Rewrite countBs to make use of this new function.

function countChar(string, ch) {
    let counted = 0;
    let i = 0;
    do {
        if(string[i] == ch) {
            counted += 1;
        }
        i++;

    } while(i < string.length);
    return counted;
}

function countBs(string) {
    return countChar(string, "B");
}

console.log(countBs("BBC")); // 2
console.log(countChar("kakkerlak", "k")); // 4

