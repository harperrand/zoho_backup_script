# zoho_backup_wizard
A script that leverages Selenium to download the Zoho CRM backup files autonomously. 

Pre-requisites:
- Python >= 3.6
- Google Chrome
- [Selenium Chromedriver](https://chromedriver.chromium.org/downloads) installed on your path
- Your `Zoho Org ID` and `Zoho Backup ID`. To obtain these, check one of the links of your current Zoho data backup.
The Zoho backup links will be in the form `https://download-accl.zoho.com/v2/crm/{Zoho Org ID}/backup/{Zoho Backup ID}/{ filename }.zip`

Usage:
- It is recommended that you use a virtual environment to install the necessary Python packages
- Inside your virtual environemt, run `pip install -r requirements.txt`
- Run `python main.py`
- Follow the prompts in the application to enter your username, password, Zoho Org ID, Zoho Backup ID, and the number of attachment files

Notes
- If two-factor authentication is enabled, you will still need to manually authenticate into Zoho once the script tries to log you in
- Google Chrome will limit your number of simultaneous downloads. If there are many attachment files, they will download automatically as other downloads are completed.
