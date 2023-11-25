import json                     # for saving and parsing json files
from scholarly import scholarly # google scholar
import sys                      # for testing


# List of faculty names and google scholar IDs
faculty_in_department: list[tuple[str, str]] = [
    ("Farimani",            "aH52nxkAAAAJ"),
    ("Bedillion",           "UIS_G1YAAAAJ"),
    ("Bergbreiter",         "SU0c5P0AAAAJ"),
    ("Beuth",               None),
    ("Bolmin",              "YM2HSekAAAAJ"),
    ("Cagan",               "VtINcewAAAAJ"),
    ("de Boer",             "P1OWCkAAAAAJ"),
    ("Gomez",               None),
    ("Grande Gutiérrez",    "HzsuNvEAAAAJ"),
    ("Haidar",              None),
    ("Halilaj",             "Fr9Vhe4AAAAJ"),
    ("Jayan",               "NNSeBe4AAAAJ"),
    ("Johnson",             "GN5Mc3UAAAAJ"),
    ("Jones",               "xnyNe2EAAAAJ"),
    ("Kang",                "jcgAPTYAAAAJ"),
    ("Kara",                "_X2eOeQAAAAJ"),
    ("LeDuc",               "sLEB9iYAAAAJ"),
    ("Litster",             "7zUqi1sAAAAJ"),
    ("Majidi",              "1LyndUsAAAAJ"),
    ("Malen",               "U8r6ir4AAAAJ"),
    ("McComb",              "0P9w_S0AAAAJ"),
    ("McGaughey",           "HmNtygkAAAAJ"),
    ("Michalek",            "92jyX2EAAAAJ"),
    ("Narra",               "LxF27NYAAAAJ"),
    ("Ozdoganlar",          "F3UFKWMAAAAJ"),
    ("Panat",               "y1-WJhYAAAAJ"),
    ("Presto",              "4iYpwt8AAAAJ"),
    ("Quinn",               "2b0ZjdsAAAAJ"),
    ("Rabin",               "INTSXtcAAAAJ"),
    ("Shen",                "9KtTt28AAAAJ"),
    ("Shimada",             "pgcK25AAAAAJ"),
    ("Singh",               "lViJAdQAAAAJ"),
    ("Steif",               "NVHAIw4AAAAJ"),
    ("Sullivan",            "wXSgFr4AAAAJ"),
    ("Taylor",              "eDzzGUQAAAAJ"),
    ("Tucker",              "8N6uFIkAAAAJ"),
    ("Weber",               "7iFu3a4AAAAJ"),
    ("Webster-Wood",        "jW3whJYAAAAJ"),
    ("Whitefoot",           "3W2VK5sAAAAJ"),
    ("Zhang",               "dzHYBKcAAAAJ"),
    ("Zhao",                "z7tPc9IAAAAJ"),
]


# Function to save publications from Google Scholar
def save_publications_to_json(faculty: tuple[str, str]) -> None:
    name, google_scholar_id = faculty
    print(name)
    if google_scholar_id:
        author = scholarly.fill(scholarly.search_author_id(google_scholar_id))
        faculty_pubs = [publication['bib'] for publication in author['publications']]
        with open('data/' + name + '.json', 'w', encoding='utf-8') as f:
            json.dump(faculty_pubs, f, ensure_ascii=False, indent=4)


# get teh publications for every faculty member
number_of_faculty: int = len(faculty_in_department) if len(sys.argv) == 1 else int(sys.argv[1])
for faculty_tuple in faculty_in_department[:number_of_faculty]:
    save_publications_to_json(faculty_tuple)
