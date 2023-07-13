// printing something on the console

console.log('hello everyone');

alert('i am a tech enterprenuer');

//variables

let nameofmine = 'Michael';
let age = 32;
let hobbies = ['sports', 'cooking', 'Reading'];
let job = {title: 'Enterprenuer', place: 'Nairobi'};



alert(age);


//functions

function logger(){
    console.log("I have faith in what am doing");
    console.log("I have faith in what am doing");
    console.log("I have faith in what am doing");
    console.log("I have faith in what am doing");
    console.log(hobbies);
}

logger();

//this is also a function

function adder(num1, num2){
    console.log(num1 + num2);
}

adder(9,7);

// a function that turns text to uppercase

const ojuu = "Dev Ed";
let mine ="I am feeling good ooooh"

function toUpper(text){
    const upperCased = text.toUpperCase();
    console.log(upperCased);
}

toUpper(ojuu);
toUpper(mine);

//string concatenation

console.log("Hello am the" + " Owner");
console.log("Hola una nina, it's me");

console.log(`hello it's me and my name is ${ojuu}`);

age =43;

console.log(`My name is ${ojuu} and my age is ${age}`);

console.log(typeof age)

// if else statements

const yourage = 18;

if(yourage > 28){
    console.log("You are good to go");
} 
else if(yourage === 18){
    console.log("Seems that you have grown old already");
}
else if (yourage <= 15){
    console.log("Go do your home work");
}
else{
    console.log("You are too young");
}

// another if else statement

const dice1 = 5;
const dice2 = 10;

if (dice1 === 5 && dice2 === 9){
    console.log("You are the winner")
}
else{
    console.log("You are just another loser")
}

// 

if (dice1 === 5 || dice2 === 9){
    console.log("You are the winner")
}
else{
    console.log("You are just another loser")
}

// Arrays
// this are variables that you can store multiple values inside them

let booms = ['sports', 'cooking', 'Reading', 'playing games', 'Praying'];
console.log(booms);
// to add values to an array


