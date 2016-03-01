this["JST"] = this["JST"] || {};

this["JST"]["key_item"] = Handlebars.template({"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = "<a class=\"list-group-item key-item\">\n  <div class=\"color pull-left\" style=\"background-color:"
    + escapeExpression(((helper = (helper = helpers.color || (depth0 != null ? depth0.color : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"color","hash":{},"data":data}) : helper)))
    + ";\"></div>";
  stack1 = ((helper = (helper = helpers.label || (depth0 != null ? depth0.label : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"label","hash":{},"data":data}) : helper));
  if (stack1 != null) { buffer += stack1; }
  return buffer + "\n</a>\n";
},"useData":true});

this["JST"]["results"] = Handlebars.template({"1":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return escapeExpression(((helper = (helper = helpers.PCT || (depth0 != null ? depth0.PCT : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"PCT","hash":{},"data":data}) : helper)))
    + " ";
},"3":function(depth0,helpers,partials,data) {
  var stack1, buffer = "      <table class=\"table table-striped table-condensed\">\n        <thead>\n          <tr>\n            <th>Candidate</th>\n            <th class=\"text-right\">Votes</th>\n            <th class=\"text-right\">Share</th>\n          </tr>\n        </thead>\n        <tbody>\n";
  stack1 = helpers.each.call(depth0, (depth0 != null ? depth0.races : depth0), {"name":"each","hash":{},"fn":this.program(4, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "        </tbody>\n      </table>\n";
},"4":function(depth0,helpers,partials,data) {
  var helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression;
  return "            <tr>\n              <td>"
    + escapeExpression(((helper = (helper = helpers.candidate || (depth0 != null ? depth0.candidate : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"candidate","hash":{},"data":data}) : helper)))
    + "</td>\n              <td class=\"text-right\">"
    + escapeExpression(((helper = (helper = helpers.votes_str || (depth0 != null ? depth0.votes_str : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"votes_str","hash":{},"data":data}) : helper)))
    + "</td>\n              <td class=\"text-right\">"
    + escapeExpression(((helper = (helper = helpers.share || (depth0 != null ? depth0.share : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"share","hash":{},"data":data}) : helper)))
    + "</td>\n            </tr>\n";
},"6":function(depth0,helpers,partials,data) {
  return "      <p>Tap or hover over a race to see per-precinct vote counts.</p>\n";
  },"8":function(depth0,helpers,partials,data) {
  var stack1;
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.demos : depth0), {"name":"if","hash":{},"fn":this.program(9, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { return stack1; }
  else { return ''; }
  },"9":function(depth0,helpers,partials,data) {
  var stack1, helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = "\n  <div class=\"panel panel-default\">\n    <div class=\"panel-heading\">\n      <h3 class=\"panel-title\">Precinct "
    + escapeExpression(((helper = (helper = helpers.PCT || (depth0 != null ? depth0.PCT : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"PCT","hash":{},"data":data}) : helper)))
    + " 2010 demographics</h3>\n    </div>\n    <div class=\"panel-body\">\n";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.PCT : depth0), {"name":"if","hash":{},"fn":this.program(10, data),"inverse":this.program(13, data),"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "    </div>\n  </div>\n";
},"10":function(depth0,helpers,partials,data) {
  var stack1, lambda=this.lambda, escapeExpression=this.escapeExpression, buffer = "        <table class=\"table table-striped table-condensed\">\n          <thead>\n            <tr>\n              <th></th>\n              <th class=\"text-right\">Population</th>\n              <th class=\"text-right\">Voter-age population</th>\n            </tr>\n          </thead>\n          <tbody>\n";
  stack1 = helpers.each.call(depth0, (depth0 != null ? depth0.demos : depth0), {"name":"each","hash":{},"fn":this.program(11, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "            <tr>\n              <td><strong>Total</strong></td>\n              <td class=\"text-right\"><strong>"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.demos_sum : depth0)) != null ? stack1.sum : stack1), depth0))
    + "</strong></td>\n              <td class=\"text-right\"><strong>"
    + escapeExpression(lambda(((stack1 = (depth0 != null ? depth0.demos_sum : depth0)) != null ? stack1.sum_vap : stack1), depth0))
    + "</strong></td>\n            </tr>\n          </tbody>\n        </table>\n";
},"11":function(depth0,helpers,partials,data) {
  var stack1, helper, functionType="function", helperMissing=helpers.helperMissing, escapeExpression=this.escapeExpression, buffer = "              <tr>\n                <td>"
    + escapeExpression(((helper = (helper = helpers.group || (depth0 != null ? depth0.group : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"group","hash":{},"data":data}) : helper)))
    + "</td>\n                <td class=\"text-right\">";
  stack1 = ((helper = (helper = helpers.sum || (depth0 != null ? depth0.sum : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"sum","hash":{},"data":data}) : helper));
  if (stack1 != null) { buffer += stack1; }
  buffer += "</td>\n                <td class=\"text-right\">";
  stack1 = ((helper = (helper = helpers.sum_vap || (depth0 != null ? depth0.sum_vap : depth0)) != null ? helper : helperMissing),(typeof helper === functionType ? helper.call(depth0, {"name":"sum_vap","hash":{},"data":data}) : helper));
  if (stack1 != null) { buffer += stack1; }
  return buffer + "</td>\n              </tr>\n";
},"13":function(depth0,helpers,partials,data) {
  return "        <p>Tap or hover over a race to see per-precinct vote counts.</p>\n";
  },"compiler":[6,">= 2.0.0-beta.1"],"main":function(depth0,helpers,partials,data) {
  var stack1, buffer = "<div class=\"panel panel-default\">\n  <div class=\"panel-heading\">\n    <h3 class=\"panel-title\">Precinct ";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.PCT : depth0), {"name":"if","hash":{},"fn":this.program(1, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  buffer += "results</h3>\n  </div>\n  <div class=\"panel-body\">\n";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.PCT : depth0), {"name":"if","hash":{},"fn":this.program(3, data),"inverse":this.program(6, data),"data":data});
  if (stack1 != null) { buffer += stack1; }
  buffer += "  </div>\n</div>\n\n";
  stack1 = helpers['if'].call(depth0, (depth0 != null ? depth0.PCT : depth0), {"name":"if","hash":{},"fn":this.program(8, data),"inverse":this.noop,"data":data});
  if (stack1 != null) { buffer += stack1; }
  return buffer + "\n";
},"useData":true});