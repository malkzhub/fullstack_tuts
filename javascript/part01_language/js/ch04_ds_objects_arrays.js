// // // // #### 2022-08-01

///// Data Structures: Objects and Arrays

//// Data Sets

//// Array
let listOfNumbers = [2, 3, 5, 7, 11];
console.log(listOfNumbers[2]); // 5
console.log(listOfNumbers[0]); // 2
console.log(listOfNumbers[2 - 1]); // 3

//// Properties
// null.length; // TypeError: null has no properties

console.log();

//// Methods
let doh = "Doh";
console.log(typeof doh.toUpperCase); // function
console.log(doh.toUpperCase()); // DOH

console.log();

// Manipulating Arrays
let sequence = [1, 2 ,3];
sequence.push(4);
sequence.push(5);
console.log(sequence); // [1, 2, 3, 4, 5]

console.log(sequence.pop()); // 5

console.log(sequence); // [1, 2, 3, 4]

console.log();

//// Objectes
let day1 = {
    squirrel: false,
    events: ["work", "touched tree", "pizza", "running"]
};

console.log(day1.squirrel); // false
console.log(day1.wolf); // undefined

day1.wolf = false;
console.log(day1.wolf); // false

console.log();

let descriptions = {
    work: "Went to work",
    "touched tree": "Touched a tree"
};

console.log();

let anObject = {left: 1, right: 2};

console.log(anObject.left); // 1

delete anObject.left;
console.log(anObject.left); // undefined
console.log("left" in anObject); // false
console.log("right" in anObject); // true

console.log();

// Finding out what properties an object has
console.log(Object.keys({x: 0, y: 0, z: 2}));
// ["x", "y", "z"]

let objectA = {a: 1, b: 2};
Object.assign(objectA, {b: 3, c: 4});
console.log(objectA); // {a: 1, b: 3, c: 4}

console.log();

let journal = [
    {
        events: [
            "work",
            "touched tree",
            "pizza",
            "running",
            "television"
        ],
        squirrel: false
    },
    {
        events: [
            "work",
            "ice cream",
            "cauliflower",
            "lasagna",
            "touched tree",
            "brushed teeth"
        ],
        squirrel: false
    },
    {
        events: [
            "weekend",
            "cycling",
            "break",
            "peanuts",
            "beer"
        ],
        squirrel: true
    }
    /* and so on... */
];
console.log(journal[1]);