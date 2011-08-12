(function() {
  $(function() {
    var hashTag, imgWidth, page, pageImg, url, windowHeight, windowWidth;
    url = window.location.href;
    hashTag = url.substr(url.indexOf('#'));
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
    $('.tile-pages').click(function() {
      $('.tile-pages span').toggle();
      if ($('#content').hasClass('tiled')) {
        page.fadeOut(function() {
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
        $('#content').addClass('tiled');
      }
      return guiders.next();
    });
    if (hashTag === "#tour") {
      guiders.createGuider({
        buttons: [
          {
            name: "Next"
          }
        ],
        description: "Guiders are a user interface design pattern for introducing features of software. This dialog box, for example, is the first in a series of guiders that together make up a guide.",
        id: "first",
        next: "second",
        overlay: true,
        title: "Welcome to Guiders.js!"
      }).show();
      guiders.createGuider({
        attachTo: ".page:first",
        buttons: [
          {
            name: "Close"
          }, {
            name: "Next"
          }
        ],
        description: "For example, this guider is attached to the 12 o'clock direction relative to the attached element. The Guiders.js API uses a clock model to determine where the guider should be placed.<br/><br/>Attaching a guider to an element focuses user on the area of interest.",
        id: "second",
        next: "third",
        position: 3,
        title: "Guiders are typically attached to an element on the page."
      });
      guiders.createGuider({
        attachTo: ".toggle-loupe",
        buttons: [
          {
            name: "Close, then click on the clock.",
            onclick: guiders.hideAll
          }
        ],
        description: "Custom event handlers can be used to hide and show guiders. This allows you to interactively show the user how to use your software by having them complete steps. To try it, click on the clock.",
        id: "third",
        next: "fourth",
        position: 9,
        title: "You can advance guiders from custom event handlers.",
        width: 500
      });
      return guiders.createGuider({
        attachTo: ".tile-pages",
        buttons: [
          {
            name: "Finish",
            onclick: guiders.hideAll
          }
        ],
        buttonCustomHTML: "<input type=\"checkbox\" id=\"stop_showing\" /><label for=\"stop_showing\" class=\"stopper\">Stop showing these. (Not implemented)</label>",
        description: "Other aspects of the guider can be customized as well, such as the button names, button onclick handlers, and dialog widths. You'd also want to modify the CSS to your own project's style.",
        id: "fourth",
        position: 5,
        title: "Guiders can be customized.",
        width: 600
      });
    }
  });
}).call(this);
