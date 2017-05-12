import json
import sample

cli = sample.sample()
tempjson = {}
columns = []
options = []
columns.append({'key':'yield', 'full_name':'Yield', 'type':'numeric', 'goal':'max'})
columns.append({'key':'production', 'full_name':'Production', 'type':'numeric', 'goal':'max'})
columns.append({'key':'acres_harvested', 'full_name':'Acres Harvested', 'type':'numeric', 'goal':'max'})
columns.append({'key':'acres_planted', 'full_name':'Acres Planted', 'type':'numeric', 'goal':'max'})
tempjson.update({'subject': 'Plantaplan'})
tempjson.update({'columns': columns})
options.append(cli.analyze('MARICOPA', 'Barley'.upper()))
options.append(cli.analyze('PINAL', 'Barley'.upper()))
tempjson.update({'options': options})
print json.dumps(tempjson)