$(function () {
    let timer = null;
    let xhr = null; // async
    $('.user_popup').hover(
        function (event) {
            // mouse in event handler
            let elem = $(event.currentTarget);
            timer = setTimeout(function () {
                timer = null;
                xhr = $.ajax(
                    '/accounts/profile/' + elem.first().text().trim() + '/popup/').done(
                    function (data) {
                        xhr = null;
                        elem.popover({
                            trigger: 'manual',
                            html: true,
                            animation: false,
                            container: elem,
                            content: data
                        }).popover('show');
                    }
                );
            }, 1000);
        },
        function (event) {
            // mouse out event handler
            let elem = $(event.currentTarget);
            if (timer) {
                clearTimeout(timer);
                timer = null;
            } else if (xhr) {
                xhr.abort();
                xhr = null;
            } else {
                elem.popover('dispose');
            }
        }
    );
});
