// function to add thousand-separator commas
function addCommas(num) {
    num += '';
    var x = num.split('.');
    var x1 = x[0];
    var x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }
    return x1 + x2;
}

(function($, _) {
    "use strict";

    var FIPS = {"001": "Anderson", "003": "Andrews", "005": "Angelina", "007": "Aransas", "009": "Archer", "011": "Armstrong", "013": "Atascosa", "015": "Austin", "017": "Bailey", "019": "Bandera", "021": "Bastrop", "023": "Baylor", "025": "Bee", "027": "Bell", "029": "Bexar", "031": "Blanco", "033": "Borden", "035": "Bosque", "037": "Bowie", "039": "Brazoria", "041": "Brazos", "043": "Brewster", "045": "Briscoe", "047": "Brooks", "049": "Brown", "051": "Burleson", "053": "Burnet", "055": "Caldwell", "057": "Calhoun", "059": "Callahan", "061": "Cameron", "063": "Camp", "065": "Carson", "067": "Cass", "069": "Castro", "071": "Chambers", "073": "Cherokee", "075": "Childress", "077": "Clay", "079": "Cochran", "081": "Coke", "083": "Coleman", "085": "Collin", "087": "Collingsworth", "089": "Colorado", "091": "Comal", "093": "Comanche", "095": "Concho", "097": "Cooke", "099": "Coryell", "101": "Cottle", "103": "Crane", "105": "Crockett", "107": "Crosby", "109": "Culberson", "111": "Dallam", "113": "Dallas", "115": "Dawson", "117": "Deaf Smith", "119": "Delta", "121": "Denton", "123": "DeWitt", "125": "Dickens", "127": "Dimmit", "129": "Donley", "131": "Duval", "133": "Eastland", "135": "Ector", "137": "Edwards", "139": "Ellis", "141": "El Paso", "143": "Erath", "145": "Falls", "147": "Fannin", "149": "Fayette", "151": "Fisher", "153": "Floyd", "155": "Foard", "157": "Fort Bend", "159": "Franklin", "161": "Freestone", "163": "Frio", "165": "Gaines", "167": "Galveston", "169": "Garza", "171": "Gillespie", "173": "Glasscock", "175": "Goliad", "177": "Gonzales", "179": "Gray", "181": "Grayson", "183": "Gregg", "185": "Grimes", "187": "Guadalupe", "189": "Hale", "191": "Hall", "193": "Hamilton", "195": "Hansford", "197": "Hardeman", "199": "Hardin", "201": "Harris", "203": "Harrison", "205": "Hartley", "207": "Haskell", "209": "Hays", "211": "Hemphill", "213": "Henderson", "215": "Hidalgo", "217": "Hill", "219": "Hockley", "221": "Hood", "223": "Hopkins", "225": "Houston", "227": "Howard", "229": "Hudspeth", "231": "Hunt", "233": "Hutchinson", "235": "Irion", "237": "Jack", "239": "Jackson", "241": "Jasper", "243": "Jeff Davis", "245": "Jefferson", "247": "Jim Hogg", "249": "Jim Wells", "251": "Johnson", "253": "Jones", "255": "Karnes", "257": "Kaufman", "259": "Kendall", "261": "Kenedy", "263": "Kent", "265": "Kerr", "267": "Kimble", "269": "King", "271": "Kinney", "273": "Kleberg", "275": "Knox", "277": "Lamar", "279": "Lamb", "281": "Lampasas", "283": "La Salle", "285": "Lavaca", "287": "Lee", "289": "Leon", "291": "Liberty", "293": "Limestone", "295": "Lipscomb", "297": "Live Oak", "299": "Llano", "301": "Loving", "303": "Lubbock", "305": "Lynn", "307": "McCulloch", "309": "McLennan", "311": "McMullen", "313": "Madison", "315": "Marion", "317": "Martin", "319": "Mason", "321": "Matagorda", "323": "Maverick", "325": "Medina", "327": "Menard", "329": "Midland", "331": "Milam", "333": "Mills", "335": "Mitchell", "337": "Montague", "339": "Montgomery", "341": "Moore", "343": "Morris", "345": "Motley", "347": "Nacogdoches", "349": "Navarro", "351": "Newton", "353": "Nolan", "355": "Nueces", "357": "Ochiltree", "359": "Oldham", "361": "Orange", "363": "Palo Pinto", "365": "Panola", "367": "Parker", "369": "Parmer", "371": "Pecos", "373": "Polk", "375": "Potter", "377": "Presidio", "379": "Rains", "381": "Randall", "383": "Reagan", "385": "Real", "387": "Red River", "389": "Reeves", "391": "Refugio", "393": "Roberts", "395": "Robertson", "397": "Rockwall", "399": "Runnels", "401": "Rusk", "403": "Sabine", "405": "San Augustine", "407": "San Jacinto", "409": "San Patricio", "411": "San Saba", "413": "Schleicher", "415": "Scurry", "417": "Shackelford", "419": "Shelby", "421": "Sherman", "423": "Smith", "425": "Somervell", "427": "Starr", "429": "Stephens", "431": "Sterling", "433": "Stonewall", "435": "Sutton", "437": "Swisher", "439": "Tarrant", "441": "Taylor", "443": "Terrell", "445": "Terry", "447": "Throckmorton", "449": "Titus", "451": "Tom Green", "453": "Travis", "455": "Trinity", "457": "Tyler", "459": "Upshur", "461": "Upton", "463": "Uvalde", "465": "Val Verde", "467": "Van Zandt", "469": "Victoria", "471": "Walker", "473": "Waller", "475": "Ward", "477": "Washington", "479": "Webb", "481": "Wharton", "483": "Wheeler", "485": "Wichita", "487": "Wilbarger", "489": "Willacy", "491": "Williamson", "493": "Wilson", "495": "Winkler", "497": "Wise", "499": "Wood", "501": "Yoakum", "503": "Young", "505": "Zapata", "507": "Zavala"};

    var GEOJSON_URL = '../race-data/counties.json';
    var DEM_DATA_URL = 'dems.json';
    var GOP_DATA_URL = 'gop.json';

    _.templateSettings.variable = "template_data";
    var key_template = _.template($( "script.key_template" ).html());
    var results_template = _.template($( "script.results_template" ).html());

    var colors = {
        "Hillary Clinton": "#1E44A8",
        "Bernie Sanders": "#1E8A0E",
        "Keith Judd": "#FFCC00",
        "Martin O'Malley": "#FF6600",
        "Star Locke": "#4D1979",
        "Willie Wilson": "#4D1979",
        "Roque \"Rocky\" De La Fuente": "#4D1979",
        "Calvis L. Hawes": "#4D1979",
        "Rand Paul": "#4D1979",
        "Rick Santorum": "#4D1979",
        "Chris Christie": "#4D1979",
        "Jeb Bush": "#4D1979",
        "Uncommitted": "#4D1979",
        "John Kasich": "#FFCC00",
        "Donald Trump": "#1E8A0E",
        "Lindsey Graham": "#4D1979",
        "Marco Rubio": "#FF6600",
        "Mike Huckabee": "#4D1979",
        "Elizabeth Gray": "#4D1979",
        "Carly Fiorina": "#4D1979",
        "Ben Carson": "#4D1979",
        "Ted Cruz": "#1E44A8"
    };

    $('#loading').html('Loading ...');

    // get county geojson
    $.getJSON(GEOJSON_URL).then(function(geodata) {

        // load and cache dem/gop data
        var dem_data, gop_data;

        $.when(
            $.getJSON(DEM_DATA_URL, function(data) {
                dem_data = data;
            }),
            $.getJSON(GOP_DATA_URL, function(data) {
                gop_data = data;
            })
        ).then(function() {

            var gmap = new GMaps({
              div: "#map",
              lat: 31.29,
              lng: -100.29,
              zoom: 6
            });

            $('.partypick').on('click', function() {
                var $t = $(this);
                if ($t.attr('id') === "gop") {
                    $t.removeClass('btn-default')
                           .addClass('btn-danger');
                    $("#dems").removeClass('btn-primary')
                              .addClass('btn-default');
                } else {

                    $t.removeClass('btn-default')
                           .addClass('btn-primary');
                    $("#gop").removeClass('btn-danger')
                              .addClass('btn-default');
                }
                var p = $t.attr('id');
                updateMap(p);
            });

        function fetchResults(fips, party) {
            var record;
            if (party === "dems") {
                record = _.find(dem_data.popular_vote, function(d) {
                    return Object.getOwnPropertyNames(d)[0] === fips.toString();
                });
            } else {
                record = _.find(gop_data.popular_vote, function(d) {
                    return Object.getOwnPropertyNames(d)[0] === fips.toString();
                });
            }

            var results = {};
            var isTie = false;
            var votes = _.values(record[fips].regular).sort().reverse();
            if (votes[0] === votes[1]) {
                isTie = true;
            }
            var total = _.reduce(votes, function(memo, num){ return memo + num; }, 0);

            results.countyname = FIPS[fips];
            results.totalvotes = total;
            results.tie = isTie;
            results.candidates = [];
            _.each(record[fips].regular, function(v, k, i) {
                results.candidates.push({
                    name: k,
                    votes: v,
                    share: ((+v / total) * 100).toFixed(2).replace(".00", "")
                });
            });
            return results;
        }

        var getUniqueWinners = function(party) {
            var winners = [];
            var data_source;
            if (party === "dems") {
                data_source = dem_data;
            } else {
                data_source = gop_data;
            }
            _.each(data_source.popular_vote, function(d) {
                var county_totals = _.values(d)[0];
                var winner = "";
                var max = 0;
                _.each(county_totals.regular, function(v,k,i) {
                    if (v > max) {
                        winner = k;
                        max = v;
                    }
                });
                winners.push(winner);
            });
            return _.uniq(winners);
        };

        var getStatewideTotals = function(party) {
            var totals = {};
            var data_source;
            if (party === "dems") {
                data_source = dem_data;
            } else {
                data_source = gop_data;
            }
            _.each(data_source.popular_vote, function(d) {
                var county_totals = _.values(d)[0];
                _.each(county_totals.regular, function(v,k,i) {
                    if (!totals.hasOwnProperty(k)) {
                        totals[k] = +v;
                    } else {
                        totals[k] += +v;
                    }
                });
            });
            return totals;
        };

        var w = getUniqueWinners("gop");

        var key_data_to_template = {
            cands: []
        };

        _.each(w, function(s) {
            if (s && s !== "") {
                key_data_to_template.cands.push({
                    "name": s,
                    "color": colors[s]
                });
            } else {
                key_data_to_template.cands.push({
                    "name": "No results",
                    "color": "white",
                    "border": "#aaa"
                });
            }
        });

        $("#key").html(key_template(key_data_to_template));

        $("#results").html(results_template(""));

        // draw the county polygons
        _.each(geodata.features, function(d) {
            var record = fetchResults(d.properties.COUNTYFP.toString(), "gop");
                var winner = _.max(record.candidates, function(d) { return d.votes; } );
                var color;
                if (record.isTie) {
                    color = "#000000";
                }
                else if (record.totalvotes < 1) {
                    color = "#ffffff";
                }
                else {
                    color = colors[winner.name];
                }

                var to_template = {
                    results: {
                        county: record.countyname,
                        totalvotes: record.totalvotes,
                        candidates: _.sortBy(record.candidates, function(d) { return d.votes; }).reverse()
                    }
                };

                gmap.drawPolygon({
                  paths: d.geometry.coordinates,
                  useGeoJSON: true,
                  strokeColor: '#fff',
                  strokeOpacity: 0.5,
                  strokeWeight: 1,
                  fillColor: color,
                  fillOpacity: (winner.votes / record.totalvotes) * 1.25,
                  data: to_template,
                  zIndex: 500,
                  fips: d.properties.COUNTYFP,
                  mouseover: function(d) {
                      $("#results").html(results_template(this.data));
                      console.log(this.fips);
                        this.setOptions({
                          strokeWeight: 4,
                          strokeOpacity: 0.75,
                          zIndex: 505
                        });
                  },
                  mouseout: function() {
                    $("#results").html(results_template(""));
                    this.setOptions({
                      strokeWeight: 1,
                      strokeOpacity: 0.5,
                      zIndex: 500
                    });
                  }
                });
         });
        // hide loading indicator
        $('#loading').html('');

        function updateMap(party) {
            // show loading indicator
            $('#loading').html('Loading ...');
            var w = getUniqueWinners(party);

            var key_data_to_template = {
                cands: []
            };

            _.each(w, function(s) {
                if (s && s !== "") {
                    key_data_to_template.cands.push({
                        "name": s,
                        "color": colors[s]
                    });
                } else {
                    key_data_to_template.cands.push({
                        "name": "No results",
                        "color": "white",
                        "border": "#aaa"
                    });
                }
            });

            $("#key").html(key_template(key_data_to_template));

            _.each(gmap.polygons, function(d) {
                var record = fetchResults(d.fips, party);
                    var winner = _.max(record.candidates, function(d) { return d.votes; } );
                    var color;
                    if (record.isTie) {
                        color = "#000000";
                    }
                    else if (record.totalvotes < 1) {
                        color = "#ffffff";
                    }
                    else {
                        color = colors[winner.name];
                    }
                    var to_template = {
                        results: {
                            county: record.countyname,
                            totalvotes: record.totalvotes,
                            candidates: _.sortBy(record.candidates, function(d) { return d.votes; }).reverse()
                        }
                    };
                    d.setOptions({
                        fillColor: color,
                        fillOpacity: (winner.votes / record.totalvotes) * 1.25,
                        data: to_template
                    });
            });










            // hide loading indicator
            $('#loading').html('');
        }

        });
        });

}(jQuery, _));
