// Open Fidelity Portfolio and Run this Script in the Console
// Copy the Array and Paste it into the Fidelity env varaible in the .env file

// Get all elements with the class name "acct-selector__acct-num"
const elements = document.getElementsByClassName("acct-selector__acct-num");

// Create an array to store the text content
const textArray = [];

// Iterate through the elements and store the trimmed text content in the array
for (let i = 0; i < elements.length; i++) {
  const text = elements[i].textContent.trim();
  textArray.push(text);
}

// Print the array
console.log(textArray);
