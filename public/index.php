<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <?php
  $meta = array(
    "title" => "Travis County March 1, 2016 primary election results by precinct  | Statesman.com",
    "description" => "Precinct-level results for the March 1, 2016 election.",
    "thumbnail" => "http://projects.statesman.com/databases/election-map-20160301/assets/social-share.png", // needs update
    "shortcut_icon" => "http://media.cmgdigital.com/shared/media/2015-11-16-11-32-05/web/site/www_mystatesman_com/images/favicon.ico",
    "apple_touch_icon" => "http://media.cmgdigital.com/shared/theme-assets/242014/www.statesman.com_fa2d2d6e73614535b997734c7e7d2287.png",
    "url" => "http://projects.statesman.com/databases/election-map-20160301/",
    "twitter" => "statesman"
  );
?>

  <title>Interactive: <?php print $meta['title']; ?> | Austin American-Statesman</title>
  <link rel="shortcut icon" href="<?php print $meta['shortcut_icon']; ?>" />
  <link rel="apple-touch-icon" href="<?php print $meta['apple_touch_icon']; ?>" />

  <link rel="canonical" href="<?php print $meta['url']; ?>" />

  <meta name="description" content="<?php print $meta['description']; ?>">

  <meta property="og:title" content="<?php print $meta['title']; ?>"/>
  <meta property="og:description" content="<?php print $meta['description']; ?>"/>
  <meta property="og:image" content="<?php print $meta['thumbnail']; ?>"/>
  <meta property="og:url" content="<?php print $meta['url']; ?>"/>

  <meta name="twitter:card" content="summary" />
  <meta name="twitter:site" content="@<?php print $meta['twitter']; ?>" />
  <meta name="twitter:title" content="<?php print $meta['title']; ?>" />
  <meta name="twitter:description" content="<?php print $meta['description']; ?>" />
  <meta name="twitter:image" content="<?php print $meta['thumbnail']; ?>" />
  <meta name="twitter:url" content="<?php print $meta['url']; ?>" />

  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="dist/style.css">

  <link href='http://fonts.googleapis.com/css?family=Lusitana:400,700' rel='stylesheet' type='text/css'>
  <link href='http://fonts.googleapis.com/css?family=Merriweather:400,300,300italic,400italic,700,700italic,900,900italic' rel='stylesheet' type='text/css'>
  <link href='http://fonts.googleapis.com/css?family=Merriweather+Sans:400,300,300italic,400italic,700italic,700,800,800italic' rel='stylesheet' type='text/css'>
 

  <?php /* CMG advertising and analytics */ ?>
  <?php include "includes/advertising.inc"; ?>
  <?php include "includes/metrics-head.inc"; ?>

</head>
<body>
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>

        <a class="navbar-brand" href="http://www.statesman.com/" target="_blank">
        <img class="visible-xs visible-sm" width="103" height="26" src="assets/logo-short-black.png" />
        <img class="hidden-xs hidden-sm" width="273" height="26" src="assets/logo.png" />
        </a>
    </div>
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="./">Travis precincts <span class="sr-only">(current)</span></a></li>
        <li><a href="county-results/">President by county</a></li>
        <li><a href="http://www.statesman.com/s/elections-guide/#central-texas-results" target="_blank">More election coverage</a></li>
        <li class="visible-xs small-social"><a target="_blank" href="https://www.facebook.com/sharer.php?u=<?php echo urlencode($meta['url']); ?>"><i class="fa fa-facebook-square"></i></a><a target="_blank" href="https://twitter.com/intent/tweet?url=<?php echo urlencode($meta['url']); ?>&via=<?php print urlencode($meta['twitter']); ?>&text=<?php print urlencode($meta['title']); ?>"><i class="fa fa-twitter"></i></a><a target="_blank" href="https://plus.google.com/share?url=<?php echo urlencode($meta['url']); ?>"><i class="fa fa-google-plus"></i></a></li>
      </ul>
        <ul class="nav navbar-nav navbar-right social hidden-xs">
          <li><a target="_blank" href="https://www.facebook.com/sharer.php?u=<?php echo urlencode($meta['url']); ?>"><i class="fa fa-facebook-square"></i></a></li>
          <li><a target="_blank" href="https://twitter.com/intent/tweet?url=<?php echo urlencode($meta['url']); ?>&via=<?php print urlencode($meta['twitter']); ?>&text=<?php print urlencode($meta['title']); ?>"><i class="fa fa-twitter"></i></a></li>
          <li><a target="_blank" href="https://plus.google.com/share?url=<?php echo urlencode($meta['url']); ?>"><i class="fa fa-google-plus"></i></a></li>
        </ul>
    </div>
  </div>
</nav>

  <article class="container">
  <br>
    <div class="row">
      <div class="col-xs-12 interactive-header">
        <h4>2016 Texas Primary</h4>
        <h1 class="page-title">Travis county precinct-by-precinct results</h1>
        <p class="author">Interactive by Christian McDonald and Cody Winchester, Austin American-Statesman</p>
        <p>Use the dropdown to see the highest vote-getter in a race in a Travis county precinct in the March 1 primary election. Roll your cursor over each precinct on the map to see votes for all candidates in the selected race. Hover over a candidate's name in the map legend to see his or her support in each precinct. <span>Also check out <a href="county-results/"> county-level results for president</a></span>.</p>
      </div>

      <div class="form-group clearfix">
        <div class="col-lg-6">
          <label for="race" class="control-label">Choose a race:</label>
          <select class="form-control" id="race" name="race">
          <optgroup label="National">
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="p-d">PRESIDENT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="p-r">PRESIDENT - REP</option>
            <option data-zoom="+1" data-center="30.372542, -97.652969" value="usr10-d">DISTRICT 10, UNITED STATES REPRESENTATIVE - DEM</option>
            <option data-zoom="+1" data-center="30.372542, -97.652969" value="usr10-r">DISTRICT 10, UNITED STATES REPRESENTATIVE - REP</option>
            <option data-zoom="+1" data-center="30.468765, -97.545294" value="usr17-d">DISTRICT 17, UNITED STATES REPRESENTATIVE - DEM</option>
            <option data-zoom="+1" data-center="30.468765, -97.545294" value="usr17-r">DISTRICT 17, UNITED STATES REPRESENTATIVE - REP</option>
            <option data-zoom="+1" data-center="30.232049, -97.872953" value="usr21-d">DISTRICT 21, UNITED STATES REPRESENTATIVE - DEM</option>
            <option data-zoom="+1" data-center="30.232049, -97.872953" value="usr21-r">DISTRICT 21, UNITED STATES REPRESENTATIVE - REP</option>
            <option data-zoom="0" data-center="30.381437, -98.026075" value="usr25-d">DISTRICT 25, UNITED STATES REPRESENTATIVE - DEM</option>
            <option data-zoom="0" data-center="30.381437, -98.026075" value="usr25-r">DISTRICT 25, UNITED STATES REPRESENTATIVE - REP</option>
            <option data-zoom="+1" data-center="30.195331, -97.665732, -97.758797" value="usr35-d">DISTRICT 35, UNITED STATES REPRESENTATIVE - DEM</option>
            <option data-zoom="+1" data-center="30.195331, -97.665732" value="usr35-r">DISTRICT 35, UNITED STATES REPRESENTATIVE - REP</option>
          </optgroup>
          <optgroup label="State races">
            <option data-zoom="+1" data-center="30.137376, -97.716907" value="ss21-d">DISTRICT 21, STATE SENATOR - DEM</option>
            <option data-zoom="+1" data-center="30.336957, -98.009545" value="ss24-d">DISTRICT 24, STATE SENATOR - DEM</option>
            <option data-zoom="+1" data-center="30.336957, -98.009545" value="ss24-r">DISTRICT 24, STATE SENATOR - REP</option>
            <option data-zoom="+1" data-center="30.331981, -97.601582" value="sr46-d">DISTRICT 46, STATE REPRESENTATIVE - DEM</option>
            <option data-zoom="+1" data-center="30.331981, -97.601582" value="sr46-r">DISTRICT 46, STATE REPRESENTATIVE - REP</option>
            <option data-zoom="-1" data-center="30.356862, -98.006662" value="sr47-d">DISTRICT 47, STATE REPRESENTATIVE - DEM</option>
            <option data-zoom="-1" data-center="30.356862, -98.006662" value="sr47-r">DISTRICT 47, STATE REPRESENTATIVE - REP</option>
            <option data-zoom="+1" data-center="30.288111, -97.786823" value="sr48-d">DISTRICT 48, STATE REPRESENTATIVE - DEM</option>
            <option data-zoom="+1" data-center="30.286244, -97.749343" value="sr49-d">DISTRICT 49, STATE REPRESENTATIVE - DEM</option>
            <option data-zoom="+1" data-center="30.391375, -97.545361" value="sr50-d">DISTRICT 50, STATE REPRESENTATIVE - DEM</option>
            <option data-zoom="+1" data-center="30.391375, -97.545361" value="sr50-r">DISTRICT 50, STATE REPRESENTATIVE - REP</option>
            <option data-zoom="+1" data-center="30.146102, -97.681589" value="sr51-d">DISTRICT 51, STATE REPRESENTATIVE - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="rc-d">RAILROAD COMMISSIONER - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="rc-r">RAILROAD COMMISSIONER - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="sboe5-d">DISTRICT 5, MEMBER, STATE BOARD OF EDUCATION - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="sboe5-r">DISTRICT 5, MEMBER, STATE BOARD OF EDUCATION - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="sboe10-d">DISTRICT 10, MEMBER, STATE BOARD OF EDUCATION - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="sboe10-r">DISTRICT 10, MEMBER, STATE BOARD OF EDUCATION - REP</option>
          </optgroup>
          <optgroup label="Judicial races">
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="scj3-d">PLACE 3, JUSTICE, SUPREME COURT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="scj3-r">PLACE 3, JUSTICE, SUPREME COURT - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="scj5-d">PLACE 5, JUSTICE, SUPREME COURT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="scj5-r">PLACE 5, JUSTICE, SUPREME COURT - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="scj9-d">PLACE 9, JUSTICE, SUPREME COURT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="scj9-r">PLACE 9, JUSTICE, SUPREME COURT - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="caj2-d">PLACE 2, JUDGE, COURT OF CRIMINAL APPEALS - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="caj2-r">PLACE 2, JUDGE, COURT OF CRIMINAL APPEALS - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="caj5-d">PLACE 5, JUDGE, COURT OF CRIMINAL APPEALS - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="caj5-r">PLACE 5, JUDGE, COURT OF CRIMINAL APPEALS - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="caj6-d">PLACE 6, JUDGE, COURT OF CRIMINAL APPEALS - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="caj6-r">PLACE 6, JUDGE, COURT OF CRIMINAL APPEALS - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="3caj2-r">PLACE 2, JUSTICE, 3RD COURT OF APPEALS DISTRICT - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="3caj4-r">PLACE 4, JUSTICE, 3RD COURT OF APPEALS DISTRICT - REP</option>
          </optgroup>
          <optgroup label="County races">
            <option data-zoom="+1" data-center="30.350697, -97.528060" value="cc1-d">PRECINCT NO. 1, COUNTY COMMISSIONER - DEM</option>
            <option data-zoom="+1" data-center="30.350697, -97.528060" value="cc1-r">PRECINCT NO. 1, COUNTY COMMISSIONER - REP</option>
            <option data-zoom="+1" data-center="30.402323, -97.929113" value="cc3-d">PRECINCT NO. 3, COUNTY COMMISSIONER - DEM</option>
            <option data-zoom="+1" data-center="30.402323, -97.929113" value="cc3-r">PRECINCT NO. 3, COUNTY COMMISSIONER - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="da53-d">DISTRICT ATTORNEY, 53RD JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="da53-r">DISTRICT ATTORNEY, 53RD JUDICIAL DISTRICT - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj53-d">DISTRICT JUDGE, 53RD JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj98-d">DISTRICT JUDGE, 98TH JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj126-d">DISTRICT JUDGE, 126TH JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj167-d">DISTRICT JUDGE, 167TH JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj200-d">DISTRICT JUDGE, 200TH JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj345-d">DISTRICT JUDGE, 345TH JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj353-d">DISTRICT JUDGE, 353RD JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj390-d">DISTRICT JUDGE, 390TH JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj427-d">DISTRICT JUDGE, 427TH JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj450-d">DISTRICT JUDGE, 450TH JUDICIAL DISTRICT - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="dj450-r">DISTRICT JUDGE, 450TH JUDICIAL DISTRICT - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="s-d">SHERIFF - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="s-r">SHERIFF - REP</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="tac-d">TAX ASSESSOR-COLLECTOR - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="ccj8-d">JUDGE, COUNTY CRIMINAL COURT NO. 8 - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="ccj9-d">JUDGE, COUNTY CRIMINAL COURT NO. 9 - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="ca-d">COUNTY ATTORNEY - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="chair-d">COUNTY CHAIRMAN - DEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="chair-r">COUNTY CHAIRMAN - REP</option>
            <option data-zoom="+1" data-center="30.350697, -97.528060" value="c1-d">PRECINCT NO. 1, CONSTABLE - DEM</option>
            <option data-zoom="0" data-center="30.480208, -97.777208" value="c2-d">PRECINCT NO. 2, CONSTABLE - DEM</option>
            <option data-zoom="0" data-center="30.480208, -97.777208" value="c2-r">PRECINCT NO. 2, CONSTABLE - REP</option>
            <option data-zoom="0" data-center="30.309475, -97.945225" value="c3-d">PRECINCT NO. 3, CONSTABLE - DEM</option>
            <option data-zoom="+1" data-center="30.157849, -97.719668" value="c4-d">PRECINCT NO. 4, CONSTABLE - DEM</option>
            <option data-zoom="+1" data-center="30.305004, -97.755343" value="c5-d">PRECINCT NO. 5, CONSTABLE - DEM</option>
          </optgroup>
          <optgroup label="Democratic party races">
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="r1-d">REFERENDUM ITEM #1 - ON ECONOMIC SECURITY & PROSPERITY</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="r2-d">REFERENDUM ITEM #2 - ON A FAIR CRIMINAL JUSTICE SYSTEM</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="r3-d">REFERENDUM ITEM #3 - ON CLIMATE</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="r4-d">REFERENDUM ITEM #4 - ON THE VOTING RIGHTS ACT</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="r5-d">REFERENDUM ITEM #5 - ON CAMPUS CARRY</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="r6-d">REFERENDUM ITEM #6 - ON COMPREHENSIVE IMMIGRATION REFORM</option>
            <option data-zoom="+3" data-center="30.232095, -97.749754" value="pc433">PRECINCT 433, PRECINCT CHAIRMAN</option>
          </optgroup>
          <optgroup label="Republican party races">
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="p1-r">PROPOSITION 1</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="p2-r">PROPOSITION 2</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="p3-r">PROPOSITION 3</option>
            <option data-zoom="-1" data-center="30.329632, -97.758797" value="p4-r">PROPOSITION 4</option>
            <option data-zoom="+3" data-center="30.279221, -97.665287" value="pc129">PRECINCT 129, PRECINCT CHAIRMAN</option>
            <option data-zoom="+2" data-center="30.401235, -98.049124" value="pc308-r">PRECINCT 308, PRECINCT CHAIRMAN</option>
            <option data-zoom="+3" data-center="30.413655, -97.930594" value="pc312-r">PRECINCT 312, PRECINCT CHAIRMAN</option>
            <option data-zoom="+2" data-center="30.302496, -98.031929" value="pc316-r">PRECINCT 316, PRECINCT CHAIRMAN</option>
            <option data-zoom="+3" data-center="30.446749, -97.806538" value="pc334-r">PRECINCT 334, PRECINCT CHAIRMAN</option>
            <option data-zoom="+3" data-center="30.232818, -97.718647" value="pc429-r">PRECINCT 429, PRECINCT CHAIRMAN</option>

          </optgroup>
          </select>
        </div>
        <div class="col-lg-6">
          <label for="address" class="control-label">Find an address:</label>
          <input name="address" id="address" type="text" class="form-control">
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col-xs-12 col-sm-8 col-sm-push-4">
        <div id="map" style="width:100%;min-height:350px;"></div>
      </div>
      <div class="col-xs-12 col-sm-4 col-sm-pull-8">
        <ul id="key" class="list-group"></ul>
        <div id="results"></div>
        <p><small>Data source: Travis County Clerk, Elections Division<!-- ; Williamson County Clerk, Elections Department--></small></p>
      </div>
    </div>
  </div>
  <br>

  </article>


    <!-- bottom matter -->
    <?php include "includes/banner-ad.inc";?>
    <?php include "includes/legal.inc";?>
    <?php include "includes/project-metrics.inc"; ?>
    <?php include "includes/metrics.inc"; ?>

    <script type="text/javascript" src="http://maps.google.com/maps/api/js?key=AIzaSyBFqzY0Bf4VMn4Wtx-EEb9S-cVkvzm8RFE  &libraries=places"></script>
    <script src="dist/scripts.js"></script>


  <?php if($_SERVER['SERVER_NAME'] === 'localhost'): ?>
    <script src="//localhost:35729/livereload.js"></script>
  <?php endif; ?>
</body>
</html>
