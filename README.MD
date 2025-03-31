# CSVExpenseTracker

CSVExpenseTracker automates the process of tracking monthly expenses using **Google Spreadsheets**. It allows for:
- **Automatic categorization** of expenses based on keywords (categories & subcategories).
- **Exclusion of certain expenses** based on keywords.

>[!NOTE]
>Currently, only **N26** and **PayPal** parsers are implemented.
>(See: [How to correctly export PayPal logs](#-how-to-export-paypal-logs-correctly))

---
## 🚀 Installation
### 1️⃣ Install Required Libraries
First, install the necessary Python libraries:
```sh
pip install gspread google-auth
```

### 2️⃣ Google API Configuration
To enable Google Sheets integration, you need to set up API access:

#### Step 1: Create a Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/apis).
2. Create a new project (`Select a Project` → `New Project`).
3. Give it a name and click **Create**.

#### Step 2: Enable Google Sheets & Drive APIs
1. In the left menu, navigate to **API & Services > Library**.
2. Search for **Google Sheets API**, click **Enable**.
3. Repeat the process for **Google Drive API** (needed for file access).

#### Step 3: Create Credentials
1. Go to **API & Services > Credentials**.
2. Click **Create Credentials > Service Account**.
3. Enter a name for the account, then click **Create and Continue**.
4. Assign the **Editor** role (or **Owner** for full access), then click **Continue > Done**.
5. Under "Service Accounts," click on the newly created account.
6. Go to the **Keys** tab and click **Add Key > JSON**.
7. Download the `.json` file and save it in the **/config** directory of the project.

#### Step 4: Share the Google Sheet with the Service Account
1. Open your **Google Spreadsheet**.
2. Click **Share** (top-right corner).
3. Copy the service account email from the JSON file (`name@project.iam.gserviceaccount.com`).
4. Paste it into the sharing field and grant **Editor** access.
5. Click **Send**.

>[!NOTE]
>A template spreadsheet is available here: [Google Sheets Template](https://docs.google.com/spreadsheets/d/1uwWi78mgVENbNoc8REMdLWvAdgcTZm4_h78E1VNSqWk/edit?usp=sharing)

>[!IMPORTANT] 
>*Do NOT request access to the template file. Instead, copy it to your own Google Drive:*
>- Click **File > Make a Copy**

---
## 🔧 Software Configuration
All configuration files are located in the `/config` directory.

### 🔹 `config.py`
- Configure the input file names, Google API key file, spreadsheet name, and worksheet.

### 🔹 `paypal_category.csv` & `n26_category.csv`
- Define **keywords** and their corresponding **categories** for automatic assignment.
- Format: `keyword, category, subcategory`
- (Default files include example configurations.)

### 🔹 `paypal_blacklist.csv` & `n26_blacklist.csv`
- Define **keywords** that should be ignored if found in the sender or transaction message.
- ⚠️ The **N26 blacklist** excludes `PayPal` by default to prevent **double spending** issues.

### 🔹 Uploading CSV Files
- Place the CSV files to be parsed in the `/input` directory before running the script.

---
## ▶️ Running the Script
Once everything is configured, run the script:
```sh
python3 main.py
```

---
## 📌 How to Export PayPal Logs Correctly
To properly export PayPal logs:
1. Go to: [PayPal Reports](https://www.paypal.com/reports/dlog)
2. Set:
   - **Transaction Type** → `Affects Balance`
   - **Format** → `CSV`
   - Choose the date range.
3. Click **Create Report**.

---

✅ Your expense tracker is now set up! 🎉 Happy budgeting!

