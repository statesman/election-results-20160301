import csv, sys, simplejson


def write_precinct_data(races, precinct, data):
  """
  Write the race data to the passed precinct data dict
  """
  try:
    sorted_races = sorted(races, key=lambda k: k['votes'], reverse=True)
    data[precinct] = {
      'races': sorted_races,
      'winner': sorted_races[0]
    }

    # Special handling for ties
    if (sorted_races[0]['votes'] == sorted_races[1]['votes']):
      data[precinct]['winner'] = {
        'candidate': 'Tie',
        'votes': '-',
        'party': 'TIE'
      }
  except IndexError:
    pass


# And walk the CSV
def build_race_file(target_races, filename):

  # Get the JSON files for Travis and Williamson and combine them
  combined = open('precincts/combined-simplified.geojson', 'r')
  text = combined.read()
  combined.close()
  geo = simplejson.loads(text)

  races = []
  current_precinct = None
  running_vote_total = 0
  precinct_data = {}

  # Loop through Travis results and add them to precinct data
  with open('results/travis-runoff.csv', 'rb') as input_file:

    # Open a reader for the input file
    results = csv.reader(input_file, delimiter=',')
    next(results, None)

    # Loop over the input, parse & write the new file
    for row in results:

      # Pull our data from the CSV columns
      precinct = row[0]
      candidate_name = row[1]
      total_votes = int(row[3])
      race = row[2]
      party = ''

      if race in target_races:

        if current_precinct != precinct and current_precinct != None:
          if running_vote_total > 0:
            write_precinct_data(races, current_precinct, precinct_data)

          races = []
          running_vote_total = 0

        races.append({
          'candidate': candidate_name,
          'votes': total_votes,
          'party': party
        })

        current_precinct = precinct

        # Keep a running vote total to calculate the percentage down the road
        running_vote_total = running_vote_total + total_votes

    # Write the last row
    write_precinct_data(races, current_precinct, precinct_data)

  to_thin = []
  for i, feature in enumerate(geo['features']):
    precinct = feature['properties']['PCT']

    old_props = feature['properties']
    del feature['properties']

    try:
      feature['properties'] = dict(old_props.items() + precinct_data[precinct].items())
    except KeyError:
      to_thin.append(i)
      pass

  for feature in to_thin[::-1]:
    geo['features'].pop(feature)

  json_out = open('race-data/' + filename + '.json', 'w')
  json_out.write(simplejson.dumps(geo))
  json_out.close()

build_race_file(["MAYOR, CITY OF AUSTIN", "Mayor, City of Austin"], 'mayor-runoff')
build_race_file(["DISTRICT 1, AUSTIN CITY COUNCIL, CITY OF AUSTIN"], 'council-d1-runoff')
build_race_file(["DISTRICT 3, AUSTIN CITY COUNCIL, CITY OF AUSTIN"], 'council-d3-runoff')
build_race_file(["DISTRICT 4, AUSTIN CITY COUNCIL, CITY OF AUSTIN"], 'council-d4-runoff')
build_race_file(["DISTRICT 6, AUSTIN CITY COUNCIL, CITY OF AUSTIN"], 'council-d6-runoff')
build_race_file(["DISTRICT 7, AUSTIN CITY COUNCIL, CITY OF AUSTIN"], 'council-d7-runoff')
build_race_file(["DISTRICT 8, AUSTIN CITY COUNCIL, CITY OF AUSTIN"], 'council-d8-runoff')
build_race_file(["DISTRICT 10, AUSTIN CITY COUNCIL, CITY OF AUSTIN"], 'council-d10-runoff')
