"use strict";
(function() {
    var cx = "008572255874373046644:chip1p1uf-4";
    var gcse = document.createElement("script");
    gcse.type = "text/javascript";
    gcse.async = true;
    gcse.src = (document.location.protocol == "https:" ? "https:" : "http:") + "//www.google.com/cse/cse.js?cx=" + cx;
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(gcse, s);
})();

function checkBck() {
    jQuery(".gsc-input input").attr("placeholder", "Buscar en la Universidad");
    if (!jQuery(".gsc-search-button input").attr("src")) {
        window.setTimeout(function() {
            checkBck();
        }, 100);
    }
}
checkBck();
jQuery(document).ready(function($) {
    prepare_content_menu();
    $("#unalOpenMenuServicios, #unalOpenMenuPerfiles").on("click", function(e) {
        var $target = $(this).data("target");
        var $mOffset = $(this).offset();
        $($target).css({
            top: $mOffset.top + $(this).outerHeight(),
            left: $mOffset.left
        });
    });

    function serviceMenuStatus() {
        var $s = $("#services");
        $s.height($(window).height());
        $("ul", $s).height($(window).height());
        if ($(".indicator", "#services").hasClass("active")) {
            $s.css({
                right: 0
            });
        } else {
            $s.css({
                right: parseInt($("#services").width()) * -1
            });
        }
    }
    $(".indicator", "#services").click(function() {
        $(this).toggleClass("active");
        serviceMenuStatus();
    });
    $(window).resize(function() {
        $(".open").removeClass("open");
        if ($(window).width() > 767) {
            $("#services").css({
                right: parseInt($("#services").width()) * -1,
                left: "auto",
                top: "auto"
            });
            $("#bs-navbar").removeClass("in");
            serviceMenuStatus();
        } else {
            $(".indicator", "#services").removeClass("active");
        }
    });
    $("#services").css({
        right: parseInt($("#services").width()) * -1
    });
    serviceMenuStatus();
});

function prepare_content_menu(){
    var $content_subdominio = $( "#subdominio" ).html();
    $( "#container_subdominio_mobil" ).html( $content_subdominio );

    var $content_buscador = $( "#buscador" ).html();
    $( "#container_buscador_mobil" ).html( $content_buscador );

    var $content_mainmenu = $('#main_menu_container').clone().find(".menu_sedes").remove().end().html()
    $( "#container_mainmenu_mobil" ).html( $content_mainmenu );

    var $conten_sedes = $( "#sedes" ).html();
    $( "#container_sedes_mobil" ).html( $conten_sedes );

    var $conten_servicios = $( "#servicios" ).html();
    $( "#container_servicios_mobil" ).html( "<ul>" + $conten_servicios + "</ul>");

    var $conten_profiles = $( "#profiles" ).html();
    $( "#container_profiles_mobil" ).html( $conten_profiles );
}
