# Helper Scripts

This folder contains essential sub-scripts to facilitate your project tasks.

## merge-tax-pdfs .py

This script streamlines the management of numerous Tax Forms/PDFs. By specifying the exact page numbers containing the required data, you can filter and consolidate them into a single PDF for simplified tax processing by either yourself or your accountant.

### Usage:

```bash
cd src\Helper-Scripts
pip install -r requirements.txt
python merge-tax-pdfs.py C:\Users\Premium\TaxForms\Vanguard Vanguard-Combined.pdf 3 4
```
In this example, the script traverses through PDFs within the Vanguard folder, extracts pages 3 and 4 from each PDF, and compiles them into a new file named Vanguard-Combined.pdf.

Structure:
```bash
python merge-tax-pdfs.py input_folder output.pdf 1 3 5
```

## Fidelity_Account_Array.js

This script is designed to be executed within your browser's console to swiftly retrieve your Fidelity account numbers.

### Instructions:

1. Open Fidelity Portfolio.
2. Run this Script in the Console.
3. Copy the generated Array.
4. Paste it into the Fidelity environment variable in the `.env` file.

## SoFi_Account_Array.js

Similar to `Fidelity_Account_Array.js`, this script facilitates the gathering of account information for Sofi.

### Instructions:

1. Log in to Sofi's Invest Homepage on your browser.
2. Execute this script in the console.
