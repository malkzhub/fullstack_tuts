// // // #### 2022-07-17

// //// Binding or Variable
// let caught = 5 * 5;
// console.log(caught); // 25

// let ten = 10;
// console.log(ten * ten); // 100

// let mood = "light";
// console.log(mood); // light

// mood = "dark";
// console.log(mood); // dark

// // Number of dollars that Luigi owes after paying $35
// let luigiDebt = 140;
// luigiDebt = luigiDebt - 35;
// console.log("$" + luigiDebt); // 105

// //
// let one = 1, two = 2;
// console.log(one + two); // 3

// // 
// var name = "Ayda";
// const greeting = "Hello ";
// console.log(greeting + name); // Hello Ayda

// // Javascript keywords and reserved words
// // ######
// // break, case, catch, class, const, continue, debugger, default,
// // delete, do, else, enum, export, extends, false, finally, for,
// // function, if, implements, import, interface, in, instanceof, let
// // new, package, private, protected, public, return, static, super,
// // switch, this, throw, true, try, typeof, var, void, while, with, yield

// // Functions
// // prompt("Enter Passcode:"); // View in browser


// ###################################################

// // // // #### 2022-07-17 

// console.log();

// //// Return Values
// console.log(Math.max(2, 4)); // 4
// console.log(Math.min(2, 4) + 100); // 102

// //// Control Flow
// console.log();

// // let theNumber = Number(prompt("Pick a number:")); // View in browser
// // console.log("Your number is the square root of " + theNumber * theNumber);

// //// Conditional Execution

// // View in browser
// // let theNumber = Number(prompt("Pick a number:"));

// // if(!Number.isNaN(theNumber)) {
// //     console.log("Your number is the square root of " +
// //     theNumber * theNumber);
// // }

// console.log();

// if(1 + 1 == 2) console.log("It's true");

// // // View in browser
// // let theNumber = Number(prompt("Pick a number"));
// // if(!Number.isNaN(theNumber)) {
// //     console.log("Your number is the square root of " +
// //     theNumber * theNumber);
// // } else {
// //     console.log("Hey. Why didn't you give me a number?");
// // }

// // View in browser

// // let num = Number(prompt("Pick a number"));

// // if(num < 10) {
// //     console.log("Small");
// // } else if(num < 100) {
// //     console.log("Medium");
// // } else {
// //     console.log("Large");
// // }


// //// while and do loops

// // While Loop
// let number = 0;
// while(number <= 12) {
//     console.log(number);
//     number = number + 2;
// }
// // 0
// // 2
// // ... up to 12

// console.log();

// let result = 1;
// let counter = 0;

// while(counter < 10) {
//     result = result * 2;
//     counter = counter + 1;
// }

// console.log(result); // 1024

// // Do-while Loop

// // View in browser

// // let yourName;
// // do {
// //     yourName = prompt("Who are you?");
// // } while(!yourName);

// // console.log(yourName);

// // console.log();

// // the do-while version the while example 

// let resultDo = 1;
// let counterDo = 0;

// do {
//     resultDo = resultDo * 2;
//     counterDo += 1;
// } while(counterDo < 10);

// console.log(resultDo); // 1024

// console.log();

// // Indenting Code
// if(false != true) {
//     console.log("That makes sense.");
//     if(1 < 2) {
//         console.log("No surprise there.");
//     }
// }

// console.log();

// //// For Loops
// for(let number = 0; number <= 12; number += 2) {
//     console.log(number);
// }
// // 0
// // 1
// // 2
// // ... up to 12

// console.log();

// // the for loop example of the while example above
// let resultFor = 1;
// for(let counter = 0; counter < 10; counter += 1) {
//     resultFor *= 2;
// }

// console.log(resultFor); // 1024

// console.log();


// //// Breaking out of a loop

// // Find the first number that is both greater than or equal to 20 and divisible by 7
// for(let current = 20; current += 1;) {
//     if(current % 7 == 0) {
//         console.log(current); //21
//         break;
//     }
// }

// ////// #######################################
// ////// #### EXERCISE
// ////// #######################################

// // // Using for, while, and do-while loops, show a list of odd and even numbers
// // // up to 100

// // // Even - For loop

// // for(let evenFor = 0; evenFor <= 100; evenFor++) {
// //     if(evenFor % 2 === 0) {
// //         console.log("evenFor: " + evenFor);
// //     }
// // }

// // console.log();


// // // Even - While loop
// // let evenWhile = 0;
// // while(evenWhile <= 100) {
// //     if(evenWhile % 2 === 0) {
// //         console.log("evenWhile: " + evenWhile);
// //     }
// //     evenWhile++;
// // }

// // console.log();

// // // Even - Do-While loop
// // let evenDo = 0;
// // do {
// //     if(evenDo % 2 === 0) {
// //         console.log("evenDo: " + evenDo);
// //     }
// //     evenDo++;
// // } while(evenDo <= 100);


// // console.log();


// // // Odd - For loop
// // for(let oddFor = 0; oddFor <= 100; oddFor++) {
// //     if((oddFor % 2 !== 0)) {
// //         console.log("oddFor: " + oddFor);
// //     }
// // }

// // console.log();


// // // Odd - While loop
// // let oddWhile = 0;

// // while(oddWhile <= 100) {
// //     if(oddWhile % 2 !== 0) {
// //         console.log("oddWhile: " + oddWhile);
// //     }
// //     oddWhile++;
// // }

// // console.log();


// // // Odd - Do-While loop

// // let oddDo = 0;
// // do {
// //     if(oddDo % 2 !== 0) {
// //         console.log("oddDo: " + oddDo);
// //     }
// //     oddDo++;
// // } while(oddDo <= 100);


// // // ####################################################################

// // // // #### 2022-07-20

// //// Updating Bindings Succintly
// // counter = counter + 1;

// // // JS shortcut

// // counter += 1;
// // counter -= 2;
// // counter *= 3;
// // counter /= 4;
// // counter++;
// // counter--;

// for(let number = 0; number <= 12; number += 2) {
//     console.log(number);
// }

// // 0
// // 2
// // 4
// // ... up to 12 incremented 2 numbers


// console.log();

// //// Dispatching on a Value with switch

// // // View in browser
// // switch(prompt("What is the weather like?")) {
// //     case "rainy":
// //         console.log("Remember to bring an umbrella.");
// //         break;
// //     case "sunny":
// //         console.log("Dress lightly");
// //         break;
// //     case "cloudy":
// //         console.log("Go outside");
// //         break;
// //     default:
// //         console.log("Unknown weather type!");
// // }

// console.log();

// //// Capitalization

// // // Note: binding names with several words

// // fuzzylittleturtle
// // fuzzy_little_turtle
// // FuzzyLittleTurtle
// // fuzzyLittleTurtle

// //// Comments
// // or /* */


////// #######################################
////// #### EXERCISE
////// #######################################


//// ###### Looping a Triangle

// Write a loop that makes seven calls to console.log() to
// output the following triangle
//
// #
// ##
// ###
// ####
// #####
// ######
// #######

// Answer:

for(let i = "#"; i.length < 8; i += "#") {
    console.log(i);
}


console.log();

//// ###### FizzBuzz

// Write a program that uses console.log(); to print all the numbers from 1
// to 100, with two exceptions. For numbers divisible by 3, print "Fizz"
// instead of the number, and for numbers divisible by 5 (and not 3), 
// print "Buzz" instead.

// Answer:
let fizzBuzz = 1;
do {
    let output = "";
    if(fizzBuzz % 3 == 0) {
        output += "Fizz";
    } else if(fizzBuzz % 5 == 0) {
        output += "Buzz"
    }

    console.log(output || fizzBuzz);

    fizzBuzz++;
} while(fizzBuzz <= 100);

console.log();

//// ###### Chessboard

// Write a program that creates a string that represents an
// 8x8 grid, using new-line characters to separate lines.
// At each position of the grid there is 
// either a space or a # character. The characters
// should form a chessboard.
//
// Passing this string to console.log() should show something like this:
//
//  # # # #
// # # # #
//  # # # #
// # # # #
//  # # # #
// # # # #
//  # # # #
// # # # #

// Answer

let grid = 8;
let board = "";

for(let y = 0; y < grid; y++) {
    for(x = 0; x < grid; x++) {
        if((x + y) % 2 == 0) {
            board += " ";
        } else {
            board += "#";
        }
    }
    board += "\n";
}

console.log(board);
