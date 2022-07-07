$(function () {
    $(document).scroll(function () {
        var $nav = $(".main-header");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
      });
  });