Election results March 1, 2016
===============================

Thought is to have a two pronged project:

* Precinct-level results from Travis and possibly Williamson County, based off of [last year](http://projects.statesman.com/databases/election-map-20151103/).
* County-level results for presidential races, maybe scraped [from here](https://enrpages.sos.state.tx.us/)?
* We should also include Williamson and Hays, but Williamson was not ready the afternoon after the election. We have done it in the past and have the geo files for it from an earlier election. Hays was pretty lost on how to get us the data.

## County

### Scrape the data

Some python scripts by @cjwinchester to pull the state results:

``` shell
pip install requirements.txt
cd results/state
## for a json file of Democratic primary:
fab scrape:d > dems.json results
##for a json file of GOP primary results:
fab scrape:r > gop.json 
```

<@cjwinchester to add more info here about County stuff>

## Travis precincts

Get the file from [Travis county elections](elections@traviscoutytx.gov). I typically reach out to Ginny Ballard in advance and ask her to ftp it to ftp.statesman.com. Perhaps for the general we can get the races in advance?

Ginny Ballard CERA
Public Information Coordinator
Travis County Clerk – Elections Division
512-854-4177

### Processing
* The file comes as something like `20160301unconsolidatedtallyexportwithoversandunders.txt`
* I uploaded this into mysql and then ran a consolidation based on candidate, with `20160301_Travis` as my table name:

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

* I then exported that to `/results/travis.csv`
* I did a separate query to get the titles so I can build the files list for processing:

``` sql
SELECT DISTINCT
`20160301_Travis`.`Contest_title`
FROM
`20160301_Travis`
```

* I then took each line of that file and started creating the python array in a file called `contest_titles_travis_py.csv`. It looks something like this:

``` python
build_race_file(["PRESIDENT - DEM"], 'p-d')
build_race_file(["DISTRICT 35, UNITED STATES REPRESENTATIVE - DEM"], 'rd35-d')
```

The last field has to be unique for the race, and will be used in the name of the JSON file, and for the dropdown in the map. I had to decide myself what to call each race.

I then used regex on that to create `contest_selects_travis.txt`, which is formated like this and later added to the html page of results:

``` html
<option data-zoom="-1" data-center="30.329632, -97.758797" value="p-d">PRESIDENT - DEM</option>
<option data-zoom="-1" data-center="30.329632, -97.758797" value="rd35-d">DISTRICT 35, UNITED STATES REPRESENTATIVE - DEM</option>

```

The `data-zoom` and `data-center` options there can be used to center the map for that race, which I did after everything else was done. 

* Lastly, I put in a blank `williamson.csv` file with only headers so the next step wouldn't choke.

### Creating the JSON files

The script `races.py` walks through the `results/travis.csv` and and `results/williamson.csv` files to combine them. I took the contents of my `contest_titles_travis_py.csv` file and replaced what was at the bottom of `races.py` and then ran the python script. (It did fail first when I didn't have a `williamson.csv` file it expected.)

### Updating index.php

I had to sub in the `contest_selects_travis.txt` info into this file, rearranging it to make sense.


