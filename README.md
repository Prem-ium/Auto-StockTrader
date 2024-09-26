<h1 align="center"> ⚙️ Auto Stock Trader 💵 </h1>
<!--
<p align="center">
    <img src="https://github.com/Prem-ium/Auto-StockTrader/blob/main/.github/assets/Auto-StockTrader-Banner.jpeg?raw=true" alt="Auto Stock Trader Banner" style="height: 450px;">
</p>
-->
<p align="center">An <i>awesome</i> repository containing scripts and projects for automating stock orders across multiple brokerages.</p>

<p align="right"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/><a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="Github Sponsor"/></a></p>

## Features 🚀

- **Multi-Ticker Support**: Trade multiple stock tickers like `NVDA, TSLA, AAPL` all in one swift test run! 📈
- **Multi-Account Login**: Effortlessly manage and trade across multiple accounts with seamless login automation 🔑
- **Smart Error Handling**: Dynamic error checking & handling with XPATHs ensures your trades run smoothly and without hiccups ⚙️
- **Account Slicing**: Want to focus on specific accounts? Automate starting from a particular account and beyond! 🎯
- **Extended Trading Hours**: Take advantage of extended hours for supported brokerages and never miss out on prime trading opportunities ⏰
- **Limit Order Support**: Set precise limit orders with select brokerages to stay in control of your trades! 📊
- **1-Click Updates**: Update `.side` files with new tickers, account variables, and more in a single click using `.sh` or ' `.bat` script! 🔄
- **JavaScript Helper Scripts**: Boost efficiency with easy-to-use JavaScript helper scripts for managing account arrays 💻


## Supported Brokerages 🏦
This project contains the means of automating buy/sell stock orders within:

- Ally Invest
- Charles Schwab
- Chase's J.P. Morgan Invest
- Fidelity
- Firstrade
- Merrill Edge Lynch
- Sofi Invest
- Vanguard
- Robinhood (GitHub Gold Sponsor)
- WellsTrade (GitHub Gold Sponsor)

Note: Although I no longer have an Ally Invest or Merrill Edge account, the existing scripts should still work as intended. While I can’t provide direct updates for those platforms, I am able to assist with bug fixes or issues during a remote TeamViewer session for Gold sponsors.

## 🚀 Unlock Premium Features w/ Gold Sponsorship! 🌟

Gold Sponsors get **exclusive access** to the private repository, filled with the latest updates, cool features, and handy tools. Here’s a glimpse of what you can expect as a Gold Sponsor: 

#### 🌟 **Optimized Python & Selenium Scripts**  
The private version of the automation script(s) have been **completely reworked** for maximum efficiency. Unlike the public version, which requires more configuration and manual setup (like for accounts with Chase and Fidelity), the Gold Sponsor version is designed to be **seamless**, **user-friendly**, and **fast**. 

#### ⚡ **Up-to-Date & Faster Automation**  
You gain access to the latest updates for brokerage automation and project features, ensuring that any potential optimizations, errors, or bugs are promptly addressed in the private version. In contrast, the public version remains unchanged and is not updated as frequently.

#### 💰 **Exclusive Tools**  
Gain access to the **Automated Cash Transfer/Withdrawal tool**, which lets you seamlessly consolidate funds from multiple accounts into a single account. This script also allows you to rename multiple accounts for easier management. Additionally, Gold Sponsors receive exclusive access to trading  automation for Robinhood and WellsTrade.

**Ready to upgrade?**  
[Become a Gold Sponsor **here** and unlock these exclusive benefits!](https://github.com/sponsors/Prem-ium/sponsorships?sponsor=Prem-ium&tier_id=308205&preview=false)
[![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)


## Enviornmental Variables 🔧
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
| --|--|--|
| `CUSTOM_DIR`        | Path to the folder to store updated .side files  | String               |
| `DYNAMIC`           | Dynamic Account Length Feature (0=Off, 1=On)    | Integer              |
| `SOFI_AI`           | List of account numbers for Sofi Helper Auto.side| List of Strings       |
| `SOFI_ACCOUNT_NAMES`| Account names and numbers for SoFi Auto.side    | String               |
| `SOFI_LOGIN`        | Login credentials for SoFi Auto.side file       | String               |
| `EXCLUDE_ACCOUNTS`  | List of SoFi account names to exclude           | String               |

As a reminder, if you are a Gold Sponsor, please refer to the `sponsors` repository README instead of this public version. The sponsor version includes more features and customization options tailored specifically for your needs.

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

## Installation ⚙️

Follow these steps to set up and use Selenium IDE for automation:

1. **Download Selenium IDE:**
   - Install the Selenium IDE browser extension for your preferred browser from the add-on store. For the most reliable automation runs, it is recommend to use a Chromium browser. Avoid using Firefox if possible.
     - [Chrome Web Store Selenium IDE Page](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd)
     - [Edge Add-on Selenium IDE Page](https://microsoftedge.microsoft.com/addons/detail/selenium-ide/ajdpfmkffanmkhejnopjppegokpogffp)

2. **Clone the Repository & Install Dependencies:**
   ```bash
   git clone https://github.com/Prem-ium/Auto-StockTrader
   cd Auto-StockTrader
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables (.env):**  
   Create a `.env` file and set up your environment variables following the formats outlined in the [Environmental Variables](https://github.com/Prem-ium/Auto-StockTrader#environmental-variables) section.

4. **Run the Python Script:**
   ```bash
   python main.py
   ```

   - Pass a stock ticker as an argument to update all `.side` files:
   ```bash
   python main.py AAPL
   ```

   - Separate multiple tickers with a comma:
   ```bash
   python main.py NVDA,TSLA,AAPL
   ```

5. **Open Updated .side Files:**
   - Open the updated `.side` project files in Selenium IDE.

6. **Execute Desired Automation within Selenium IDE:**
   - Log in to your brokerage account.
   - Begin running your desired automation tasks in either the buy or sell test tabs.

# Donations ❤️

I've been diligently working on this project for several months, and I'm thrilled with the progress it has made. Based on user testimonials, it has proven to be an invaluable tool for automating stock ticker orders across multiple brokerage accounts and various brokerages. I am continually striving to enhance its functionality and optimize its efficiency for automated order execution.

If you appreciate my work and would like to show your support, there are two convenient ways to make a donation:

1. **GitHub Sponsors**
   - [Donate via GitHub Sponsors](https://github.com/sponsors/Prem-ium)
   - Preferred because this donation method is fee-free and offers perks for your contribution.
   - [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)

2. **Buy Me A Coffee**
   - [Donate via Buy Me A Coffee](https://www.buymeacoffee.com/prem.ium)
   - [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)

Your generous donations will go a long way in helping me cover the expenses associated with developing new features and promoting the project to a wider audience. I extend my heartfelt gratitude to all those who have already contributed. Thank you for your support!

## Experiencing Issues? 🛠️
I'm not available to respond to issues in this repository. For direct support, please consider sponsoring me below under the `Silver` or `Gold` tier. Keep in mind that the public version is mostly "as built" and is rarely updated, while the private Gold Sponsor version receives regular updates and support.
[![Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white)](https://github.com/sponsors/Prem-ium)

## Pull Request Requirements 📋

To ensure a smooth review process, please follow these guidelines when submitting a pull request (PR):

1. **Title**: Provide a clear and concise title.
2. **Description**: Include a detailed description of changes, problems addressed, and any relevant context.
3. **Documentation**: If necessary, update comments, README, requirements, and any relevant documentation.
4. **License Compliance**: Ensure any changes made in forks uphold the [repository's license](https://github.com/Prem-ium/Auto-StockTrader/blob/main/LICENSE). Do not make changes to certain areas such as the `FUNDING.yml` or any present copyright information without approval.

Once you have verified that your changes adhere to these guidelines, please open a pull request with your changes and click 'Request Review' on the Pull Request.

By adhering to these guidelines, you help maintain the quality and consistency of the project. Thank you for your interest in making contributions!

# License
This repository follows the [BSD 3-Clause “New” or “Revised” License.](https://github.com/Prem-ium/Auto-StockTrader/blob/main/LICENSE)

<!--
<details><summary><h2>🎯 Project Tree</h2></summary>

```
├─ .env.example
├─ .github
│  └─ FUNDING.yml
├─ .gitignore
├─ LICENSE
├─ README.md
├─ main.py
├─ requirements.txt
└─ src
   ├─ Helper_Scripts
   │  ├─ Fidelity_Account_Array.js
   │  ├─ merge-tax-pdfs.py
   │  ├─ README.md
   │  ├─ requirements.txt
   │  ├─ RSA-QuickStart.bat
   │  ├─ RSA-QuickStart.sh
   │  └─ SoFi_Account_Array.js
   ├─ README.md
   ├─ Selenium_IDE
   │  ├─ Ally_Auto.side
   │  ├─ Chase_Auto.side
   │  ├─ Fidelity_Auto.side
   │  ├─ Firstrade_Auto.side
   │  ├─ Merrill_Auto.side
   │  ├─ Schwab_Auto.side
   │  └─ Vanguard_Auto.side
   └─ X_Archive
      ├─ README.md
      ├─ Sofi Helper.side
      └─ sofi_main.py
```
</details>
-->


# Acknowledgments / Final Remarks 💬
I express my sincere gratitude to <a href="https://github.com/sponsors/Prem-ium">my sponsors</a>, <a href="https://www.buymeacoffee.com/prem.ium" target="_blank">donors</a>, &<a href="https://github.com/Prem-ium/Auto-StockTrader/graphs/contributors" target="_blank"> project contributor(s).</a>  Your support is invaluable, and it enables me to create exciting projects like this.

Thank you for backing my work. Each one of you plays a crucial role, and I am truly grateful for your contributions.
If you find this project interesting, please consider leaving a :star2:, <a href="https://github.com/sponsors/Prem-ium">donating, </a> or <a href="https://github.com/Prem-ium/Auto-StockTrader/graphs/contributors" target="_blank">contributing</a> if you found this project to be helpful!

## Other Projects

- **Tax Document Consolidator (Coming Soon):**: I’m developing a 1099 Tax Consolidation script that combines multiple tax PDFs from brokerages into a single CSV, detailing all relevant tax information (such as proceeds, costs, gains, interest earned, etc.). 
   - The script also offers data analysis and visualization for your 1099 tax returns. 
   - Useful for people with multiple accounts. Most accountants charge anywhere from $50-$100/per tax document; so the hope is it will help people save big. The program comes with a CSV/PDF viewer, which makes it easy to verify accuracy. 
   - Stay tuned for its release, which will be available for purchase soon.
- **[Referral-Link-Me](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md):** Maximize your rewards with curated referral links for credit cards, brokerages, and more. 

## Speed Considerations:
- Adjust `SET_SPEED` env to control test execution pace on faster computers.
- Opt for 'Reference' over 'Log' in Selenium IDE for faster execution.
- Activate 'Best performance' mode in Laptop Battery settings to accelerate execution.
- Keep the browser's automation tab as the focused window for potential speed enhancements.
<details>
  <summary>🎯 Stream Deck</summary>
  
  <p>This part of the README might be extremely specific to a subset of people, specifically those who own Elgato Stream Decks. This is how I have mine currently set up, which may or may not be helpful for others:</p>
  <img src="" alt="Stream Deck Setup">
  
  <table>
    <tr>
      <th>Action</th>
      <th>Type</th>
      <th>Command</th>
    </tr>
    <tr>
      <td>Run</td>
      <td>Hotkey</td>
      <td><code>Ctrl + R</code></td>
    </tr>
    <tr>
      <td>Stop</td>
      <td>Hotkey</td>
      <td><code>Ctrl + .</code></td>
    </tr>
    <tr>
      <td>Pause</td>
      <td>Hotkey</td>
      <td><code>Ctrl + P</code></td>
    </tr>
    <tr>
      <td>QuickStart</td>
      <td>Open</td>
      <td><code>cmd.exe /c ""C:\Users\Frost\Desktop\RSA-QuickStart.bat""</code></td>
    </tr>
    <tr>
      <td>Save</td>
      <td>Hotkey</td>
      <td><code>Ctrl + S</code></td>
    </tr>
    <tr>
      <td>Switch Windows</td>
      <td>Hotkey</td>
      <td><code>Alt + Tab</code></td>
    </tr>
    <tr>
      <td>Open Tests</td>
      <td>Hotkey</td>
      <td><code>Ctrl + 1</code></td>
    </tr>
    <tr>
      <td>Open Test Suites</td>
      <td>Hotkey</td>
      <td><code>Ctrl + 2</code></td>
    </tr>
    <tr>
      <td>Start Brave</td>
      <td>Powershell</td>
      <td><code>Start-Process "AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe" -ArgumentList "--new-window", "--app=chrome-extension://mooikfkahbdckldjjndioackbalphokd/index.html"</code></td>
    </tr>
    <tr>
      <td>Start Edge</td>
      <td>Powershell</td>
      <td><code>start msedge --app="chrome-extension://ajdpfmkffanmkhejnopjppegokpogffp/index.html"</code></td>
    </tr>
  </table>
</details>

## ⚠️ DISCLAIMER ⚠️
I am not a financial advisor, nor am I affiliated with any brokerage mentioned in this repository. 

You may use this tool at your own risk. I am not responsible for any financial loss, account restriction, or any other damage that may occur with the use of this tool. This project is provided "as is" and without warranty of any kind. 

By using this repository, the user accepts all the risks and agrees to hold the developer(s) harmless from any claims, damages, or losses arising from the use of the project. 
