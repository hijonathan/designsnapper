(function() {
  $(function() {
    var iframe;
    iframe = jQuery('<iframe width="100%" height="100%"></iframe>');
    console.log(iframe);
    iframe.load(function() {
      var script;
      try {
        script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = window.location.protocol + '//' + window.location.host + '/static/js/visual-selector.js';
        return this.contentDocument.getElementsByTagName('head')[0].appendChild(script);
      } catch (e) {
        return alert(e);
      }
    });
    iframe.attr('src', '/example-framed-content/?url=' + window.page_url);
    return jQuery('#visual-selector').append(iframe);
  });
}).call(this);
