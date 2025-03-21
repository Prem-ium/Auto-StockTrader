<h1 align="center"> ⚙️ Auto Stock Trader 💵 </h1>

<p align="center">An <i>awesome</i> repository containing scripts and projects for automating stock orders across multiple brokerages.</p>

<p align="right"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/><a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="Github Sponsor"/></a></p>
<p align="center">
    <img src="https://github.com/Prem-ium/Auto-StockTrader/blob/main/.github/assets/Auto-StockTrader-Banner.jpeg?raw=true" alt="Auto Stock Trader Banner">
</p>

---
## Features 🚀

- **Multi-Ticker Support**: Trade multiple stock tickers like `NVDA, TSLA, AAPL` all in one swift test run! 📈
- **Multi-Account Login**: Effortlessly manage and trade across multiple accounts with seamless login automation 🔑
- **Smart Error Handling**: Dynamic error checking & handling with XPATHs ensures your trades run smoothly and without hiccups ⚙️
- **Account Slicing**: Want to focus on specific accounts? Automate starting from a particular account and beyond! 🎯
- **Extended Trading Hours**: Take advantage of extended hours for supported brokerages and never miss out on prime trading opportunities ⏰
- **Limit Order Support**: Set precise limit orders with select brokerages to stay in control of your trades! 📊
- **1-Click Updates**: Update `.side` files with new tickers, account variables, and more in a single click using `.sh` or ' `.bat` script! 🔄
- **JavaScript Helper Scripts**: Boost efficiency with easy-to-use JavaScript helper scripts for managing account arrays 💻

---
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
- Robinhood (Gold Sponsor Only)
- WellsTrade (Gold Sponsor Only)

---
## 🚀 Unlock Premium Features w/ Gold Sponsorship! 🌟
Gold Sponsors gain **exclusive access** to advanced, fully optimized features that streamline and automate brokerage management. Here’s a sneak peek at what you’ll receive with Gold Sponsorship:

#### 🌟 **Optimized Python & Selenium Scripts**
- **Completely reworked** for maximum efficiency, making them faster and easier to use.
- Unlike public versions, which require more configuration, the Gold version is **seamless** and **user-friendly**.

#### ⚡ **Up-to-Date & Faster Automation**
- Access the latest brokerage automation updates and improvements.
- Bug fixes, optimizations, and faster execution are guaranteed with the private version, unlike the public version, which may not be updated frequently.

#### 💰 **Exclusive Tools**
- **Automated Cash Transfer/Withdrawal Tool** to consolidate funds from multiple accounts.
- **Exclusive Robinhood and WellsTrade automation support** available only to Gold Sponsors.
- **Exclusive Features**: Automated limit pricing and account retrieval. Brokerages are dynamically consolidated within a single MASTER file containing all automation test suites. Additional command line arguments, environmental variables, etc., are available for enhanced customization. 

**Ready to upgrade?**  

[Become a Gold Sponsor **here** and unlock these exclusive benefits!](https://github.com/sponsors/Prem-ium/sponsorships?sponsor=Prem-ium&tier_id=308205&preview=false) 
[![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)



---
## Environmental Variables 🔧
To use this project, you will need to set the following environment variables in your `.env` file:

| Variable             | Description                                                                                                            | Type                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| `SCHWAB_AI`           | Total number of Schwab accounts                                                                                         | Integer                     |
| `MERRILL_AI`          | Total number of Merrill accounts                                                                                        | Integer                     |
| `VANGUARD_AI`         | Total number of Vanguard accounts                                                                                       | Integer                     |
| `FIDELITY_AI`         | Fidelity account numbers                                                                                               | Nested List of Strings      |
| `CHASE_AI`            | [List of AI values in Trade URL](https://github.com/Prem-ium/Auto-StockTrader/blob/main/src/README.MD#chase-automatio)   | Nested List of Strings      |
| `FIRSTRADE_AI`        | Firstrade account numbers                                                                                                | List of Strings             |
| `ALLY_AI`             | Ally account numbers.                                                                                                    | List of Strings             |
| `CUSTOM_DIR`          | Path to the folder to store updated `.side` files                                                                         | String                      |
| `DYNAMIC`             | Enable dynamic account length feature (0 = Off, 1 = On)                                                                 | Integer                     |
| `SOFI_AI`             | List of account numbers for Sofi Helper Auto.side                                                                         | List of Strings             |

As a reminder, if you are a Gold Sponsor, please refer to the private `sponsors` repository README instead of this public version. The sponsor version includes more features and customization options tailored specifically for your needs.
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

---
## Installation ⚙️

Follow these steps to set up and use Selenium IDE for automation:

1. **Download Selenium IDE:**
   - Install the Selenium IDE browser extension for your preferred browser from the add-on store. For the most reliable automation runs, it is recommend to use a Chromium browser. Avoid using Firefox if possible.
     - [Chrome Web Store Selenium IDE Page](https://chrome.google.com/webstore/detail/selenium-ide/mooikfkahbdckldjjndioackbalphokd)
     - [Edge Add-on Selenium IDE Page](https://microsoftedge.microsoft.com/addons/detail/selenium-ide/ajdpfmkffanmkhejnopjppegokpogffp)
     Note: Due to recent changes, Selenium IDE extension might be unavailable in the browser extension store. You can manually import the extension using the provided `.crx` file located in the `src`-> `Selenium_IDE` folder of this project. Go to manage extensions on your browser, enable developer mode, and drag the `Selenium-IDE.crx` file into the window.

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

---
## Donations ❤️

I've been diligently working on this project for several months, and I'm thrilled with the progress it has made. Based on user testimonials, it has proven to be an invaluable tool for automating stock ticker orders across multiple brokerage accounts and various brokerages. I am continually striving to enhance its functionality and optimize its efficiency for automated order execution.

If you appreciate my work and would like to show your support, there are two convenient ways to make a donation:

1. **GitHub Sponsors**
   - [Donate via GitHub Sponsors](https://github.com/sponsors/Prem-ium)
   - Preferred because this donation method is fee-free and offers perks for your contribution.
   - [![GitHub Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)](https://github.com/sponsors/Prem-ium)

2. **Buy Me A Coffee**
   - [Donate via Buy Me A Coffee](https://www.buymeacoffee.com/prem.ium)
   - [![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/prem.ium)
3. **Referral Links**  
   - If you're unable to make a monetary donation, you can still support my work by using my curated [Referral Links](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md). Earn bonuses and rewards while contributing to my projects at the same time.  
   - [Explore Referral Links](https://github.com/Prem-ium/Referral-Link-Me/blob/main/README.md)  

Your generous donations will go a long way in helping me cover the expenses associated with developing new features and promoting the project to a wider audience. I extend my heartfelt gratitude to all those who have already contributed. Thank you for your support!

---
## Experiencing Issues? 🛠️
I'm not available to respond to issues in this repository. For direct support, please consider sponsoring me below under the `Silver` or `Gold` tier. Keep in mind that the public version is mostly "as built" and is rarely updated, while the private Gold Sponsor version receives regular updates and support.
[![Sponsor](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white)](https://github.com/sponsors/Prem-ium)

---
<details>
        <summary>Pull Request Requirements 📋</summary>
To ensure a smooth review process, please follow these guidelines when submitting a pull request (PR):

1. **Title**: Provide a clear and concise title.
2. **Description**: Include a detailed description of changes, problems addressed, and any relevant context.
3. **Documentation**: If necessary, update comments, README, requirements, and any relevant documentation.
4. **License Compliance**: Ensure any changes made in forks uphold the [repository's license](https://github.com/Prem-ium/Auto-StockTrader/blob/main/LICENSE). Do not make changes to certain areas such as the `FUNDING.yml` or any present copyright information without approval.

Once you have verified that your changes adhere to these guidelines, please open a pull request with your changes and click 'Request Review' on the Pull Request.

By adhering to these guidelines, you help maintain the quality and consistency of the project. Thank you for your interest in making contributions!
</details>

---
## License
This repository follows the [BSD 3-Clause “New” or “Revised” License.](https://github.com/Prem-ium/Auto-StockTrader/blob/main/LICENSE)

---
## Acknowledgments / Final Remarks 💬

I sincerely thank [my sponsors](https://github.com/sponsors/Prem-ium), [donors](https://www.buymeacoffee.com/prem.ium), and [project contributors](https://github.com/Prem-ium/Auto-StockTrader/graphs/contributors). Your support is invaluable, allowing me to continue creating exciting projects like this. Each one of you plays a crucial role, and I am deeply grateful for your contributions. If you find this project valuable, please consider leaving a :star2:, [donating](https://github.com/sponsors/Prem-ium), or [contributing](https://github.com/Prem-ium/Auto-StockTrader/graphs/contributors).

### Other Projects

- **TaxMerge – 1099 Tax Document Consolidator:**  
  I’ve developed a 1099 Tax Consolidation script that merges multiple tax PDFs from various brokerages into a single CSV, summarizing all the important tax information (proceeds, costs, gains, interest earned, etc.).  
  - Includes **data analysis** and **visualization** features for easy review of your 1099 tax returns.  
  - Perfect for individuals with multiple brokerage accounts, helping them avoid paying the usual tax document fees (typically $50-$100 per document).  
  - Comes with a **CSV/PDF viewer** to cross-check and ensure accuracy.  
  - **Available now for purchase**! Check it out on [GitHub](https://github.com/Prem-ium/Tax-Merge).<details open><summary>🎥 Demo Video</summary>Check out the demo video below to see how it works:<video src="https://github.com/user-attachments/assets/d87c5c93-c09c-4c41-a1c3-a0d248784b95" controls="controls" style="max-width: 100%; height: auto;">Your browser does not support video tags.<a href="https://github.com/user-attachments/assets/d87c5c93-c09c-4c41-a1c3-a0d248784b95">View the video</a></video></details>

### Speed Considerations:

- Adjust the `SET_SPEED` environment variable to control test execution speed on faster computers.
- Use 'Reference' instead of 'Log' in Selenium IDE for faster performance.
- Enable 'Best performance' mode in Laptop Battery settings to boost execution speed.
- Keep the browser’s automation tab focused for potential speed enhancements.

<details>
  <summary>🎯 Stream Deck</summary>
  
  <p>For those with an Elgato Stream Deck, here’s my current setup:</p>
  <img src="https://github.com/user-attachments/assets/ea4f71a8-183f-402a-91e5-2c1c5f7b3e3b" alt="Stream Deck Setup">
  
  <table>
    <tr><th>Action</th><th>Type</th><th>Command</th></tr>
    <tr><td>Run</td><td>Hotkey</td><td><code>Ctrl + R</code></td></tr>
    <tr><td>Stop</td><td>Hotkey</td><td><code>Ctrl + .</code></td></tr>
    <tr><td>Pause</td><td>Hotkey</td><td><code>Ctrl + P</code></td></tr>
    <tr><td>QuickStart</td><td>Open</td><td><code>cmd.exe /c ""C:\Users\Frost\Desktop\RSA-QuickStart.bat""</code></td></tr>
    <tr><td>Save</td><td>Hotkey</td><td><code>Ctrl + S</code></td></tr>
    <tr><td>Switch Windows</td><td>Hotkey</td><td><code>Alt + Tab</code></td></tr>
    <tr><td>Open Tests</td><td>Hotkey</td><td><code>Ctrl + 1</code></td></tr>
    <tr><td>Open Test Suites</td><td>Hotkey</td><td><code>Ctrl + 2</code></td></tr>
    <tr><td>Start Brave</td><td>Powershell</td><td><code>Start-Process "AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe" -ArgumentList "--new-window", "--app=chrome-extension://mooikfkahbdckldjjndioackbalphokd/index.html"</code></td></tr>
    <tr><td>Start Edge</td><td>Powershell</td><td><code>start msedge --app="chrome-extension://ajdpfmkffanmkhejnopjppegokpogffp/index.html"</code></td></tr>
  </table>
  <hr>
</details>


### ⚠️ DISCLAIMER ⚠️
- I am not a financial advisor, nor am I affiliated with any brokerage mentioned in this repository. 
- You may use this tool at your own risk. I am not responsible for any financial loss, account restriction, or any other damage that may occur with the use of this tool. This project is provided "as is" and without warranty of any kind. 
- By using this repository, the user accepts all the risks and agrees to hold the developer(s) harmless from any claims, damages, or losses arising from the use of the project.
