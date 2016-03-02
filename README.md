Election results March 1, 2016
===============================

Thought is to have a two pronged project:

* Precinct-level results from Travis and possibly Williamson County, based off of [last year](http://projects.statesman.com/databases/election-map-20151103/).
* County-level results for presidential races, maybe scraped from here?

God help us.

### County scrape
``` shell
pip install requirements.txt
cd results/state
## for a json file of Democratic primary:
fab scrape:d > dems.json results
##for a json file of GOP primary results:
fab scrape:r > gop.json 
```