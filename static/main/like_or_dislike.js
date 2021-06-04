// get csrf_token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

const LIKE_OR_DISLIKE = document.querySelectorAll('.like_or_dislike');
const LIKE_OR_DISLIKE_ARRAY = Array.prototype.slice.call(LIKE_OR_DISLIKE);
const ACT = document.querySelectorAll('.act');

// request on server
LIKE_OR_DISLIKE_ARRAY.forEach(item =>
    item.addEventListener('click', () => {
        const {itemValue} = item.dataset;
        item.parentNode.dataset.totalValue = item.dataset.itemValue;

        let url_path = ACT[0].action;
        $.ajax({
            type: 'POST',
            url: url_path,
            data: {'csrfmiddlewaretoken': csrftoken, 'act': item.value},
            success: function() {
                location.reload();
            }
        });
        return false;
    })
);
