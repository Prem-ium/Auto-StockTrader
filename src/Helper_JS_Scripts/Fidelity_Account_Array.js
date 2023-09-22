// Instructions for Non-Technical Users:

// 1. Open Fidelity Portfolio Webpage (https://digital.fidelity.com/ftgw/digital/portfolio)

// 2. Access the Browser's Developer Tools:
//    - If you're using Google Chrome: Right-click anywhere on the webpage, then click "Inspect."
//    - If you're using Mozilla Firefox: Right-click anywhere on the webpage, then select "Inspect Element."
//    - If you're using Microsoft Edge: Right-click anywhere on the webpage, then choose "Inspect."

// 3. Copy and Paste the Script:
//    - In the Developer Tools panel, find the "Console" tab or section.
//    - Copy the entire script
//    - Paste the script into the space in the Console.

// 4. Run the Script:
//    - After pasting the script, press "Enter" on your keyboard. The script will execute, and you'll see numbers in the Console.

// 5. Copy the Numbers:
//    - Select all the numbers in the Console by clicking and dragging your mouse cursor.
//    - Right-click on the selected numbers and choose "Copy."

// 6. Paste the Numbers into .env file:
//    - Open the ".env" file using a text editor like Notepad or TextEdit.
//    - Find the section that mentions "Fidelity env variable" (fix the typo if needed).
//    - Remove any existing content in that section.
//    - Right-click inside the section and select "Paste" to insert the copied numbers.
//    - Save the ".env" file after making this change.

// You can alos use the Fidelity side project login test, with index of 1, to obtain the account numbers.


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
