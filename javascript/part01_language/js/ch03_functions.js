// // #### 2022-07-21

//// ######### Functions

//// Defining a functions

const square = function(x) {
    return x * x;
};

console.log(square(12)); // 144

console.log();

const makeNoise = function() {
    console.log("Pling!");
};

makeNoise(); // Pling!

console.log();

const power = function(base, exponent) {
    let result = 1;
    for(let count = 0; count < exponent; count++) {
        result *= base;
    }

    return result;
};

console.log(power(2, 10)); // 1024

console.log();

//// Bindings and Scopes

// Note: pre-2015 JS var keyword is visibile throughout 
// the whole function that they appear or 
// throughout the global scope.

let x = 10;
if(true) {
    let y = 20;
    var z = 30;

    console.log(x + y + z); // 60
}

// y is not visible here
console.log(x + z); // 40

console.log();

// bindings with same name
const halve = function(n) {
    return n / 2;
};

let n = 10;
console.log(halve(100)); // 50
console.log(n); // 10

console.log();

//// Nested Scope
const hummus = function(factor) {
    const ingredient = function(amount, unit, name) {
        let ingredientAmount = amount * factor;
        if(ingredientAmount > 1) {
            unit += "s";
        }

        console.log(`${ingredientAmount} ${unit} ${name}`); // or
        // console.log(ingredientAmount + " " + unit + " " + name); 
    };

    ingredient(1, "can", "chickpeas");
    ingredient(0.25, "cup", "tahini");
    ingredient(0.25, "cup", "lemon juice");
    ingredient(1, "clove", "garlic");
    ingredient(2, "tablespoon", "olive oil");
    ingredient(0.5, "teaspoon", "cumin");
};

console.log(hummus(13));

console.log();

//// Functions as Values

// let launchMissiles = function() {
//     missileSystem.launch("now");
// };

// if(safeMode) {
//     launchMissiles = function() {/* do nothing */}
// }


//// Declaration of Notation

function squareNotation(x) {
    return x * x;
}

console.log(squareNotation(13)); // 169

console.log();

console.log("The future says:", future());

function future() {
    return "You'll never have flying cars";
}

console.log();

//// Arrow functions

const powerArrow = (base, exponent) => {
    let result = 1;
    for(let count = 0; count < exponent; count++) {
        result *= base;
    }

    return result;
};

console.log(powerArrow(2, 8)); // 256

console.log();

// if there is only one parameter name, omit the parenthesis around the parameter list.

const square1 = (x) => { return x * x };
const square2 = x => x * x;

console.log(square1(3));
console.log(square2(4));

console.log();

// if arrow function has no parameters at all
const horn = () => {
    console.log("Toot");
};

horn();

console.log();