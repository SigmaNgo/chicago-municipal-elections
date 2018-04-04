import sys
import csv
import json

precincts = json.load(sys.stdin)
features = precincts['features']

field_names = list(features[0]['properties'].keys())

field_names.remove('WARD')
field_names.remove('PRECINCT')

field_names = ['WARD', 'PRECINCT'] + field_names

writer = csv.DictWriter(sys.stdout, fieldnames=field_names, dialect='unix')
writer.writeheader()
for feature in features:
    writer.writerow(feature['properties'])
