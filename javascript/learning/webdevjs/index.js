// printing something on the console

console.log('hello everyone');

alert('i am a tech enterprenuer');




//VARIABLES

let nameofmine = 'Michael';
let age = 32;
let hobbies = ['sports', 'cooking', 'Reading'];
let job = {title: 'Enterprenuer', place: 'Nairobi'};



alert(age);



//FUNCTIONS

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





//STRING CONCATENATION

console.log("Hello am the" + " Owner");
console.log("Hola una nina, it's me");

console.log(`hello it's me and my name is ${ojuu}`);

age =43;

console.log(`My name is ${ojuu} and my age is ${age}`);

console.log(typeof age)





// IF ELSE STATEMENT

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





// ARRAYS


// this are variables that you can store multiple values inside them

let booms = ['sports', 'cooking', 'Reading', 'playing games', 'Praying'];
console.log(booms);

//accessing arrays
console.log(booms[1]);

// to add values to an array
booms.push('Just added A NEW STUFF');
console.log(booms);

//To delete a value in a array

booms.pop();
console.log(booms);
//to remove the first thing in ana array
booms.shift();
console.log(booms);
//to add at the beginning
booms.unshift("Hola to the world");
console.log(booms);
//to find the index of something in a array

console.log(booms.indexOf("playing games"));




//OBJECTS AND KEYWORD THIS

//lets create an object
const user={
    name: 'Mike', //this is a property
    age: 24,
    married: false,
    purchases: ['Laptop', 'house', 'monitor'],

    sayName: function(){
        console.log(this.name); //this is just like a function
    }
};

user.sayName();

//accessing different properties inside the user
console.log(user.purchases);





//FOR LOOPS AND WHILE LOOPS

//FOR LOOP

let mike = ['cars', 'computers', 'lawless', 'old fasion', 'vinatage', 'wiredo'];

for(i of mike){
    console.log(i);
    if(i === 'lawless'){
        console.log("Learn the rules you want to break");
    }
}

console.log("GOOODD MORNINGGGG");
//to stop the loop after we have found lawless
for(i of mike){
    console.log(i);
    if(i === 'lawless'){
        console.log("Learn the rules you want to break");
        break;
    }
}

//WHILE LOOP

let loading = 0;

while(loading < 5){
    console.log('You are still pretty young');
    loading +=1;
}





//DOM MANIPULATION

