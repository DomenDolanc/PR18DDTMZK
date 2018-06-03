# with open('G:/Moj disk/2. letnik/[PR] Podatkovno Rudarjenje/PR18DDTMZK/data/movies_metadata.txt', 'r') as file:
import json

header = True
for row in open('G:/Moj disk/2. letnik/[PR] Podatkovno Rudarjenje/PR18DDTMZK/data/movies_metadata.txt', 'r', encoding="utf8"):
    if header:
        header = False
        continue
    row = row.strip().split('\t')
    if len(row) < 24:
        continue
    genres = row[3].replace("'", '"')
    print(row)
    try:
        for genre in json.loads(genres):
            print(genre)

    except:
        pass

# a = '[{"a":"b"},{"a":"c"}]'
# b = json.loads(a)
# print(b[0])
