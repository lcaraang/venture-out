$(document).ready(function () {
    $(function () {
        $('a').each(function () {
            if ($(this).prop('href') == window.location.href) {
                $(this).addClass('active');
            }
        });
    })
})
