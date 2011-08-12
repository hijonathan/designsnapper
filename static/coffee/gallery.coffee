$ ->
    windowWidth = window.innerWidth - 20
    windowHeight = window.innerHeight
    
    page = $('.page-gallery .page')
    pageImg = $('.page-gallery .page img')

    pageImg.css({ height: (windowHeight - 230) })
    .css({ 'visibility': 'visible'})

    imgWidth = $('.page-gallery .page').first().width()

    $('.page-gallery').css({ width: screenshotCount * (imgWidth + 40) - 40 })

    $('.toggle-loupe').click ->
        $('.toggle-loupe span').toggle()
        if pageImg.data('loupe')
            pageImg.removeData()
        else
            pageImg.loupe({ width: 320, height: 240 })

    $('.tile-pages').click ->
        $('.tile-pages span').toggle()
        if $('#content').hasClass('tiled')
            page.fadeOut( ->
                pageImg.css({ width: 'auto', height: (windowHeight - 230) })
                
                imgWidth = $('.page-gallery .page').first().width()

                $('.page-gallery').css({ width: screenshotCount * (imgWidth + 40) - 40 })
                $('#content').removeClass('tiled')
            ).fadeIn()
        
        else
            page.fadeOut()
            $('.page-gallery').animate({ width: windowWidth }, ->
                pageImg.css({ height: 'auto', width: 240 })
                page.fadeIn()
            )
            $('#content').addClass('tiled')