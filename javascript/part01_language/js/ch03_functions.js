// // // #### 2022-07-21

// //// ######### Functions

// //// Defining a functions

// const square = function(x) {
//     return x * x;
// };

// console.log(square(12)); // 144

// console.log();

// const makeNoise = function() {
//     console.log("Pling!");
// };

// makeNoise(); // Pling!

// console.log();

// const power = function(base, exponent) {
//     let result = 1;
//     for(let count = 0; count < exponent; count++) {
//         result *= base;
//     }

//     return result;
// };

// console.log(power(2, 10)); // 1024

// console.log();

// //// Bindings and Scopes

// // Note: pre-2015 JS var keyword is visibile throughout 
// // the whole function that they appear or 
// // throughout the global scope.

// let x = 10;
// if(true) {
//     let y = 20;
//     var z = 30;

//     console.log(x + y + z); // 60
// }

// // y is not visible here
// console.log(x + z); // 40

// console.log();

// // bindings with same name
// const halve = function(n) {
//     return n / 2;
// };

// let n = 10;
// console.log(halve(100)); // 50
// console.log(n); // 10

// console.log();

// //// Nested Scope
// const hummus = function(factor) {
//     const ingredient = function(amount, unit, name) {
//         let ingredientAmount = amount * factor;
//         if(ingredientAmount > 1) {
//             unit += "s";
//         }

//         console.log(`${ingredientAmount} ${unit} ${name}`); // or
//         // console.log(ingredientAmount + " " + unit + " " + name); 
//     };

//     ingredient(1, "can", "chickpeas");
//     ingredient(0.25, "cup", "tahini");
//     ingredient(0.25, "cup", "lemon juice");
//     ingredient(1, "clove", "garlic");
//     ingredient(2, "tablespoon", "olive oil");
//     ingredient(0.5, "teaspoon", "cumin");
// };

// console.log(hummus(13));

// console.log();

// // // #### 2022-07-23

// //// Functions as Values

// // let launchMissiles = function() {
// //     missileSystem.launch("now");
// // };

// // if(safeMode) {
// //     launchMissiles = function() {/* do nothing */}
// // }



// //// Declaration of Notation

// function squareNotation(x) {
//     return x * x;
// }

// console.log(squareNotation(13)); // 169

// console.log();

// console.log("The future says:", future());

// function future() {
//     return "You'll never have flying cars";
// }

// console.log();

// //// Arrow functions

// const powerArrow = (base, exponent) => {
//     let result = 1;
//     for(let count = 0; count < exponent; count++) {
//         result *= base;
//     }

//     return result;
// };

// console.log(powerArrow(2, 8)); // 256

// console.log();

// // if there is only one parameter name, omit the parenthesis around the parameter list.

// const square1 = (x) => { return x * x };
// const square2 = x => x * x;

// console.log(square1(3));
// console.log(square2(4));

// console.log();

// // if arrow function has no parameters at all
// const horn = () => {
//     console.log("Toot");
// };

// horn();

// console.log();

// // // #### 2022-07-24

// //// The Call Stack

// function greet(who) {
//     console.log("Hello " +  who);
// }
// greet("Harry");
// console.log("Bye");

// // // schematic flow of control

// // not in function
// //     in greet
// //         in console.log
// //     in greet
// // not in function
// //     in console.log
// // not in function

// console.log();

// function chicken() {
//     return egg();
// }

// function egg() {
//     return chicken();
// }

// // console.log(chicken() + " came first"); // Uncaught RangeError: Maximum stack size exceeded


// console.log();

// //// Optional Arguements

// function squareOptional(x) {
//     return x * x;
// }

// console.log(squareOptional(4, true, "hedgehog")); 
// // ignores extra argument based on the given parameters of the function

// console.log();

// function minus(a, b) {
//     // if(b === undefined) {
//     //     return -a;
//     // } else {
//     //     return a - b;
//     // }
    
//     // shorthand
//     if(b === undefined) return -a;
//     else return a - b;
// }

// console.log(minus(10)); // -10
// console.log(minus(10, 5)); // 5

// console.log();

// function powerOptional(base, exponent = 2) {
//     let result = 1;
//     let count = 0;
//     while(count < exponent) {
//         result *= base;
//         count++;
//     }

//     return result;
// }

// console.log(powerOptional(4)); // 16
// console.log(power(2, 6)); // 64

// console.log();

// console.log("C", "O", 2); // Rest parameters on page 74

// console.log();

// //// Closure

// function wrapValue(n) {
//     let local = n;
//     return() => local;
// }

// let wrap1 = wrapValue(1);
// let wrap2 = wrapValue(2);

// console.log(wrap1()); // 1
// console.log(wrap2()); // 2

// console.log();

// function multiplier(factor) {
//     return number => number * factor;
// }

// let twice = multiplier(2);
// console.log(twice(5)); // 10;


// // // #### 2022-07-26

//// Recursion

function powerRecursion(base, exponent) {
    if(exponent == 0) {
        return 1;
    } else {
        return base * powerRecursion(base, exponent - 1);
    }
}

console.log(powerRecursion(2, 3)); // 8

// if exponent == 0
console.log(powerRecursion(2, 0)); // 1

console.log();

function findSolution(target) {
    function find(current, history) {
        if(current == target) {
            return history;
        } else if(current > target) {
            return null;
        } else {
            // template literal solution
            return find(current + 5, `(${history} + 5)`) ||
                    find(current * 3, `(${history} * 3)`);

            // // non-template literal
            // return find(current + 5, "(" + history + " + 5)") ||
            //         find(current * 3, "(" + history + " * 3)");
        }
    }
    return find(1, "1");
}


console.log(findSolution(24)); // (((1 * 3) + 5) * 3)


// // emphasis
// find(1, "1")
//     find(6, "(1 + 5)")
//         find(11, "((1 + 5) + 5)")
//             find(16, "(((1 + 5) + 5) + 5)")
//             too big
//             find(33, "(((1 + 5) + 5) * 3)")
//             too big
//         find(18, "((1 + 5) * 3)")
//         too big
//     find(3, "(1 * 3)")
//     find(8, "((1 * 3) + 5)")
//         find(13, "(((1 * 3) + 5) + 5)")
//         found!
