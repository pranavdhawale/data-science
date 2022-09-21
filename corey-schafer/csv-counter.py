import csv
from collections import Counter

with open("corey-schafer/data.csv") as csv_file:
    
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(";"))

# prints count of every language
print(language_counter)

# prints count of top n languages
print(language_counter.most_common(15))

languages = []
popularity = []

# makes separate list of languages and popularity
for items in language_counter.most_common(15):
    languages.append(items[0])
    popularity.append(items[1])

print(languages)
print(popularity)