
/*
    Login to Sofi's Invest Homepage on your browser and run this script in the console.
*/
const accountNumbers = [];
const links = document.getElementsByTagName("a");
for (let i = 0; i < links.length; i++) {
  const href = links[i].getAttribute("href");
  if (href && href.includes("account/") && !href.includes("/wealth/app/")) {
    const accountNumber = href.replace("account/", "");
    accountNumbers.push(accountNumber);
  }
}
console.log(accountNumbers);
