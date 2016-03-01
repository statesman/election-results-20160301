import csv, sys, simplejson

def is_in_county(p):
  """
  Check if the precinct number has a letter prefix, which would mean it's
  from another county.
  """
  try:
    float(p[0:1])
    return True
  except ValueError:
    return False


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

  # Get the JSON files for Travis and combine them (willimson edited out)
  combined = open('precincts/combined-simplified.geojson', 'r')
  text = combined.read()
  combined.close()
  geo = simplejson.loads(text)

  races = []
  current_precinct = None
  running_vote_total = 0
  precinct_data = {}

  # Loop through Travis results and add them to precinct data
  with open('results/travis.csv', 'rb') as input_file:

    # Open a reader for the input file
    results = csv.reader(input_file, delimiter=',')
    next(results, None)

    # Loop over the input, parse & write the new file
    for row in results:

      # Pull our data from the CSV columns
      precinct = row[0]
      in_county = is_in_county(precinct)
      candidate_name = row[2]
      total_votes = int(row[4])
      race = row[1]
      party = row[3]

      if race in target_races and in_county:

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

  # Loop through Williamson results and add them to precinct data
  with open('results/williamson.csv', 'rb') as input_file:

    # Open a reader for the input file
    results = csv.reader(input_file, delimiter=',')
    next(results, None)

    # Loop over the input, parse & write the new file
    for row in results:

      # Pull our data from the CSV columns
      precinct = "W" + str(row[0])
      race = row[1]
      candidate_name = row[2]
      party = row[3]
      if party == "NON":
        party = None
      total_votes = int(row[4])

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

  json_out = open('public/race-data/' + filename + '.json', 'w')
  json_out.write(simplejson.dumps(geo))
  json_out.close()

build_race_file(["PROP. 1, CONSTITUTIONAL AMENDMENT ELECTION"], 'ca-01')
build_race_file(["PROP. 2, CONSTITUTIONAL AMENDMENT ELECTION"], 'ca-02')
build_race_file(["PROP. 3, CONSTITUTIONAL AMENDMENT ELECTION"], 'ca-03')
build_race_file(["PROP. 4, CONSTITUTIONAL AMENDMENT ELECTION"], 'ca-04')
build_race_file(["PROP. 5, CONSTITUTIONAL AMENDMENT ELECTION"], 'ca-05')
build_race_file(["PROP. 6, CONSTITUTIONAL AMENDMENT ELECTION"], 'ca-06')
build_race_file(["PROP. 7, CONSTITUTIONAL AMENDMENT ELECTION"], 'ca-07')
build_race_file(["TRAVIS COUNTY BOND PROPOSITION, TRAVIS COUNTY BOND ELECTION"], 'tr-bond')
build_race_file(["COUNCIL MEMBER, PLACE 3, CITY OF PFLUGERVILLE"], 'pf-p3')
build_race_file(["COUNCIL MEMBER, PLACE 5, CITY OF PFLUGERVILLE"], 'pf-p5')
build_race_file(["PROP. 1, CITY OF PFLUGERVILLE"], 'pf-p01')
build_race_file(["PROP. 2, CITY OF PFLUGERVILLE"], 'pf-p02')
build_race_file(["PROPOSITION, VILLAGE OF WEBBERVILLE"], 'wb-p01')
build_race_file(["BOARD OF TRUSTEE, WESTBANK COMMUNITY LIBRARY DISTRICT"], 'wb-library')
build_race_file(["CITY COUNCIL, CITY OF SUNSET VALLEY"], 'sv-council')
build_race_file(["PROPOSITION 1, CITY OF SUNSET VALLEY"], 'sv-p01')
build_race_file(["MAYOR, CITY OF LAGO VISTA"], 'lv-mayor')
build_race_file(["COUNCIL MEMBER, PLACE 1, CITY OF LAGO VISTA"], 'lv-cc01')
build_race_file(["COUNCIL MEMBER, PLACE 3, CITY OF LAGO VISTA"], 'lv-cc03')
build_race_file(["COUNCIL MEMBER, PLACE 5, CITY OF LAGO VISTA"], 'lv-cc05')
build_race_file(["PROPOSITION 1, CITY OF LAGO VISTA"], 'lv-p01')
build_race_file(["PROPOSITION 2, CITY OF LAGO VISTA"], 'lv-p02')
build_race_file(["PROPOSITION 3, CITY OF LAGO VISTA"], 'lv-p03')
build_race_file(["PROPOSITION 4, CITY OF LAGO VISTA"], 'lv-p04')
build_race_file(["PROPOSITION 5, CITY OF LAGO VISTA"], 'lv-p05')
build_race_file(["PROPOSITION 6, CITY OF LAGO VISTA"], 'lv-p06')
build_race_file(["PROPOSITION 7, CITY OF LAGO VISTA"], 'lv-p07')
build_race_file(["PROPOSITION 8, CITY OF LAGO VISTA"], 'lv-p08')
build_race_file(["PROPOSITION 9, CITY OF LAGO VISTA"], 'lv-p09')
build_race_file(["MAYOR, CITY OF JONESTOWN"], 'j-mayor')
build_race_file(["ALDERMAN, PLACE 1, CITY OF JONESTOWN"], 'j-ap1')
build_race_file(["ALDERMAN, PLACE 2, CITY OF JONESTOWN"], 'j-ap2')
build_race_file(["PROP. 1, CITY OF CEDAR PARK"], 'cp-p01')
build_race_file(["PROP. 2, CITY OF CEDAR PARK"], 'cp-p02')
build_race_file(["PROP. 3, CITY OF CEDAR PARK"], 'cp-p03')
build_race_file(["PROP. 4, CITY OF CEDAR PARK"], 'cp-p04')
build_race_file(["MAYOR, VILLAGE OF POINT VENTURE"], 'pv-mayor')
build_race_file(["VILLAGE COUNCIL, VILLAGE OF VOLENTE"], 'v-council')
