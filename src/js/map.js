var ElectionMap = (function($, GMaps, google){

  function ElectionMap(el, keyEl) {
    this.defaults = {
      center: [30.329632, -97.758797],
      zoom: 10
    };

    this.gmap = new GMaps({
      div: el,
      lat: this.defaults.center[0],
      lng: this.defaults.center[1],
      zoom: this.defaults.zoom,
      minZoom: 10,
      maxZoom: 14
    });
  }

  ElectionMap.prototype.focus = function(zoom, center) {
    if(typeof center !== "undefined") {
      this.gmap.setCenter(center[0], center[1]);
    }
    else {
      this.gmap.setCenter(this.defaults.center[0], this.defaults.center[1]);
    }

    if(typeof zoom !== "undefined") {
      this.gmap.setZoom(this.defaults.zoom + parseInt(zoom, 10));
    }
    else {
      this.gmap.setZoom(this.defaults.zoom);
    }
  };

  ElectionMap.prototype.clear = function() {
    this.gmap.removePolygons();
    this.gmap.removePolylines();
  };

  ElectionMap.prototype.mark = function(lat, lng) {
    this.unMark();
    this.gmap.addMarker({
      lat: lat,
      lng: lng
    });
    this.focus(2, [lat, lng]);
  };

  ElectionMap.prototype.unMark = function() {
    this.gmap.removeMarkers();
  };

  ElectionMap.prototype.drawPrecinct = function(opts) {
    var opacity = opts.opacity || 0.5,
        self = this;

    this.gmap.drawPolygon({
      paths: opts.paths,
      useGeoJSON: true,
      strokeColor: '#fff',
      strokeOpacity: 0.5,
      strokeWeight: 1,
      fillColor: opts.fill,
      fillOpacity: opacity,
      zIndex: 500,
      mouseover: function() {
        self.results.update(opts.resultsData);
        this.setOptions({
          strokeWeight: 4,
          strokeOpacity: 0.75,
          zIndex: 505
        });
      },
      mouseout: function() {
        self.results.showDefault();
        this.setOptions({
          strokeWeight: 1,
          strokeOpacity: 0.5,
          zIndex: 500
        });
      }
    });
  };

  ElectionMap.prototype.drawPrecinctsByWinner = function(precincts) {
    var self = this;
    _.each(precincts, function(precinct) {
      if(typeof precinct.properties !== "undefined") {
        this.drawPrecinct({
          paths: precinct.geometry.coordinates,
          fill: this.colors.get(precinct.properties.winner.candidate, precinct.properties.winner.party),
          resultsData: precinct.properties
        });
      }
    }, self);
  };

  ElectionMap.prototype.drawPrecinctsBySupport = function(precincts, opt, label) {
    var color = this.colors.get(opt, "", label),
        self = this;

    _.each(precincts, function(precinct) {
      if(typeof precinct.properties !== "undefined") {
        var votes_for = 0,
            total_votes = 0;
        _.each(precinct.properties.races, function(option) {
          if(option.candidate === opt) {
            votes_for += option.votes;
          }
          total_votes += option.votes;
        });
        this.drawPrecinct({
          paths: precinct.geometry.coordinates,
          fill: color,
          opacity: (votes_for / total_votes) * 1.25,
          resultsData: precinct.properties
        });
      }
    }, self);
  };

  ElectionMap.prototype.preDraw = function(race) {
    this.clear();

    if(typeof this.key !== "undefined") {
      this.key.destroy();
    }

    this.key = new Key('#key', this);
    this.colors = new Palette(this.key);
    this.results = new Results('#results');
    this.race = race;
  };

  ElectionMap.prototype.drawWinners = function(race) {
    this.preDraw(race);

    var self = this;
    $.getJSON('race-data/' + race + '.json', function(data) {
      self.raceData = data;
      self.drawPrecinctsByWinner(data.features);
    });
  };

  ElectionMap.prototype.drawSupport = function(race, opt) {
    this.preDraw(race);

    var label = "";
    if (opt === "For") {
      label = "Votes for " + race;
    }
    else {
      label = "Votes for " + opt;
    }
    label = label + " <small>(darker precincts indicate higher support)</small>";

    var self = this;
    $.getJSON('race-data/' + race + '.json', function(data) {
      self.raceData = data;
      self.drawPrecinctsBySupport(data.features, opt, label);
    });
  };

  ElectionMap.prototype.showSupport = function(opt) {
    this.gmap.removePolygons();

    this.drawPrecinctsBySupport(this.raceData.features, opt);
  };

  ElectionMap.prototype.hideSupport = function() {
    this.gmap.removePolygons();

    this.drawPrecinctsByWinner(this.raceData.features);
  };

  return ElectionMap;

}(jQuery, GMaps, google));
