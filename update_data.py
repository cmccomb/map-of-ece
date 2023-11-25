import json                         # for saving and parsing json files
from scholarly import scholarly     # for scraping data from Google Scholar
import pandas                       # for reading data


# List of faculty names and Google Scholar IDs
faculty_in_department = pandas.read_csv("faculty.csv").to_dict('records')

# Get publications for every faculty member
for faculty in faculty_in_department:
    if not pandas.isnull(faculty['id']):    # make sure there is an ID in the dict
        # Get and fill the info
        author = scholarly.fill(scholarly.search_author_id(faculty['id']))
        # Extract publications
        faculty_pubs = [publication['bib'] for publication in author['publications']]
        # Save to JSON
        with open('data/' + faculty['name'] + '.json', 'w', encoding='utf-8') as f:
            json.dump(sorted(faculty_pubs, key=lambda x: x['title']), f, ensure_ascii=False, indent=4)

