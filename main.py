#   BSD 3-Clause License
#   
#   Copyright (c) 2023-Present, Prem Patel
#   
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#   
#   1. Redistributions of source code must retain the above copyright notice, this
#      list of conditions and the following disclaimer.
#   
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   
#   3. Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#   
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#   FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#   DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#   CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#   OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import json
import sys
import argparse
import shutil
import traceback
import subprocess

from dotenv import load_dotenv

load_dotenv()
parser = argparse.ArgumentParser(description="Process stock trading arguments.")
parser.add_argument("tickers", nargs='?', default="JOB", help="Tickers to process")

args = parser.parse_args()

def main():
    TICKERS = args.tickers.upper()
    if "," in TICKERS:  print(f"{'-'*100}\nTICKERS passed:\t{TICKERS}\n{'-'*40}")

    file_task_map = {
        "CHASE_AI": {"file": os.path.join("src", "Selenium_IDE", "Chase_Auto.side"), "task": ""},
        "FIRSTRADE_AI": {"file": os.path.join("src", "Selenium_IDE", "Firstrade_Auto.side"), "task": ""},
        "VANGUARD_AI": {"file": os.path.join("src", "Selenium_IDE", "Vanguard_Auto.side"), "task": ""},
        "FIDELITY_AI": {"file": os.path.join("src", "Selenium_IDE", "Fidelity_Auto.side"), "task": ""},
        "SCHWAB_AI": {"file": os.path.join("src", "Selenium_IDE", "Schwab_Auto.side"), "task": ""},
        "SOFI_AI":  {"file": os.path.join("src","Selenium_IDE","Sofi Helper.side"),     "task": ""},
        "ALLY_AI": {"file": os.path.join("src", "Selenium_IDE", "Ally_Auto.side"), "task": ""},
        "MERRILL_AI": {"file": os.path.join("src", "Selenium_IDE", "Merrill_Auto.side"), "task": ""},
    }
    custom_dir = os.environ.get("CUSTOM_DIR", os.path.join(os.path.expanduser('~'), 'Desktop', 'AutoStockTrader'))
    os.makedirs(custom_dir, exist_ok=True)

    files = []
    logins = []
    result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
    if 'Your local changes to the following files would be overwritten by merge' in result.stderr:
        subprocess.run(['git', 'reset', '--hard'], check=True)
        result = subprocess.run(['git', 'pull'], capture_output=False, text=False)
    if custom_dir:
        dest_path = os.path.join(custom_dir, "Account_Management_Tools.side")
        try:    shutil.copyfile(os.path.join("src", "Selenium_IDE", "Account_Management_Tools.side"), dest_path)
        except  shutil.SameFileError:    pass
    print('-'*105)
    for var_name, info in file_task_map.items():
        if os.environ.get(var_name):
            files.append(info["file"])
            print(f"{var_name} is enabled.")

            if var_name == "SCHWAB_AI":
                info["task"] = "Array.from({length: " + os.environ[var_name] + "}, (_, i) => i);"
            elif var_name == "MERRILL_AI" or var_name == "VANGUARD_AI":
                info["task"] = "Array.from({length: " +os.environ[var_name] + "}, (_, i) => i + 1);"
            else:
                info["task"] = os.environ[var_name].replace(" ", "")

            try:
                logins.append(os.environ[var_name.split("_")[0] + "_LOGIN"])
            except:
                logins.append("LOGIN:HERE")
        else:
            print(f"{var_name} is disabled. Skipping...")
    
    print(f'\n{"-"*105}\n')
    for filePath in files:
        task = ""
        for var_name, info in file_task_map.items():
            if info["file"].lower() in filePath.lower():
                task = info["task"]
                break

        # Load the JSON data
        with open(filePath, 'r') as file:
            data = json.load(file)

        for test in data['tests']:
            for command in test['commands']:
                # Store Login information, if provided
                if command['command'] == 'store' and 'LOGIN' in command['value']:
                    command['target'] = logins.pop(0)

                # Update Ticker, if provided
                if TICKERS is not None and command['value'] == 'TICKER':
                    command['target'] = f"return '{TICKERS}'" if command['command'] == 'executeScript' else TICKERS
                if command['command'] == 'store' and command['value'] == 'dynamic':
                    command['target'] = os.environ.get("DYNAMIC", 0)
                # Update the account number(s) and break to next test
                if command['command'] == 'executeScript' and command['value'] == 'accounts':
                    command['target'] = f"return {task}"
                    break

        if os.name == 'nt':
            filePath = filePath.replace("src\\Selenium_IDE\\", "")
            filePath = filePath.replace("src\\X_Archive\\", "")
            filePath = f'{custom_dir}/{filePath}' if custom_dir else f'ENV-{filePath}'
        elif os.name == 'posix':
            filePath = os.path.join("src", "Selenium_IDE", filePath.replace("src/Selenium_IDE/", ""))
            filePath = os.path.join("src", "X_Archive", filePath.replace("src/X_Archive/", ""))
            filePath = os.path.join(custom_dir, filePath) if custom_dir else f'ENV-{filePath}'

        # Create a new file with the updated data
        with open(filePath, 'w') as file:
            json.dump(data, file, indent=2)

        print(f"Created/Updated:\t{filePath}!")

    if custom_dir and len(sys.argv) != 2:
        os.startfile(custom_dir)

    try:
        directory = os.path.dirname(os.path.abspath(__file__))
        is_windows = os.name == 'nt'
        desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'RSA-QuickStart.bat') if is_windows else os.path.join(os.path.expanduser('~'), 'Desktop', 'RSA-QuickStart.sh')
        source_path = os.path.join(directory, 'src', 'Helper_Scripts', 'RSA-QuickStart.bat') if is_windows else os.path.join(directory, 'src', 'Helper_Scripts', 'RSA-QuickStart.sh')

        shutil.copyfile(source_path, desktop_path)
        print(f"Created/Updated:\t{desktop_path}")

        with open(desktop_path, 'r') as file:
            content = file.read()
            content = content.replace('set directory=', f'set directory={directory}') if is_windows else content.replace('export DIRECTORY=', f'export DIRECTORY={directory}')
        with open(desktop_path, 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print(f'Encountered File Not Found Error: {traceback.format_exc()}\n')
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()
        return

    
if __name__ == "__main__":
    print(f"""
=========================================================================================================
                        Script Execution Starting...
---------------------------------------------------------------------------------------------------------
                Free Public Version - Limited Features/Support
                            (C) Prem-ium
---------------------------------------------------------------------------------------------------------
Upgrading to Gold Sponsorship unlocks exclusive features, including:
- Faster, reliable Python/Selenium IDE scripts with consolidated brokerage automation.
- Seamless automation with automated limit prices and account retrieval.
- Exclusive setup and customization options via .env and command line arguments.
- Automated cash transfer/withdrawal tools for Fidelity, Chase, and more.
- WellsTrade & Robinhood automation support.

Join: https://github.com/login?return_to=%2Fsponsors%2FPrem-ium%2Fsponsorships%3Ftier_id%3D308205

---------------------------------------------------------------------------------------------------------
Related: Check out my new project, TaxMerge. A powerful app that consolidates multiple 1099-PDF tax forms
into a single CSV file. This tool is designed to simplify the process of tax reporting for stock traders
with multiple brokerage accounts.
Check it out here: https://github.com/Prem-ium/Tax-Merge  
---------------------------------------------------------------------------------------------------------
Thank you for your support!
=========================================================================================================\n\n\n""")
    main()


