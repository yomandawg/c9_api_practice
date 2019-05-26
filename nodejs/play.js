const fs = require('fs'); // file system functionalities
fs.writeFileSync('hello.txt', 'Hello from Node.js!'); // where to store the file, what to write


const name = 'Max'; // unchangeable
let age = 29; // changeable
var hasHobbies = true; // changeable

function summarizeUser(userName, userAge, userHasHobby) {
    return (
        'Name is ' +
        userName +
        ', age is ' +
        userAge +
        ' and the user has hobbies: ' +
        userHasHobby
    );
};

console.log(summarizeUser(name, age, hasHobbies));

const summarize = function (userName) {
    return;k
};

// arrow function
// name of the funtion = (arguments) => {function block}
const summarizer = (userName, userAge) => {
    return;
};

// single lines without brackets
const add = (a, b) => a + b;
const addOne = a => a + 1;
const addRandom = () => 1 + 2;

console.log(addRandom());


// js object
const person = {
    name: 'Max',
    age: 29,
    // this block scope
    greet() {
        console.log('Hi, I am ' + this.name);
    },
    // this global scope
    greetings: () => {
        console.log('Hi, I am ' + this.name);
    },
    greeters: () => {
        console.log('Hi, I am ' + name);
    }
};

console.log(person);
person.greet();
person.greetings();
person.greeters();


// arrays: reference types
const hobbies = ['Sports', 'Cooking'];

// iteration
for (let hobby of hobbies) {
    console.log(hobby);
}

// return mapped array
console.log(hobbies.map(hobby => 'Hobby: ' + hobby));

// array references(pointer);
// can alter items inside array without violating the const factor
hobbies.push('Programming');
console.log(hobbies);


// slice copies an array
const copiedArray = hobbies.slice();
console.log(copiedArray);

// light copy
const sample = hobbies;
console.log(sample);
hobbies.push('Gym');
console.log(sample);

// Spread Operator - deepcopy
const sampleArray = [...hobbies];
console.log(sampleArray);

// spread operator pull all the objects and add to the new one
const copiedPerson = {...person};
console.log(copiedPerson);

// Rest Operator pull elements out of object and merge it into an array
const toArray = (...args) => {
    return args;
};
console.log(toArray(1, 2, 3));
console.log(toArray(1, 2, 3, 4));


// Object Destructuring- allows to access elements in objects or arrays quickly by their name or position
const printName = ({ name }) => {
    console.log(name);
}
printName(person);

const hobbies2 = ['Sports', 'Cooking'];
const [hobby1, hobby2] = hobbies2
console.log(hobby1, hobby2);


// Async function
setTimeout(() => {
    console.log('Timer is done!')
}, 2000);
// the following codes execute right away
console.log('Next line!');
// JS does not block your code execution until that is done
// will recognize the callback function; calls back later when it's done

// create a constructor promise function inside 
const fetchData = () => {
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Done!');
        }, 1500);
    });
    return promise;
};

setTimeout(() => {
    console.log('Timer is done!');
    // then is callable on a promise
    fetchData()
        .then(text => {
            console.log(text);
            return fetchData();
        })
        .then(text2 => {
            console.log(text2);
        });
}, 2000);

console.log('Hello!');