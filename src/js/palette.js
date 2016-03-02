var Palette = (function() {

  function Palette(key) {
    this.key = key;
    this.colors = [
      '#1E44A8',
      '#1E8A0E',
      '#FFCC00',
      '#FF6600',
      '#4D1979',
      'red',
      'blue'
    ];
    this.partycolors = {
      'TIE': '#000000',
      'REP': '#B72B21',
      'LIB': '#E0C828',
      'DEM': '#1E44A8',
      'GRN': '#1E8A0E'
    };
    this.nextColor = 0;
    this.candidates = {};
    this.key.destroy();
  }

  Palette.prototype.set = function(candidate, color, label) {
    this.candidates[candidate] = color;
    var filter;
    if(candidate !== "For" && candidate !== "Tie" && typeof label == "undefined") {
      filter = candidate;
    }
    else {
      filter = null;
    }
    this.key.add({
      color: color,
      label: label || candidate
    }, filter);
  };

  Palette.prototype.get = function(candidate, party, label) {
    if(typeof this.candidates[candidate] === "undefined") {
      if(party === "") {
        this.set(candidate, this.colors[this.nextColor], label);
        this.nextColor++;
      }
      else {
        this.set(candidate, this.partycolors[party], label);
      }
    }
    return this.candidates[candidate];
  };

  return Palette;

}());
