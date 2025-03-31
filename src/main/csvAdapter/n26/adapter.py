from .n26_controller import *

def adapter(filename, keyword_blacklist, keyword_category_map):
    entries = read_from_csv(filename)
    for keyword in keyword_blacklist:
        entries = remove_entry_by_keyword(entries, keyword)
    entries = edit_transfers(entries)
    entries = filter_columns(entries)
    entries = set_category(entries, keyword_category_map)

    print("Completed N26 adaptation...")
    return entries
