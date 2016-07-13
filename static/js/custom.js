/*$(function setProject(e){
    $(this).parent('.phone').click(setProject(e));

})*/
$(function () {

    $('a.folio').fancybox();
    $('#portfolio').mixitup();

    $('.nav-tabs a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
    })
    $('.navbar-nav a').click(function (e) {
        e.preventDefault();
        $(this).parent('li').toggleClass('active');
        $(this).parent('li').siblings('.active').removeClass('active');


        //$(this).find("a").attr("href");
    })

    $('.phone').click(function (e) {
        api_gallery = ['/static/img/certs/certs_2.jpg', '/static/img/certs/certs_2.jpg', '/static/img/certs/certs_2.jpg'];
        api_titles = ['API Call Image 1', 'API Call Image 2', 'API Call Image 3'];
        api_descriptions = ['Description 1', 'Description 2', 'Description 3'];
        $.fn.prettyPhoto();
        $.prettyPhoto.open(api_gallery, api_titles, api_descriptions);
        return false;
    })


    $(".desktop").click(function (e) { // for each edit contact url
        e.preventDefault();
        // for each edit contact url
            //var url = $(this).data("form"); // get the contact form url
            //$("#cost_of_service").load(url, function () { // load the url into the modal

        $("#cost_of_service").modal('show'); // display the modal on url load

    })
     $('#costserv_acc').collapse({
          toggle: false
        })

      /*  var url = $(this).data("form"); // get the contact form url
        $("#cost_of_service").load(url, function() { // load the url into the modal
            $(this).modal('show'); // display the modal on url load
        });
        return false; // prevent the click propagation*/


       //
        //$('#myModal').modal('show');
       /* $(this).data('load-from');
        $("#cost_of_service").modal('show');
        /*return false;*/
         // выключaем стaндaртную рoль элементa
		/*var $place = $( "#cost_of_service" );
        $place.load($place.data('load-from') );*/


    /*
    $('#jump12').click(function (e){
       //window.open("", "_self");
        history.back();

    })*/
    $('.header .navbar-nav a').smoothScroll();


    $('#jump2top').css('bottom', '-100px');
    $(window).scroll(function () {
        var btn = $('#jump2top');
        if ($(this).scrollTop() > 100) {
            btn.stop().animate({ 'bottom': '0' }, 200);
        } else {
            btn.stop().animate({ 'bottom': '-100px' }, 200);
        }
    });

    $('#jump2top').smoothScroll();

    //setup email here
    $('#button-send').click(function (event) {
        $('#button-send').html('Sending E-Mail...');
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: 'contact_to',
            data: $('#contact_to').serialize(),
            success: function (html) {
                if (html.success == 1) {
                    $('#button-send').html('Send E-Mail');
                    $('#success').css({"color":"green"});
                    $('#success').html(html.status_text);
                    $('#success').show();
                }
                else {
                    $('#button-send').html('Send E-Mail');
                    $('#success').css({"color":"red"});
                    $('#success').html(html.status_text);
                    $('#success').show();
                }
            },
            error: function () {
                $('#button-send').html('Send E-Mail');
                $('#error').show();
            }
        });

    });

});
function scrollTo(elem) {
    $('body,html').animate({
        scrollTop: elem.offset().top
    }, 500);
}

function valemail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}