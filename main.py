import config
from src.utils.const import CONFIG_PATH, INPUT_PATH
#
from src.main.csvAdapter.n26 import adapter as n26adapter
from src.main.csvAdapter.paypal import adapter as paypaladapter
from src.main.csvAdapter.intesaSP import adapter as intesaSPadapter
from src.main.utils.category_reader import read_category
from src.main.utils.blacklist_reader import read_blacklist
from src.main.gspread.gspread_controller import writeOnSpreadsheet

def main():
    create_n26_adaptation()
    create_paypal_adaptation()
    create_intesaSP_adaptation()

def create_intesaSP_adaptation():
    keyword_category_map = read_category(CONFIG_PATH+""+config.INTESASP_CATEGORY_FILE)
    keyword_blacklist = read_blacklist(CONFIG_PATH+""+config.INTESASP_BLACKLIST_FILE)
    input_filename =  INPUT_PATH+""+config.INTESASP_INPUT_FILE
    entries = intesaSPadapter(input_filename, keyword_blacklist, keyword_category_map)
    writeOnSpreadsheet(CONFIG_PATH+""+config.CREDENTIALS_FILE, config.SHEET_NAME, config.WORKSHEET, entries, "intesaSP")

def create_n26_adaptation():
    keyword_category_map = read_category(CONFIG_PATH+""+config.N26_CATEGORY_FILE)
    keyword_blacklist = read_blacklist(CONFIG_PATH+""+config.N26_BLACKLIST_FILE)
    input_filename =  INPUT_PATH+""+config.N26_INPUT_FILE
    entries = n26adapter(input_filename, keyword_blacklist, keyword_category_map)
    writeOnSpreadsheet(CONFIG_PATH+""+config.CREDENTIALS_FILE, config.SHEET_NAME, config.WORKSHEET, entries, "N26")

def create_paypal_adaptation():
    keyword_category_map = read_category(CONFIG_PATH+""+config.PAYPAL_CATEGORY_FILE)
    keyword_blacklist = read_blacklist(CONFIG_PATH+""+config.PAYPAL_BLACKLIST_FILE)
    input_filename = INPUT_PATH+""+config.PAYPAL_INPUT_FILE

    entries = paypaladapter(input_filename, keyword_blacklist, keyword_category_map)
    writeOnSpreadsheet(CONFIG_PATH+""+config.CREDENTIALS_FILE, config.SHEET_NAME, config.WORKSHEET, entries, "Paypal")
    

if __name__=="__main__":
    main()
