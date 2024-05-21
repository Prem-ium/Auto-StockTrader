<h1 align="center"> ⚙️ Auto Stock Trader 💵 </h1>

<p align="center">An <i>awesome</i> repository containing scripts and projects for automating stock orders across multiple brokerages.</p>

<p align="right"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/><a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="Github Sponsor"/></a></p>

# Features
- Multiple Stock Tickers Support (ex: `NVDA,TSLA,AAPL` buys/sells in one test run)
- Multiple Accounts/Login Support 
- Dynamic Error Checking & Handling using XPATHs
- Account Slicing (Automate from a specific account & onward)
- Extended Hours Support for Certain Brokerages
- Limit Order Support for Certain Brokerages
- `.bat` Script to Update `.side` files with new Tickers, Account Variables, etc.
- Account Login Automation 
- JavaScript Account Array Helper Scripts

## Notice
Gold GitHub Sponsors will gain access to a private `sponsor` repository, which includes the latest updates and exclusive features. The free, public version of this project will not be updated as frequently as the sponsor repository. If you are a Gold Sponsor, make sure to reference the `sponsor` repo's README instead of the public README, as the `sponsor` repo contains significant upgrades and changes not available in the public version. If you're interested in becoming a Gold Sponsor, you can [become one here.](https://github.com/sponsors/Prem-ium)

## Supported Brokerages
This project contains the means of automating buy/sell stock orders within:

- Ally Invest
- Charles Schwab
- Chase's J.P. Morgan Invest
- Fidelity
- Firstrade
- Merrill Edge Lynch
- Sofi Invest
- Vanguard
- Robinhood (GitHub Gold Sponsor, Early Access)
- WellsTrade (GitHub Gold Sponsor, Exclusive Access)

Note: Please note that although I no longer have an Ally Invest or Merrill Edge account, the existing scripts should still function as intended. However, I won't be able to provide updates or make changes specific to those platforms.

# Enviornmental Variables
To use this project, you will need to set the following environment variables in your .env file:
| Variable          | Description                                       | Type                 |
|-------------------|---------------------------------------------------|----------------------|
| `SCHWAB_AI`         | Total Number of Schwab Accounts                  | Integer              |
| `MERRILL_AI`      | Total Number of Merrill Accounts                 | Integer              |
| `VANGUARD_AI`       | Total Number of Vanguard Accounts  | Integer       |
| `FIDELITY_AI`       | Fidelity account numbers                          | Nested List of Strings|
| `CHASE_AI`          | [AI Values found in Chase's Trade URL for each account](https://user-images.githubusercontent.com/80719066/216079858-746af166-8387-41ad-9564-dd0c6285eb39.png). You can find [Step-By-Step](https://github.com/Prem-ium/Auto-StockTrader/blob/main/src/README.MD#chase-automation) here.           | Nested List of Strings| 
| `FIRSTRADE_AI`      | Firstrade Account Numbers | List of Strings       |
| `ALLY_AI`           | Ally Account Numbers -- In [Ally Invest Settings Webpage](https://live.invest.ally.com/settings), change the default orders on the settings for all accounts to be a small penny stock for default stock ticker to minimize risk, Market, 1 Quantity!! | List of Strings       |
| `ROBINHOOD_AI`*    | Total Number of Robinhood Accounts                 | Integer              |
| `WELLSTRADE_AI`*    | Total Number of Wellstrade Accounts                 | Integer              |
| --|--|--|
| `CUSTOM_DIR`        | Path to the folder to store updated .side files  | String               |
| `INCLUDE_PREMARKET`*        | Include Pre-Market in Buy/Sell Suite  | Boolean               |
| `SET_SPEED`*        | Modify default speed of IDE execution (in milliseconds). Defaults to fastest (0).  | Integer               |
| `DYNAMIC`           | Dynamic Account Length Feature (0=Off, 1=On)    | Integer              |
| `SOFI_AI`           | List of account numbers for Sofi Helper Auto.side| List of Strings       |
| `SOFI_ACCOUNT_NAMES`| Account names and numbers for SoFi Auto.side    | String               |
| `SOFI_LOGIN`        | Login credentials for SoFi Auto.side file       | String               |
| `EXCLUDE_ACCOUNTS`  | List of SoFi account names to exclude           | String               |

`*` = Reference for Gold Sponsors Only

[Need more help?](https://github.com/Prem-ium/Auto-StockTrader/blob/main/src/README.MD) 


<details>
  <summary>Login Env Example</summary>
  <p>

  If you prefer, you can store your login information in a `.env` file to automatically open and log in to any brokerage. However, I strongly advise against this practice. Instead, I recommend using the login test to open the login URL and manually log in. Storing credentials in a `.side` file is  discouraged due to security reasons. Multiple account credentials are separated by the `:` character.

  Please note that the login test is a best-try approach. Some brokerages, like Chase, may block automated logins, but you can quickly fill out the user/password information manually if you choose to use this tool.
  </p>
  
  | Variable          | Description                                   | Type    | Example                        |
  |-------------------|-----------------------------------------------|---------|--------------------------------|
  | `CHASE_LOGIN`     | Chase Account Credentials                     | String  | CHASE_LOGIN="USERNAME:PASSWORD" |
  | `FIDELITY_LOGIN`  | Fidelity Account Credentials                  | String  | FIDELITY_LOGIN="USERNAME:PASSWORD"|
  | `FIRSTADE_LOGIN`  | Firstrade Account Credentials                 | String  | FIRSTADE_LOGIN="USERNAME:PASSWORD"|
  | `MERRILL_LOGIN`   | Merrill Account Credentials                    | String  | MERRILL_LOGIN="USERNAME:PASSWORD"|
  | `SCHWAB_LOGIN`    | Schwab Account Credentials                     | String  | SCHWAB_LOGIN="USERNAME:PASSWORD" |
  | `ALLY_LOGIN`      | Ally Account Credentials                       | String  | ALLY_LOGIN="USERNAME:PASSWORD"   |
  | `VANGUARD_LOGIN`  | Vanguard Account Credentials                   | String  | VANGUARD_LOGIN="USERNAME:PASSWORD"|
</details>



Refer to `.env.example` for more clarity.

# Installation

Follow these steps to set up and use Selenium IDE for automation:

1. **Download Selenium IDE:**
   - Download and install the Selenium IDE browser extension for your preferred browser from the addon extension store. We recommend using Chrome or Chromium browser for the best experience.
     - [Chrome Webstore Selenium IDE Page](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd)
     - [Edge Addon Selenium IDE Page](https://microsoftedge.microsoft.com/addons/detail/selenium-ide/ajdpfmkffanmkhejnopjppegokpogffp)

2. **Clone Repository & Install Dependencies:**
   ```bash
        git clone https://github.com/Prem-ium/Auto-StockTrader
        cd Auto-StockTrader
        pip install -r requirements.txt
    ```
    
3. **Configure Environment Variables (`.env`):**
    - Create `.env` & Configure your (`.env`) file using [Environmental Variables](https://github.com/Prem-ium/Auto-StockTrader#environmental-variables) formats.

4. **Run the Python Script:**
  ```
    python main.py
  ```

  - Pass a Stock Ticker as an argument to update all `.side` files

  ```
    python main.py APPL
  ```

  - Seperate multiple with `,`
  ```bsh
    python main.py NVDA,TSLA,APPL
  ```

5. **Open Updated Side Files:**
   - Open updated `.side` project files in Selenium IDE.

6. **Execute Desired Automation within Selenium IDE:**
   - Log in to your brokerage account.
   - Begin running your desired automation tasks in either the buy or sell test tabs.

For the most reliable automation runs, it is recommended to use Chrome or Chromium browser.

# Donations

I've been diligently working on this project for several months, and I'm thrilled with the progress it has made. Based on user testimonials, it has proven to be an invaluable tool for automating stock ticker orders across multiple brokerage accounts and various brokerages. I am continually striving to enhance its functionality and optimize its efficiency for automated order execution.

If you appreciate my work and would like to show your support, there are two convenient ways to make a donation:

1. **GitHub Sponsors**
   - [Donate via GitHub Sponsors](https://github.com/sponsors/Prem-ium)
   - This is the preferred donation method as you can place donations with no transaction fees & possibily receive perks for your donation.
   - [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)

2. **Buy Me A Coffee**
   - [Donate via Buy Me A Coffee](https://www.buymeacoffee.com/prem.ium)
   - [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)

Your generous donations will go a long way in helping me cover the expenses associated with developing new features and promoting the project to a wider audience. I extend my heartfelt gratitude to all those who have already contributed. Thank you for your support!

# License
This repository follows the [BSD 3-Clause “New” or “Revised” License.](https://choosealicense.com/licenses/bsd-3-clause/#)

# Project Tree
```
📦 
├─ .env.example
├─ .github
│  └─ FUNDING.yml
├─ .gitignore
├─ LICENSE
├─ README.md
├─ main.py
├─ requirements.txt
└─ src
   ├─ Helper_Scripts
   │  ├─ Fidelity_Account_Array.js
   │  ├─ RSA-QuickStart.bat
   │  ├─ RSA-QuickStart.sh
   │  └─ SoFi_Account_Array.js
   ├─ README.MD
   ├─ Selenium_IDE
   │  ├─ Ally_Auto.side
   │  ├─ Chase_Auto.side
   │  ├─ Fidelity_Auto.side
   │  ├─ Firstrade_Auto.side
   │  ├─ Merrill_Auto.side
   │  ├─ Schwab_Auto.side
   │  └─ Vanguard_Auto.side
   └─ X_Archive
      ├─ README.MD
      ├─ Sofi Helper.side
      └─ sofi_main.py
```
# Acknowledgments / Final Remarks
I express my sincere gratitude to <a href="https://github.com/sponsors/Prem-ium">my sponsors</a>, <a href="https://www.buymeacoffee.com/prem.ium" target="_blank">donators</a>, &<a href="https://github.com/Prem-ium/Auto-StockTrader/graphs/contributors" target="_blank"> project contributor(s).</a>  Your support is invaluable, and it enables me to create exciting projects like this.

Thank you for backing my work. Each one of you plays a crucial role, and I am truly grateful for your contributions.
If you find this project interesting, please consider leaving a :star2:, <a href="https://github.com/sponsors/Prem-ium">donating, </a> or <a href="https://github.com/Prem-ium/Auto-StockTrader/graphs/contributors" target="_blank">contributing</a> if you found this project to be helpful!

### Speed Considerations:
- Depending on your computer's speed, you may need to slow down test execution on faster machines (This can be done by assigning the `SET_SPEED` env, for Gold Sponsors. Otherwise, free-users may adjust the value manually using the slider in Selenium IDE).
- Selecting 'Reference' instead of 'Log' in Selenium IDE can slightly speed up execution.
- Enabling 'Best performance' battery mode on Laptop Battery settings can slightly speed up execution.

### ⚠️ DISCLAIMER ⚠️
I am not a financial advisor, nor am I affiliated with any brokerage mentioned in this repository. 

You may use this tool at your own risk. I am not responsible for any financial loss, account restriction, or any other damage that may occur with the use of this tool. This project is provided "as is" and without warranty of any kind. 

By using this repository, the user accepts all the risks and agrees to hold the developer(s) harmless from any and all claims, damages, or losses arising from the use of the project. 
