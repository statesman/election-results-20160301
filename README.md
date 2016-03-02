Election results March 1, 2016
===============================

Thought is to have a two pronged project:

* Precinct-level results from Travis and possibly Williamson County, based off of [last year](http://projects.statesman.com/databases/election-map-20151103/).
* County-level results for presidential races, maybe scraped from here?

God help us.

### County scrape
`pip install requirements.txt`
`cd results/state`
`fab scrape:d > dems.json` for a json file of Democratic primary results
`fab scrape:r > gop.json` for a json file of GOP primary results
