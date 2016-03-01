var Results = (function($, JST, _, numeral) {

  var race_value = function(part, whole) {
    if(whole === 0) {
      return '-';
    }
    else {
      return numeral(part).format('0,0') + ' <small>(' + numeral(part / whole).format('0 %') + ')</small>';
    }
  };

  function Results(el) {
    this.$el = $(el);
    this.$el.html(JST.results());
  }

  // Show the precinct result instructions
  Results.prototype.showDefault = function() {
    this.$el.html(JST.results());
  };

  // Update the key with new data
  Results.prototype.update = function(data) {
    // Take a pass to determine total votes
    var total_votes = 0;
    _.each(data.races, function(race) {
      total_votes += race.votes;
    });
    // Run through again and add percentages, format votes
    _.each(data.races, function(race) {
      if(total_votes !== 0) {
        race.share = numeral(race.votes / total_votes).format('0 %');
      }
      else {
        race.share = '-';
      }
      race.votes_str = numeral(race.votes).format('0,0');
    });
    // Format demographic data
    if(typeof data.SUM_TOTAL !== "undefined" && data.SUM_TOTAL !== 0) {
      data.demos = [
        {
          "group": "Anglo",
          "sum": race_value(data.SUM_ANGLO, data.SUM_TOTAL),
          "sum_vap": race_value(data.SUM_ANGLOV, data.SUM_VAP)
        },
        {
          "group": "Hispanic",
          "sum": race_value(data.SUM_HISPAN, data.SUM_TOTAL),
          "sum_vap": race_value(data.SUM_HISP_1, data.SUM_VAP)
        },
        {
          "group": "Black",
          "sum": race_value(data.SUM_BLACK, data.SUM_TOTAL),
          "sum_vap": race_value(data.SUM_BLACKV, data.SUM_VAP)
        }
      ];
      data.demos_sum = {
        "sum": numeral(data.SUM_TOTAL).format('0,0'),
        "sum_vap": numeral(data.SUM_VAP).format('0,0')
      };
    }
    this.$el.html(JST.results(data));
  };

  return Results;

}(jQuery, JST, _, numeral));
