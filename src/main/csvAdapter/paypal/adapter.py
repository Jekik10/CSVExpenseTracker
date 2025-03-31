from .paypal_controller import *

def adapter(filename, keyword_blacklist, keyword_category_map):
    entries = read_from_csv(filename)
    entries = filter_columns(entries)
    for keyword in keyword_blacklist:
        entries = remove_entry_by_keyword(entries, keyword)
    entries = set_category(entries, keyword_category_map)

    print("Completed PayPal adaptation...")
    return entries