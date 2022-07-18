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

// // // #### 2022-07-17 

console.log();

//// Return Values
console.log(Math.max(2, 4)); // 4
console.log(Math.min(2, 4) + 100); // 102

//// Control Flow
console.log();

// let theNumber = Number(prompt("Pick a number:")); // View in browser
// console.log("Your number is the square root of " + theNumber * theNumber);

//// Conditional Execution

// View in browser
// let theNumber = Number(prompt("Pick a number:"));

// if(!Number.isNaN(theNumber)) {
//     console.log("Your number is the square root of " +
//     theNumber * theNumber);
// }

console.log();

if(1 + 1 == 2) console.log("It's true");

// // View in browser
// let theNumber = Number(prompt("Pick a number"));
// if(!Number.isNaN(theNumber)) {
//     console.log("Your number is the square root of " +
//     theNumber * theNumber);
// } else {
//     console.log("Hey. Why didn't you give me a number?");
// }

// View in browser

// let num = Number(prompt("Pick a number"));

// if(num < 10) {
//     console.log("Small");
// } else if(num < 100) {
//     console.log("Medium");
// } else {
//     console.log("Large");
// }


//// while and do loops
let number = 0;
while(number <= 12) {
    console.log(number);
    number = number + 2;
}
// 0
// 2
// ... up to 12

console.log();

let result = 1;
let counter = 0;

while(counter < 10) {
    result = result * 2;
    counter = counter + 1;
}


console.log(result); // 1024