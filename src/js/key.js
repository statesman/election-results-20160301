var Key = (function($, JST, _){

  function Key(el, map) {
    this.$el = $(el);
    this.map = map;
  }

  Key.prototype.add = function(data, filter) {
    var self = this;
    var optEl = $(JST.key_item(data));
    optEl.appendTo(this.$el);
    if(filter) {
      optEl.on('mouseenter', function() {
        self.map.showSupport(filter);
      })
      .on('mouseleave', function() {
        self.map.hideSupport();
      });
    }
    else {
      optEl.addClass('disabled');
    }
  };

  Key.prototype.destroy = function() {
    this.$el.children('a').remove();
  };

  return Key;

}(jQuery, JST, _));
