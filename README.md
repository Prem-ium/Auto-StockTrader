<h1 align="center"> ⚙️ Auto Stock Trader 💵 </h1>

<p align="center">An <i>awesome</i> repository containing scripts and projects for automating stock orders across multiple brokerages.</p>

<p align="right"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/><a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="Github Sponsor"/></a></p>

## Features

- Multiple Stock Ticker Automation (Seperated by `,`)
- Pre-Market, Market, & Post-Market Support
- Quickstart Desktop `.bat` Script
- XPATH Error Handling & Output
- Market & Limit Order Support
- Account Quickstart Python Script
- Login Credentials Automation

*Note: Top Github Sponsor/Buy-Me-Coffee donation contributors may get access to more advanced beta features before the public.*

## Supported Brokerages
This project contains the means of automating buy/sell stock orders within:

- Ally Invest
- Chase JP Morgan Investments
- Charles Schwab
- Firstrade
- Fidelity
- Merrill Edge Lynch
- Sofi Invest
- Vanguard

## Enviornmental Variables

To use this project, you will need to set the following environment variables in your .env file:

`SCHWAB_AI` = Total number of SCHWAB accounts.

`MERRILL_AI` = Total number of Merrill accounts.

`CHASE_AI` = A list of stringified JSON array containing your Chase Investment AI numbers
[found within the desktop stock order URL](https://user-images.githubusercontent.com/80719066/216079858-746af166-8387-41ad-9564-dd0c6285eb39.png), separated by commas.

`FIDELITY_AI` = A list of stringified JSON array containing your Fidelity Investment account numbers, separated by commas.

`ALLY_AI` = A stringified JSON array containing your Ally Investment account name + numbers, separated by commas.

- In [Ally Invest Settings Webpage](https://live.invest.ally.com/settings), you will need to change the default orders on the settings for all accounts to be a small penny stock for default stock ticker to miminize risk, Market, & Quantity: 1. Otherwise, running the automation script will buy 100 shares by default or whatever number you've previously entered into Ally default order settings.

`FIRSTRADE_AI` = A stringified JSON array containing your FirstTrade Investment account numbers, separated by commas.

`VANGUARD_AI` = A stringified JSON array containing your Vanguard Investment account numbers, separated by commas. (Only for old Outdated Test Cases)

`CUSTOM_DIR` = Directory path updated .side files should be located. (Optional)

Example:

```bash
CHASE_AI="['1234567890','0987654321']";
ALLY_AI="['Individual-A123456789','Individual-B098765432']";
FIRSTRADE_AI="['111111','222222']";
VANGUARD_AI="['54554326','54678936']";
```

**Account Credentials Separated by ':'**

To attempt to enter credentials or login where possible, you can set the following environment variables: 

- `CHASE_LOGIN`: "USERNAME:PASSWORD" for Chase.
- `FIDELITY_LOGIN`: "USERNAME:PASSWORD" for Fidelity.
- `FIRSTRADE_LOGIN`: "USERNAME:PASSWORD" for FirstTrade.
- `MERRILL_LOGIN`: "USERNAME:PASSWORD" for Merrill.
- `SCHWAB_LOGIN`: "USERNAME:PASSWORD" for Schwab.
- `ALLY_LOGIN`: "USERNAME:PASSWORD" for Ally.
- `VANGUARD_LOGIN`: "USERNAME:PASSWORD" for Vanguard.


Refer to `.env.example` for more clarity.

## Installation

Clone the repository & install dependencies:

```bash
git clone https://github.com/Prem-ium/Auto-StockTrader
cd Auto-StockTrader
pip install -r requirements.txt
```

Configure [Enviornmental Variables](https://github.com/Prem-ium/Auto-StockTrader#enviornmental-variables) and run the script.

```
  python main.py
```

Passing an argument will quickly update the stock orders in all .side projects.

```
  python main.py APPL
```

### Selenium IDE

This project requires the use of Selenium IDE browser extension. You will need to download it for your browser's addon extension store. Keep in mind, some browsers such as Chrome are more favorable to use than Edge with this extension. 

- [Chrome](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd)
- [Edge](https://microsoftedge.microsoft.com/addons/detail/selenium-ide/ajdpfmkffanmkhejnopjppegokpogffp)

After going through the [Installation](#Installation) & running configuring your `.env` variables, you must open the generated `.side` file of your brokerage of choice, login to your brokerage account, and start running your desired test. 

- [Selenium IDE Github Repository](https://github.com/SeleniumHQ/selenium-ide)

For more assistance, refer to [archived README](https://github.com/Prem-ium/Auto-StockTrader/blob/main/src/X_Archive/README.MD)

## Donations

I've been working on this project for a few months now, and I'm really happy with how it's turned out. Based on the testimony, it has been a great tool in automating stock ticker orders across multiple brokerage accounts in multiple different brokerages. I'm working on creating new features and optimizing the project to run automation orders as efficiently as possible.

If you would like to show your appreciation for my work, I have set up two methods of sending in a donation: 

<a href="https://github.com/sponsors/Prem-ium">Github Sponsors</a>, the ideal donation method, to make donations with no fees!
<a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA" alt="GitHub Sponsor" img width="25%">
</a>
Otherwise, <a href="https://www.buymeacoffee.com/prem.ium">Buy-Me-Coffee</a> can be used to place donations as well. 
<a href="https://www.buymeacoffee.com/prem.ium" target="_blank">
        <img src="https://raw.githubusercontent.com/Prem-ium/youtube-analytics-bot/main/output-examples/media/coffee-logo.png" alt="Buy Me A Coffee" img width="25%">
</a>

Your generous donations will greatly assist me in covering the expenses associated with developing new features and promoting the project to a broader audience. I extend my heartfelt gratitude to all those who have already contributed. Thank you!

### GitHub Sponsors Perks
#### Gold Sponsor Perks

Sponsors who contribute within the `Gold Sponsor` monthly tier on my<a href="https://github.com/sponsors/Prem-ium"> Github Sponsors page</a> are entitled to receive early access to features and perks of the Auto-StockTrader project before the public, along with access to exclusive scripts & features only available to Gold sponsoring users. 

#### Silver Sponsor Perks
Sponsors who contribute within the `Silver Sponsor` monthly tier on my<a href="https://github.com/sponsors/Prem-ium"> Github Sponsors page</a> are entitled to receive expedited bug report handling, support, and a mention on a README in a project of their choice.

##⚠️ **DISCLAIMER:**
You're using this project at your own risk. I am not responsible for any financial loss, account suspension/ban, or any other damage that may occur with the use of the project(s) in this repostory. I am not a financial advisor, nor am I affiliated with any brokerage mentioned in this repository. This project is provided "as is" and without warranty of any kind. By using this repository, the user accepts all the risks and agrees to hold the developer(s) harmless from any and all claims, damages, or losses arising from the use of the project. 

## License
This repository uses the [BSD 3-Clause “New” or “Revised” License.](https://choosealicense.com/licenses/bsd-3-clause/#)

## Acknowledgments & Final Remarks
A special thanks to all <a href="https://www.buymeacoffee.com/prem.ium" target="_blank">donor(s), </a>tester(s), and<a href="https://github.com/Prem-ium/Auto-StockTrader/graphs/contributors" target="_blank"> contributor(s).</a>

Thank you so much for your interest in this repository.
Please consider leaving a :star2: if you found this project to be cool!

### Potential Brokerages
There are currently no plans to offer automation on other brokerages not listed within this repository. However, I am open to receiving pull-requests to merge any new `.side` projects for automating new brokerages. Upon sending a pull-request, please request a review from me when you believe your PR is merge-ready. 
