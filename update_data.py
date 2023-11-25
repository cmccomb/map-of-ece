import json                         # for saving and parsing json files
from scholarly import scholarly     # for scraping data from Google Scholar
import pandas                       # for reading data


# Function to save publications from Google Scholar
def save_publications_to_json(faculty: dict) -> None:
    name = faculty['name']
    google_scholar_id = faculty['id']
    if not pandas.isnull(google_scholar_id):
        author = scholarly.fill(scholarly.search_author_id(google_scholar_id))
        faculty_pubs = [publication['bib'] for publication in author['publications']]
        with open('data/' + name + '.json', 'w', encoding='utf-8') as f:
            json.dump(sorted(faculty_pubs, key=lambda x: x['title']), f, ensure_ascii=False, indent=4)


# List of faculty names and Google Scholar IDs
faculty_in_department = pandas.read_csv("faculty.csv").to_dict('records')

# Get publications for every faculty member
for faculty_dict in faculty_in_department:
    print(faculty_dict)
    save_publications_to_json(faculty_dict)
