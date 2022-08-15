// // // // // // // #### 2022-08-01

// // // ///// Data Structures: Objects and Arrays

// // // //// Data Sets

// // // //// Array
// // // let listOfNumbers = [2, 3, 5, 7, 11];
// // // console.log(listOfNumbers[2]); // 5
// // // console.log(listOfNumbers[0]); // 2
// // // console.log(listOfNumbers[2 - 1]); // 3

// // // //// Properties
// // // // null.length; // TypeError: null has no properties

// // // console.log();

// // // //// Methods
// // // let doh = "Doh";
// // // console.log(typeof doh.toUpperCase); // function
// // // console.log(doh.toUpperCase()); // DOH

// // // console.log();

// // // // Manipulating Arrays
// // // let sequence = [1, 2 ,3];
// // // sequence.push(4);
// // // sequence.push(5);
// // // console.log(sequence); // [1, 2, 3, 4, 5]

// // // console.log(sequence.pop()); // 5

// // // console.log(sequence); // [1, 2, 3, 4]

// // // console.log();

// // // //// Objectes
// // // let day1 = {
// // //     squirrel: false,
// // //     events: ["work", "touched tree", "pizza", "running"]
// // // };

// // // console.log(day1.squirrel); // false
// // // console.log(day1.wolf); // undefined

// // // day1.wolf = false;
// // // console.log(day1.wolf); // false

// // // console.log();

// // // let descriptions = {
// // //     work: "Went to work",
// // //     "touched tree": "Touched a tree"
// // // };

// // // console.log();

// // // let anObject = {left: 1, right: 2};

// // // console.log(anObject.left); // 1

// // // delete anObject.left;
// // // console.log(anObject.left); // undefined
// // // console.log("left" in anObject); // false
// // // console.log("right" in anObject); // true

// // // console.log();

// // // // Finding out what properties an object has
// // // console.log(Object.keys({x: 0, y: 0, z: 2}));
// // // // ["x", "y", "z"]

// // // let objectA = {a: 1, b: 2};
// // // Object.assign(objectA, {b: 3, c: 4});
// // // console.log(objectA); // {a: 1, b: 3, c: 4}

// // // console.log();

// // // let journal = [
// // //     {
// // //         events: [
// // //             "work",
// // //             "touched tree",
// // //             "pizza",
// // //             "running",
// // //             "television"
// // //         ],
// // //         squirrel: false
// // //     },
// // //     {
// // //         events: [
// // //             "work",
// // //             "ice cream",
// // //             "cauliflower",
// // //             "lasagna",
// // //             "touched tree",
// // //             "brushed teeth"
// // //         ],
// // //         squirrel: false
// // //     },
// // //     {
// // //         events: [
// // //             "weekend",
// // //             "cycling",
// // //             "break",
// // //             "peanuts",
// // //             "beer"
// // //         ],
// // //         squirrel: true
// // //     }
// // //     /* and so on... */
// // // ];
// // // console.log(journal[1]);

// // // // // // // #### 2022-08-02

// // //// Mutability

// // let object1 = {value: 10};
// // let object2 = object1;
// // let object3 = {value: 10};

// // console.log(object1 == object2); // true
// // console.log(object1 == object3); //false

// // object1.value = 15;
// // console.log(object2.value); // 15

// // console.log(object3.value); // 10

// // console.log();

// // const score = {visitors: 0, home: 0};
// // // this is okay
// // score.visitors = 1;

// // // This isn't allowed
// // // score = {visitors: 1, home: 1}; 
// // // // TypeError: Assignment to constant variable

// // console.log();

// // //// The Lycanthrope's Log
// // let journal = [];

// // function addEntry(events, squirrel) {
// //     journal.push({
// //         events,
// //         squirrel
// //     });
// // }

// // addEntry([
// //     "work",
// //     "touched tree",
// //     "pizza",
// //     "running",
// //     "television"
// // ], false);

// // addEntry([
// //     "work",
// //     "ice cream",
// //     "cauliflower",
// //     "lasagna",
// //     "touched tree",
// //     "brushed teeth"
// // ], false);

// // addEntry([
// //     "weekend",
// //     "cycling",
// //     "break",
// //     "peanuts",
// //     "beer"
// // ], true);


// // console.log();

// // //// Computing Correlation
// // function phi(table) {
// //     return (table[3] * table[0] - table[2] * table[1]) /
// //     Math.sqrt((table[2] + table[3]) *
// //             (table[0] + table[1]) *
// //             (table[1] + table[3]) * 
// //             (table[0] + table[2]));
// // }

// // console.log(phi([76, 9, 4, 1])); // 0.068599434

// // console.log();



// // // Extracting two-by-two table for a specific event in a journal

// // // get journal.js

// // // ###################

// // var JOURNAL = [
// //     {"events":["carrot","exercise","weekend"],"squirrel":false},
// //     {"events":["bread","pudding","brushed teeth","weekend","touched tree"],"squirrel":false},
// //     {"events":["carrot","nachos","brushed teeth","cycling","weekend"],"squirrel":false},
// //     {"events":["brussel sprouts","ice cream","brushed teeth","computer","weekend"],"squirrel":false},
// //     {"events":["potatoes","candy","brushed teeth","exercise","weekend","dentist"],"squirrel":false},
// //     {"events":["brussel sprouts","pudding","brushed teeth","running","weekend"],"squirrel":false},
// //     {"events":["pizza","brushed teeth","computer","work","touched tree"],"squirrel":false},
// //     {"events":["bread","beer","brushed teeth","cycling","work"],"squirrel":false},
// //     {"events":["cauliflower","brushed teeth","work"],"squirrel":false},
// //     {"events":["pizza","brushed teeth","cycling","work"],"squirrel":false},
// //     {"events":["lasagna","nachos","brushed teeth","work"],"squirrel":false},
// //     {"events":["brushed teeth","weekend","touched tree"],"squirrel":false},
// //     {"events":["lettuce","brushed teeth","television","weekend"],"squirrel":false},
// //     {"events":["spaghetti","brushed teeth","work"],"squirrel":false},
// //     {"events":["brushed teeth","computer","work"],"squirrel":false},
// //     {"events":["lettuce","nachos","brushed teeth","work"],"squirrel":false},
// //     {"events":["carrot","brushed teeth","running","work"],"squirrel":false},
// //     {"events":["brushed teeth","work"],"squirrel":false},
// //     {"events":["cauliflower","reading","weekend"],"squirrel":false},
// //     {"events":["bread","brushed teeth","weekend"],"squirrel":false},
// //     {"events":["lasagna","brushed teeth","exercise","work"],"squirrel":false},
// //     {"events":["spaghetti","brushed teeth","reading","work"],"squirrel":false},
// //     {"events":["carrot","ice cream","brushed teeth","television","work"],"squirrel":false},
// //     {"events":["spaghetti","nachos","work"],"squirrel":false},
// //     {"events":["cauliflower","ice cream","brushed teeth","cycling","work"],"squirrel":false},
// //     {"events":["spaghetti","peanuts","computer","weekend"],"squirrel":true},
// //     {"events":["potatoes","ice cream","brushed teeth","computer","weekend"],"squirrel":false},
// //     {"events":["potatoes","ice cream","brushed teeth","work"],"squirrel":false},
// //     {"events":["peanuts","brushed teeth","running","work"],"squirrel":false},
// //     {"events":["potatoes","exercise","work"],"squirrel":false},
// //     {"events":["pizza","ice cream","computer","work"],"squirrel":false},
// //     {"events":["lasagna","ice cream","work"],"squirrel":false},
// //     {"events":["cauliflower","candy","reading","weekend"],"squirrel":false},
// //     {"events":["lasagna","nachos","brushed teeth","running","weekend"],"squirrel":false},
// //     {"events":["potatoes","brushed teeth","work"],"squirrel":false},
// //     {"events":["carrot","work"],"squirrel":false},
// //     {"events":["pizza","beer","work","dentist"],"squirrel":false},
// //     {"events":["lasagna","pudding","cycling","work"],"squirrel":false},
// //     {"events":["spaghetti","brushed teeth","reading","work"],"squirrel":false},
// //     {"events":["spaghetti","pudding","television","weekend"],"squirrel":false},
// //     {"events":["bread","brushed teeth","exercise","weekend"],"squirrel":false},
// //     {"events":["lasagna","peanuts","work"],"squirrel":true},
// //     {"events":["pizza","work"],"squirrel":false},
// //     {"events":["potatoes","exercise","work"],"squirrel":false},
// //     {"events":["brushed teeth","exercise","work"],"squirrel":false},
// //     {"events":["spaghetti","brushed teeth","television","work"],"squirrel":false},
// //     {"events":["pizza","cycling","weekend"],"squirrel":false},
// //     {"events":["carrot","brushed teeth","weekend"],"squirrel":false},
// //     {"events":["carrot","beer","brushed teeth","work"],"squirrel":false},
// //     {"events":["pizza","peanuts","candy","work"],"squirrel":true},
// //     {"events":["carrot","peanuts","brushed teeth","reading","work"],"squirrel":false},
// //     {"events":["potatoes","peanuts","brushed teeth","work"],"squirrel":false},
// //     {"events":["carrot","nachos","brushed teeth","exercise","work"],"squirrel":false},
// //     {"events":["pizza","peanuts","brushed teeth","television","weekend"],"squirrel":false},
// //     {"events":["lasagna","brushed teeth","cycling","weekend"],"squirrel":false},
// //     {"events":["cauliflower","peanuts","brushed teeth","computer","work","touched tree"],"squirrel":false},
// //     {"events":["lettuce","brushed teeth","television","work"],"squirrel":false},
// //     {"events":["potatoes","brushed teeth","computer","work"],"squirrel":false},
// //     {"events":["bread","candy","work"],"squirrel":false},
// //     {"events":["potatoes","nachos","work"],"squirrel":false},
// //     {"events":["carrot","pudding","brushed teeth","weekend"],"squirrel":false},
// //     {"events":["carrot","brushed teeth","exercise","weekend","touched tree"],"squirrel":false},
// //     {"events":["brussel sprouts","running","work"],"squirrel":false},
// //     {"events":["brushed teeth","work"],"squirrel":false},
// //     {"events":["lettuce","brushed teeth","running","work"],"squirrel":false},
// //     {"events":["candy","brushed teeth","work"],"squirrel":false},
// //     {"events":["brussel sprouts","brushed teeth","computer","work"],"squirrel":false},
// //     {"events":["bread","brushed teeth","weekend"],"squirrel":false},
// //     {"events":["cauliflower","brushed teeth","weekend"],"squirrel":false},
// //     {"events":["spaghetti","candy","television","work","touched tree"],"squirrel":false},
// //     {"events":["carrot","pudding","brushed teeth","work"],"squirrel":false},
// //     {"events":["lettuce","brushed teeth","work"],"squirrel":false},
// //     {"events":["carrot","ice cream","brushed teeth","cycling","work"],"squirrel":false},
// //     {"events":["pizza","brushed teeth","work"],"squirrel":false},
// //     {"events":["spaghetti","peanuts","exercise","weekend"],"squirrel":true},
// //     {"events":["bread","beer","computer","weekend","touched tree"],"squirrel":false},
// //     {"events":["brushed teeth","running","work"],"squirrel":false},
// //     {"events":["lettuce","peanuts","brushed teeth","work","touched tree"],"squirrel":false},
// //     {"events":["lasagna","brushed teeth","television","work"],"squirrel":false},
// //     {"events":["cauliflower","brushed teeth","running","work"],"squirrel":false},
// //     {"events":["carrot","brushed teeth","running","work"],"squirrel":false},
// //     {"events":["carrot","reading","weekend"],"squirrel":false},
// //     {"events":["carrot","peanuts","reading","weekend"],"squirrel":true},
// //     {"events":["potatoes","brushed teeth","running","work"],"squirrel":false},
// //     {"events":["lasagna","ice cream","work","touched tree"],"squirrel":false},
// //     {"events":["cauliflower","peanuts","brushed teeth","cycling","work"],"squirrel":false},
// //     {"events":["pizza","brushed teeth","running","work"],"squirrel":false},
// //     {"events":["lettuce","brushed teeth","work"],"squirrel":false},
// //     {"events":["bread","brushed teeth","television","weekend"],"squirrel":false},
// //     {"events":["cauliflower","peanuts","brushed teeth","weekend"],"squirrel":false}
// //   ];
  
// //   // This makes sure the data is exported in node.js —
// //   // `require('./path/to/journal.js')` will get you the array.
// //   if (typeof module != "undefined" && module.exports && (typeof window == "undefined" || window.exports != exports))
// //     module.exports = JOURNAL;
// //   if (typeof global != "undefined" && !global.JOURNAL)
// //     global.JOURNAL = JOURNAL;

// // // ###################

// // function tableFor(event, journal) {
// //     let table = [0, 0, 0, 0];
// //     for(let i = 0; i < journal.length; i++) {
// //         let entry = journal[i], index = 0;
// //         if(entry.events.includes(event)) index += 1;
// //         if(entry.squirrel) index += 2;
// //         table[index] += 1;
// //     }
// //     return table;
// // }

// // console.log(tableFor("pizza", JOURNAL));
// // // [76, 9, 4, 1];

// // console.log();



// // // // // // 2022-08-09
// // //// Array Loops

// // // Traditional Loops
// // for(let i = 0; i < JOURNAL.length; i++) {
// //     let entry = JOURNAL[i];
// //     // Do something with entry
// //     console.log("OLD JS: " + entry.events.length + " events.");
// // }

// // console.log();

// // // Modern JS Looping
// // for(let entry of JOURNAL) {
// //     console.log(`NEW JS: ${entry.events.length} events.`);
// // }


// // console.log();

// // //// The Final Analysis

// // // finding every type of event in the data set

// // function journalEvents(journal) {
// //     let events = [];
// //     for(let entry of journal) {
// //         for(let event of entry.events) {
// //             if(!events.includes(event)) {
// //                 events.push(event);
// //             }
// //         }
// //     }

// //     return events;
// // }

// // console.log();

// // console.log(journalEvents(JOURNAL));
// // // ["carrot", "exercise", "weekend", "bread", ...]

// // // Functions collects every type of event that are not 
// // // not in the events array

// // for(let event of journalEvents(JOURNAL)) {
// //     console.log(event + ":", phi(tableFor(event, JOURNAL)));
// // }

// // // carrot: 0.014097096860865023
// // // exercise: 0.06859943405700354
// // // weekend: 0.13719886811400708
// // // bread: -0.07575540190785703
// // // pudding: -0.06482037235521644
// // // and so on...

// // console.log();

// // // Showing correlations greater than 0.1 or less than -0.1
// // for(let event of journalEvents(JOURNAL)) {
// //     let correlation = phi(tableFor(event, JOURNAL));
// //         if(correlation > 0.1 || correlation < -0.1) {
// //             console.log(event + ":", correlation);
// //         }
// // }

// // // weekend: 0.13719886811400708
// // // brushed teeth: -0.3805211953235953
// // // candy: 0.12964074471043288
// // // work: -0.13719886811400708
// // // spaghetti: 0.242535625036333
// // // reading: 0.11068280537595927
// // // peanuts: 0.59026798116852


// // console.log();

// // for(let entry of JOURNAL) {
// //     if(entry.events.includes("peanuts") &&
// //     !entry.events.includes("brushed teeth")) {
// //         entry.events.push("peanut teeth");
// //     }
// // }

// // console.log(phi(tableFor("peanut teeth", JOURNAL))); // 1


// // // // // 2022-08-15
// let todoList = [];

// function remember(task) {
//     todoList.push(task);
// }

// function getTask() {
//     return todoList.shift();
// }

// function rememberUrgently(task) {
//     todoList.unshift(task);
// }

// remember("grocery");

// console.log(getTask()); // grocery
// console.log(rememberUrgently("unshift"));

// console.log();


// // indexOf() and lastIndexOf()
// console.log([1, 2, 3, 2, 1].indexOf(2)); // 1
// console.log([1, 2, 3, 2, 1].lastIndexOf(2)); // 3

// console.log();

// // slice()
// console.log([0, 1, 2, 3, 4].slice(2, 4)); // [2, 3]
// console.log([0, 1, 2, 3, 4].slice(2)); // [2, 3, 4]

// console.log();

// // concat()
// function remove(array, index) {
//     return array.slice(0, index)
//     .concat(array.slice(index + 1));
// }

// console.log(remove(["a", "b", "c", "d", "e"], 2));
// // ["a", "b", "d", "e"]


// console.log();

// //// Strings and Their Properties
// let kim = "Kim";
// kim.age = 88;
// console.log(kim.age); // undefined

// console.log();

// console.log("coconuts".slice(4, 7)); // nut
// console.log("coconut".indexOf("u")); // 5

// console.log("one two three".indexOf("ee")); // 11
// console.log("    okay \n ".trim()); // okay

// // padStart() - takes the desired length and padding
// // character as arguments

// console.log(String(6).padStart(3, "0")); // 006

// console.log();

// // split a string on every occurence
// let sentence = "Secretarybirds specialize in stomping";
// let words = sentence.split(" ");

// console.log(words);
// // ["Secretarybirds", "specialize", "in", "stomping"]

// console.log(words.join(". "));
// // Secretarybirds. specialize. in. stomping

// console.log();

// // repeat()
// console.log("LA".repeat(3)); // LALALA

// console.log();

// let string = "abc";
// console.log(string.length); // 3

// console.log(string[1]);  // b

// console.log();

// //// Rest Parameters

// function max(...numbers) {
//     let result = -Infinity;
//     for(let number of numbers) {
//         if(number > result) result = number;
//     }
//     return result;
// }

// console.log(max(4, 1, 9, -2)); // 9

// console.log();

// let numbers = [5, 1, 7];
// console.log(max(...numbers)); // 7

// let words2 = ["never", "fully"];
// console.log(["will", ...words2, "understand"]);
// // ["will", "never", "fully", "understand"]

// console.log();

// //// The Math Object
// function randomPointOnCircle(radius) {
//     let angle = Math.random() * 2 * Math.PI;
//     return {
//         x: radius * Math.cos(angle),
//         y: radius * Math.sin(angle)
//     };
// }

// console.log(randomPointOnCircle(2));
// // x: 0.3667, y: 1.966

// // three random numbers
// console.log(Math.random());
// console.log(Math.random());
// console.log(Math.random());

// // whole random number
// console.log(Math.floor(Math.random() * 10)) // random whole number


// console.log();

// //// Destructuring

// // function phi(table) {
// //     return (table[3] * table[0] - table[2] * table[1]) /
// //     Math.sqrt((table[2] + table[3]) *
// //             (table[0] + table[1]) *
// //             (table[1] + table[3]) * 
// //             (table[0] + table[2]));
// // }

// // awkward to read because of a binding pointed at
// // the array

// function phi([n00, n01, n10, n11]) {
//     return(n11 * n00 * n01) /
//     Math.sqrt((n10 + n11) * (n00 + n01) *
//     (n01 + n11) * (n00 + n10));
// }

// let {name} = {name: "Faraji", age: 23};
// console.log(name); // Faraji

// console.log();

// //// JSON

// let stringer = JSON.stringify({
//     squirrel: false,
//     events: ["weekend"]
// });

// console.log(stringer);
// // {"squirrel":false,"events":["weekend"]}

// console.log(JSON.parse(stringer).events);
// // [ 'weekend' ]

// ////// #######################################
// ////// #### EXERCISE
// ////// #######################################

//// ###### The Sum of a Range

// Write a range function that takes two arguments, start and end, and
// returns an array containing all the numbers from start up to (and
// including) end.
// Next, write a sum function that takes an array of numbers and returns
// the sum of these numbers. Run the example program and see whether it
// does indeed return 55.
// As a bonus assignment, modify your range function to take an
// optional third argument that indicates the “step” value used when
// building the array. If no step is given, the elements go up by increments
// of one, corresponding to the old behavior. The function call range(1,
// 10, 2) should return [1, 3, 5, 7, 9]. Make sure it also works with
// negative step values so that range(5, 2, -1) produces [5, 4, 3, 2].

function range(start, end, step = start < end ? 1 : - 1) {
    let array = [];

    if(step > 0) {
        for(let i = start; i <= end; i += step) {
            array.push(i);
        }
    } else {
        for(let i = start; i >= end; i += step) {
            array.push(i);
        }
    }
    return array;
}

function sum(array) {
    let total = 0;
    for(let value of array) {
        total += value;
    }
    return total;
}

console.log(range(1, 10));
console.log(range(5, 2, -1));
console.log(sum(range(1, 10)));
