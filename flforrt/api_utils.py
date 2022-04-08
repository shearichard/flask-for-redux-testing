import csv
import uuid

MOVIE_INPUT_FIELD_NAMES = ['film', 'genre', 'lead_studio', 'audience_score_percent', 'profitability', 'rotten_tomatoes_percent', 'worldwide_gross_usd', 'year']

def initialize_movies():
    dicout = {}
    with open('movies.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=MOVIE_INPUT_FIELD_NAMES)
        #
        for row in reader:
            slug = str(uuid.uuid4())[:8]
            dicout[slug] = row
            dicout[slug]['worldwide_gross_usd'] = dicout[slug]['worldwide_gross_usd'].replace("$","")

    #
    return dicout

