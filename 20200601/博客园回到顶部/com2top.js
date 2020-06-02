$(function () {
    // 默认是隐藏“回到顶部”按钮
    $("#back-top").hide();
    // 滚动距离顶部 500 像素时 淡入、淡出
    $(window).scroll(function () {
        if ($(this).scrollTop() > 500) {
            $('#back-top').fadeIn();
        } else {
            $('#back-top').fadeOut();
        }
    });
    // 回到顶部，点击事件
    $('#back-top a').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
});
com2top.js