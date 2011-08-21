$ ->
    header = $('header')
    header_opacity = header.css('opacity')

    $(window).scroll ->
        current_position = $(window).scrollTop()

        if current_position > 0
            header.stop(false, true).animate opacity: .35
            header_opacity = .35
        else if current_position == 0
            header.stop(true).animate opacity: 1
            header_opacity = 1
    
    before_hover = header.css('opacity')
    header.mouseenter ->
        header.animate opacity: 1
    header.mouseleave ->
        header.animate opacity: header_opacity
    
    # # Gallery
    # $.ajax({
    #    type: "GET",
    #    url: "/static/js/compiled/gallery.js",
    #    dataType: "script"
    #  });