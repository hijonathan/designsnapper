(function() {
  $(function() {
    var before_hover, header, header_opacity;
    header = $('header');
    header_opacity = header.css('opacity');
    $(window).scroll(function() {
      var current_position;
      current_position = $(window).scrollTop();
      if (current_position > 0) {
        header.stop(false, true).animate({
          opacity: .35
        });
        return header_opacity = .35;
      } else if (current_position === 0) {
        header.stop(true).animate({
          opacity: 1
        });
        return header_opacity = 1;
      }
    });
    before_hover = header.css('opacity');
    header.mouseenter(function() {
      return header.animate({
        opacity: 1
      });
    });
    header.mouseleave(function() {
      return header.animate({
        opacity: header_opacity
      });
    });
    return $.ajax({
      type: "GET",
      url: "/static/js/compiled/gallery.js",
      dataType: "script"
    });
  });
}).call(this);
