(function() {
  $(function() {
    var imgWidth, page, pageImg, windowHeight, windowWidth;
    windowWidth = window.innerWidth - 20;
    windowHeight = window.innerHeight;
    page = $('.page-gallery .page');
    pageImg = $('.page-gallery .page img');
    pageImg.css({
      height: windowHeight - 230
    }).css({
      'visibility': 'visible'
    });
    imgWidth = $('.page-gallery .page').first().width();
    $('.page-gallery').css({
      width: screenshotCount * (imgWidth + 40) - 40
    });
    $('.toggle-loupe').click(function() {
      $('.toggle-loupe span').toggle();
      if (pageImg.data('loupe')) {
        return pageImg.removeData();
      } else {
        return pageImg.loupe({
          width: 320,
          height: 240
        });
      }
    });
    return $('.tile-pages').click(function() {
      $('.tile-pages span').toggle();
      if ($('#content').hasClass('tiled')) {
        return page.fadeOut(function() {
          pageImg.css({
            width: 'auto',
            height: windowHeight - 230
          });
          imgWidth = $('.page-gallery .page').first().width();
          $('.page-gallery').css({
            width: screenshotCount * (imgWidth + 40) - 40
          });
          return $('#content').removeClass('tiled');
        }).fadeIn();
      } else {
        page.fadeOut();
        $('.page-gallery').animate({
          width: windowWidth
        }, function() {
          pageImg.css({
            height: 'auto',
            width: 240
          });
          return page.fadeIn();
        });
        return $('#content').addClass('tiled');
      }
    });
  });
}).call(this);
