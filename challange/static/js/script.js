$(function () {
    $("a").each(function () {
        if ($(this).prop("href") == window.location.href.split("?")[0]) {
            $(this).addClass("active");
            $(this).parents("li").addClass("active");
        }
    });
});
