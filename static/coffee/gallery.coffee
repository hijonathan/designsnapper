$ ->
    url = window.location.href;
    hashTag = url.substr(url.indexOf('#'));

    page = $('.page-gallery .page')
    pageImg = $('.page-gallery .page img')

    # Handle turning loupe on and off
    $('.toggle-loupe').click ->
        $('.toggle-loupe span').toggle()
        if pageImg.data('loupe')
            pageImg.removeData()
        else
            pageImg.loupe({ width: 320, height: 240 })

    # Handle tiled and full-height modes
    $('.tile-pages').click ->
        $('.tile-pages span').toggle()
        if not $('.page-gallery').hasClass('full')
            page.fadeOut( ->
                pageImg.css({ width: 958 })

                $('.page-gallery').addClass('full')
            ).fadeIn()
        
        else
            page.fadeOut( ->
                pageImg.css({ width: 298 })
                $('.page-gallery').removeClass('full')
                page.fadeIn()
            )
        guiders.next()

    # Enable the guided tour only if the hash exists
    if hashTag is "#tour"
        # Start guided tour
        guiders.createGuider({
            title: "Welcome to DesignSnapper."
            description: "DesignSnapper is a light-weight piece of software that monitors your competitors' websites to track and analyze changes over time. Click to get started.",
            buttons: [{name: "Next"}],
            id: "first",
            next: "second",
            overlay: true,
        })
        .show();

        guiders.createGuider({
            attachTo: ".page:first",
            title: "Beautiful, high-res snapshots."
            description: "We collect snapshots of the pages you're monitoring and show you a visual history of that page over time. In addition to our auto-generated annoations, you can also add your own.",
            buttons: [{name: "Close"},
                    {name: "Next"}],
            id: "second",
            next: "third",
            position: 3,
        });

        guiders.createGuider({
            attachTo: ".tile-pages",
            title: "A flexible interface.",
            description: "Sort and manipulate the changes as your archive gets richer over time. Go ahead: try it out.",
            buttons: [{name: "Close, then tile.", onclick: guiders.hideAll}],
            id: "third",
            next: "fourth",
            position: 5,
            width: 500
        });

        guiders.createGuider({
            title: "Holy smokes, did you see that?",
            description: "Feel free to experiment with all the features we have to offer. Thanks for checking out DesignSnapper, brought to you by Vaporware.",
            buttons: [{name: "Finish", onclick: guiders.hideAll}]
            buttonCustomHTML: "<input type=\"checkbox\" id=\"stop_showing\" /><label for=\"stop_showing\" class=\"stopper\">Stop showing these. (Not implemented)</label>",
            id: "fourth",
            overlay: true
        });