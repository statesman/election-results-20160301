Election results March 1, 2016
===============================

Thought is to have a two pronged project:

* Precinct-level results from Travis and possibly Williamson County, based off of [last year](http://projects.statesman.com/databases/election-map-20151103/).
* County-level results for presidential races, maybe scraped from here?

God help us.

## County scrape
``` shell
pip install requirements.txt
cd results/state
## for a json file of Democratic primary:
fab scrape:d > dems.json results
##for a json file of GOP primary results:
fab scrape:r > gop.json 
```

## Travis precincts

Get the file from [Travis county elections](elections@traviscoutytx.gov). I typically reach out to Ginny Ballard in advance and ask her to ftp it to ftp.statesman.com.

Ginny Ballard CERA
Public Information Coordinator
Travis County Clerk – Elections Division
512-854-4177

### Processing
* The file comes as something like `20160301unconsolidatedtallyexportwithoversandunders.txt`
* I uploaded this into mysql and then ran a consolidation based on candidate

``` sql
SELECT
    `20160301_Travis`.`Precinct_name`,
    `20160301_Travis`.`Contest_title`,
    `20160301_Travis`.`candidate_name`,
    `20160301_Travis`.`Party_Code`,
    sum(`20160301_Travis`.`total_votes`)
FROM
    `20160301_Travis`
GROUP BY
    1,2,3,4
```

* and then exported that into `/results/` as `travis.csv`
* I did a separate query to get the titles so I can build the files list for processing:

``` sql
SELECT DISTINCT
`20160301_Travis`.`Contest_title`
FROM
`20160301_Travis`
```

* I then took each line of that file and started creating the python array in a file called `contest_titles_travis_py.csv`:

``` python
build_race_file(["PRESIDENT - DEM"], 'p-dem')
build_race_file(["DISTRICT 35, UNITED STATES REPRESENTATIVE - DEM"], 'rd35-dem')
```

The last field has to be unique for the race, and will be used in the name of the JSON file, and for the dropdown in the map. I had to decide myself what to call each race.

I then used regex on that to create `contest_selects_travis.txt`, which is formated like this:

``` html
<option data-zoom="-1" data-center="30.470995016166533,-97.67961883544923" value="p-d">PRESIDENT - DEM</option>
<option data-zoom="-1" data-center="30.470995016166533,-97.67961883544923" value="rd35-d">DISTRICT 35, UNITED STATES REPRESENTATIVE - DEM</option>

```

* Lastly, I put in a blank `williamson.csv` file with only headers so the next step wouldn't choke.

### Creating the JSON files

The script `races.py` walks through the `results/travis.csv` and and `results/williamson.csv` files to combine them. I took the contents of my `contest_titles_travis_py.csv` file and replaced what was at the bottom of `races.py` and then ran the python script. (It did fail first when I didn't have a `williamson.csv` file it expected.)

### Updating index.php

I had to sub in the `contest_selects_travis.txt` info into this file, rearranging it to make sense.


