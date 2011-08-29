$ ->

    $("a.menu").click ->
        console.log(this)
        $(this).parent("li").toggleClass('open')
        return false