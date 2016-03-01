<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <?php
  $meta = array(
    "title" => "Travis County November 3, 2015 election results by precinct  | Statesman.com",
    "description" => "Precinct-level results for the Novemer 3, 2015 election.",
    "thumbnail" => "http://projects.statesman.com/election-results-20151103/assets/share.png", // needs update
    "shortcut_icon" => "http://media.cmgdigital.com/shared/theme-assets/242014/www.statesman.com_5126cb2068bd43d1ab4e17660ac48255.ico",
    "apple_touch_icon" => "http://media.cmgdigital.com/shared/theme-assets/242014/www.statesman.com_fa2d2d6e73614535b997734c7e7d2287.png",
    "url" => "http://projects.statesman.com/databases/election-results-20151103/",
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
<div id="back">


  <div class="container">
    <div class="row">
      <div class="col-xs-12 header">
        <h4>2015 elections</h4>
        <h2 class="page-title">Travis county precinct-by-precinct results</h2>
        <p><small>Interactive by Christian McDonald and Andrew Chavez, Austin American-Statesman</small></p>
        <p>Use the dropdown to see the highest vote-getter in a race in a Travis county precinct in the Nov. 3 general election. Roll your cursor over each precinct on the map to see votes for all candidates in the selected race. Hover over a candidate's name in the map legend to see his or her support in each precinct. Williamson county totals are not included.</p>
      </div>

      <div class="form-group clearfix">
        <div class="col-lg-6">
          <label for="race" class="control-label">Choose a race:</label>
           <select class="form-control" id="race" name="race">
            <optgroup label="Travis County">
                <option data-zoom="-1" data-center="30.329632, -97.758797" value="tr-bond">TRAVIS COUNTY BOND PROPOSITION, TRAVIS COUNTY BOND ELECTION</option>
            </optgroup>
            <optgroup label="State amendments">
                <option data-zoom="-1" data-center="30.329632, -97.758797" value="ca-01">PROP. 1, CONSTITUTIONAL AMENDMENT ELECTION</option>
                <option data-zoom="-1" data-center="30.329632, -97.758797" value="ca-02">PROP. 2, CONSTITUTIONAL AMENDMENT ELECTION</option>
                <option data-zoom="-1" data-center="30.329632, -97.758797" value="ca-03">PROP. 3, CONSTITUTIONAL AMENDMENT ELECTION</option>
                <option data-zoom="-1" data-center="30.329632, -97.758797" value="ca-04">PROP. 4, CONSTITUTIONAL AMENDMENT ELECTION</option>
                <option data-zoom="-1" data-center="30.329632, -97.758797" value="ca-05">PROP. 5, CONSTITUTIONAL AMENDMENT ELECTION</option>
                <option data-zoom="-1" data-center="30.329632, -97.758797" value="ca-06">PROP. 6, CONSTITUTIONAL AMENDMENT ELECTION</option>
                <option data-zoom="-1" data-center="30.329632, -97.758797" value="ca-07">PROP. 7, CONSTITUTIONAL AMENDMENT ELECTION</option>
            </optgroup>
            <optgroup label="Individual cities">
                <option data-zoom="+2" data-center="30.458022, -97.613120" value="pf-p3">COUNCIL MEMBER, PLACE 3, CITY OF PFLUGERVILLE</option>
                <option data-zoom="+2" data-center="30.458022, -97.613120" value="pf-p5">COUNCIL MEMBER, PLACE 5, CITY OF PFLUGERVILLE</option>
                <option data-zoom="+2" data-center="30.458022, -97.613120" value="pf-p01">PROP. 1, CITY OF PFLUGERVILLE</option>
                <option data-zoom="+2" data-center="30.458022, -97.613120" value="pf-p02">PROP. 2, CITY OF PFLUGERVILLE</option>
                <option data-zoom="+1" data-center="30.347887, -97.486435" value="wb-p01">PROPOSITION, VILLAGE OF WEBBERVILLE</option>
                <option data-zoom="+2" data-center="30.274056, -97.811662" value="wb-library">BOARD OF TRUSTEE, WESTBANK COMMUNITY LIBRARY DISTRICT</option>
                <option data-zoom="+2" data-center="30.226140, -97.815576" value="sv-council">CITY COUNCIL, CITY OF SUNSET VALLEY</option>
                <option data-zoom="+2" data-center="30.226140, -97.815576" value="sv-p01">PROPOSITION 1, CITY OF SUNSET VALLEY</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-mayor">MAYOR, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-cc01">COUNCIL MEMBER, PLACE 1, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-cc03">COUNCIL MEMBER, PLACE 3, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-cc05">COUNCIL MEMBER, PLACE 5, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-p01">PROPOSITION 1, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-p02">PROPOSITION 2, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-p03">PROPOSITION 3, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-p04">PROPOSITION 4, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-p05">PROPOSITION 5, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-p06">PROPOSITION 6, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-p07">PROPOSITION 7, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-p08">PROPOSITION 8, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="lv-p09">PROPOSITION 9, CITY OF LAGO VISTA</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="j-mayor">MAYOR, CITY OF JONESTOWN</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="j-ap1">ALDERMAN, PLACE 1, CITY OF JONESTOWN</option>
                <option data-zoom="+1" data-center="30.461191, -97.989763" value="j-ap2">ALDERMAN, PLACE 2, CITY OF JONESTOWN</option>
                <option data-zoom="+2" data-center="30.503471, -97.902008" value="cp-p01">PROP. 1, CITY OF CEDAR PARK</option>
                <option data-zoom="+2" data-center="30.503471, -97.902008" value="cp-p02">PROP. 2, CITY OF CEDAR PARK</option>
                <option data-zoom="+2" data-center="30.503471, -97.902008" value="cp-p03">PROP. 3, CITY OF CEDAR PARK</option>
                <option data-zoom="+2" data-center="30.503471, -97.902008" value="cp-p04">PROP. 4, CITY OF CEDAR PARK</option>
                <option data-zoom="+2" data-center="30.437719, -97.975931" value="pv-mayor">MAYOR, VILLAGE OF POINT VENTURE</option>
                <option data-zoom="+2" data-center="30.461401, -97.888092" value="v-council">VILLAGE COUNCIL, VILLAGE OF VOLENTE</option>
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

<hr>

    <!-- bottom matter -->
    <?php include "includes/banner-ad.inc";?>
    <?php include "includes/legal.inc";?>
    <?php include "includes/project-metrics.inc"; ?>
    <?php include "includes/metrics.inc"; ?>

    <script type="text/javascript" src="http://maps.google.com/maps/api/js?key=AIzaSyBFqzY0Bf4VMn4Wtx-EEb9S-cVkvzm8RFE  &libraries=places"></script>
    <script src="dist/scripts.js"></script>

</div>

  <?php if($_SERVER['SERVER_NAME'] === 'localhost'): ?>
    <script src="//localhost:35729/livereload.js"></script>
  <?php endif; ?>
</body>
</html>
