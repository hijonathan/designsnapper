(function() {
  $(function() {
    return $("a.menu").click(function() {
      console.log(this);
      $(this).parent("li").toggleClass('open');
      return false;
    });
  });
}).call(this);
