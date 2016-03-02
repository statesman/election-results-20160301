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

build_race_file(["PRESIDENT - DEM"], 'p-d')
build_race_file(["DISTRICT 35, UNITED STATES REPRESENTATIVE - DEM"], 'usr35-d')
build_race_file(["RAILROAD COMMISSIONER - DEM"], 'rc-d')
build_race_file(["PLACE 3, JUSTICE, SUPREME COURT - DEM"], 'scj3-d')
build_race_file(["PLACE 5, JUSTICE, SUPREME COURT - DEM"], 'scj5-d')
build_race_file(["PLACE 9, JUSTICE, SUPREME COURT - DEM"], 'scj9-d')
build_race_file(["PLACE 2, JUDGE, COURT OF CRIMINAL APPEALS - DEM"], 'caj2-d')
build_race_file(["PLACE 5, JUDGE, COURT OF CRIMINAL APPEALS - DEM"], 'caj5-d')
build_race_file(["PLACE 6, JUDGE, COURT OF CRIMINAL APPEALS - DEM"], 'caj6-d')
build_race_file(["DISTRICT 5, MEMBER, STATE BOARD OF EDUCATION - DEM"], 'sboe5-d')
build_race_file(["DISTRICT 51, STATE REPRESENTATIVE - DEM"], 'sr51-d')
build_race_file(["DISTRICT JUDGE, 53RD JUDICIAL DISTRICT - DEM"], 'dj53-d')
build_race_file(["DISTRICT JUDGE, 98TH JUDICIAL DISTRICT - DEM"], 'dj98-d')
build_race_file(["DISTRICT JUDGE, 126TH JUDICIAL DISTRICT - DEM"], 'dj126-d')
build_race_file(["DISTRICT JUDGE, 167TH JUDICIAL DISTRICT - DEM"], 'dj167-d')
build_race_file(["DISTRICT JUDGE, 200TH JUDICIAL DISTRICT - DEM"], 'dj200-d')
build_race_file(["DISTRICT JUDGE, 345TH JUDICIAL DISTRICT - DEM"], 'dj345-d')
build_race_file(["DISTRICT JUDGE, 353RD JUDICIAL DISTRICT - DEM"], 'dj353-d')
build_race_file(["DISTRICT JUDGE, 390TH JUDICIAL DISTRICT - DEM"], 'dj390-d')
build_race_file(["DISTRICT JUDGE, 427TH JUDICIAL DISTRICT - DEM"], 'dj427-d')
build_race_file(["DISTRICT JUDGE, 450TH JUDICIAL DISTRICT - DEM"], 'dj450-d')
build_race_file(["DISTRICT ATTORNEY, 53RD JUDICIAL DISTRICT - DEM"], 'da53-d')
build_race_file(["JUDGE, COUNTY CRIMINAL COURT NO. 8 - DEM"], 'ccj8-d')
build_race_file(["JUDGE, COUNTY CRIMINAL COURT NO. 9 - DEM"], 'ccj9-d')
build_race_file(["COUNTY ATTORNEY - DEM"], 'ca-d')
build_race_file(["SHERIFF - DEM"], 's-d')
build_race_file(["TAX ASSESSOR-COLLECTOR - DEM"], 'tac-d')
build_race_file(["PRECINCT NO. 1, COUNTY COMMISSIONER - DEM"], 'cc1-d')
build_race_file(["PRECINCT NO. 1, CONSTABLE - DEM"], 'c1-d')
build_race_file(["COUNTY CHAIRMAN - DEM"], 'chair-d')
build_race_file(["REFERENDUM ITEM #1 - ON ECONOMIC SECURITY & PROSPERITY"], 'r1-d')
build_race_file(["REFERENDUM ITEM #2 - ON A FAIR CRIMINAL JUSTICE SYSTEM"], 'r2-d')
build_race_file(["REFERENDUM ITEM #3 - ON CLIMATE"], 'r3-d')
build_race_file(["REFERENDUM ITEM #4 - ON THE VOTING RIGHTS ACT"], 'r4-d')
build_race_file(["REFERENDUM ITEM #5 - ON CAMPUS CARRY"], 'r5-d')
build_race_file(["REFERENDUM ITEM #6 - ON COMPREHENSIVE IMMIGRATION REFORM"], 'r6-d')
build_race_file(["DISTRICT 17, UNITED STATES REPRESENTATIVE - DEM"], 'usr17-d')
build_race_file(["DISTRICT 10, MEMBER, STATE BOARD OF EDUCATION - DEM"], 'sboe10-d')
build_race_file(["DISTRICT 50, STATE REPRESENTATIVE - DEM"], 'sr50-d')
build_race_file(["DISTRICT 10, UNITED STATES REPRESENTATIVE - DEM"], 'usr10-d')
build_race_file(["PRECINCT NO. 2, CONSTABLE - DEM"], 'c2-d')
build_race_file(["DISTRICT 46, STATE REPRESENTATIVE - DEM"], 'sr46-d')
build_race_file(["PRECINCT NO. 4, CONSTABLE - DEM"], 'c4-d')
build_race_file(["DISTRICT 25, UNITED STATES REPRESENTATIVE - DEM"], 'usr25-d')
build_race_file(["PRECINCT 129, PRECINCT CHAIRMAN"], 'pc129')
build_race_file(["PRECINCT NO. 5, CONSTABLE - DEM"], 'c5-d')
build_race_file(["DISTRICT 21, STATE SENATOR - DEM"], 'ss21-d')
build_race_file(["DISTRICT 49, STATE REPRESENTATIVE - DEM"], 'sr49-d')
build_race_file(["DISTRICT 48, STATE REPRESENTATIVE - DEM"], 'sr48-d')
build_race_file(["PRECINCT NO. 3, CONSTABLE - DEM"], 'c3-d')
build_race_file(["DISTRICT 47, STATE REPRESENTATIVE - DEM"], 'sr47-d')
build_race_file(["DISTRICT 21, UNITED STATES REPRESENTATIVE - DEM"], 'usr21-d')
build_race_file(["PRECINCT NO. 3, COUNTY COMMISSIONER - DEM"], 'cc3-d')
build_race_file(["DISTRICT 24, STATE SENATOR - DEM"], 'ss24-d')
build_race_file(["PRECINCT 433, PRECINCT CHAIRMAN"], 'pc433')
build_race_file(["PRESIDENT - REP"], 'p-r')
build_race_file(["DISTRICT 35, UNITED STATES REPRESENTATIVE - REP"], 'usr35-r')
build_race_file(["RAILROAD COMMISSIONER - REP"], 'rc-r')
build_race_file(["PLACE 3, JUSTICE, SUPREME COURT - REP"], 'scj3-r')
build_race_file(["PLACE 5, JUSTICE, SUPREME COURT - REP"], 'scj5-r')
build_race_file(["PLACE 9, JUSTICE, SUPREME COURT - REP"], 'scj9-r')
build_race_file(["PLACE 2, JUDGE, COURT OF CRIMINAL APPEALS - REP"], 'caj2-r')
build_race_file(["PLACE 5, JUDGE, COURT OF CRIMINAL APPEALS - REP"], 'caj5-r')
build_race_file(["PLACE 6, JUDGE, COURT OF CRIMINAL APPEALS - REP"], 'caj6-r')
build_race_file(["DISTRICT 5, MEMBER, STATE BOARD OF EDUCATION - REP"], 'sboe5-r')
build_race_file(["PLACE 2, JUSTICE, 3RD COURT OF APPEALS DISTRICT - REP"], '3caj2-r')
build_race_file(["PLACE 4, JUSTICE, 3RD COURT OF APPEALS DISTRICT - REP"], '3caj4-r')
build_race_file(["DISTRICT JUDGE, 450TH JUDICIAL DISTRICT - REP"], 'dj450-r')
build_race_file(["DISTRICT ATTORNEY, 53RD JUDICIAL DISTRICT - REP"], 'da53-r')
build_race_file(["SHERIFF - REP"], 's-r')
build_race_file(["PRECINCT NO. 1, COUNTY COMMISSIONER - REP"], 'cc1-r')
build_race_file(["COUNTY CHAIRMAN - REP"], 'chair-r')
build_race_file(["PROPOSITION 1"], 'p1-r')
build_race_file(["PROPOSITION 2"], 'p2-r')
build_race_file(["PROPOSITION 3"], 'p3-r')
build_race_file(["PROPOSITION 4"], 'p4-r')
build_race_file(["DISTRICT 17, UNITED STATES REPRESENTATIVE - REP"], 'usr17-r')
build_race_file(["DISTRICT 10, MEMBER, STATE BOARD OF EDUCATION - REP"], 'sboe10-r')
build_race_file(["DISTRICT 50, STATE REPRESENTATIVE - REP"], 'sr50-r')
build_race_file(["DISTRICT 10, UNITED STATES REPRESENTATIVE - REP"], 'usr10-r')
build_race_file(["PRECINCT NO. 2, CONSTABLE - REP"], 'c2-r')
build_race_file(["DISTRICT 46, STATE REPRESENTATIVE - REP"], 'sr46-r')
build_race_file(["DISTRICT 25, UNITED STATES REPRESENTATIVE - REP"], 'usr25-r')
build_race_file(["DISTRICT 47, STATE REPRESENTATIVE - REP"], 'sr47-r')
build_race_file(["DISTRICT 21, UNITED STATES REPRESENTATIVE - REP"], 'usr21-r')
build_race_file(["PRECINCT NO. 3, COUNTY COMMISSIONER - REP"], 'cc3-r')
build_race_file(["DISTRICT 24, STATE SENATOR - REP"], 'ss24-r')
build_race_file(["PRECINCT 308, PRECINCT CHAIRMAN"], 'pc308-r')
build_race_file(["PRECINCT 312, PRECINCT CHAIRMAN"], 'pc312-r')
build_race_file(["PRECINCT 316, PRECINCT CHAIRMAN"], 'pc316-r')
build_race_file(["PRECINCT 334, PRECINCT CHAIRMAN"], 'pc334-r')
build_race_file(["PRECINCT 429, PRECINCT CHAIRMAN"], 'pc429-r')
