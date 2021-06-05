from django.template import Library
from django.utils.html import mark_safe

register = Library()


@register.filter
def comments_filter(comments_list):
    """ Comments filter """

    res = """
          <ul style="list-style-type: none;">
              <div class="col-md-12 mt-2">
                  {}
              </div>
          </ul>
          """
    i = ''
    for comment in comments_list:
        i += f"""
             <li>
                 <div class="col-md-12 mb-2 mt-2 p-0">
                     <span class="user_popup">
                         <a href="{comment['author'].get_absolute_url()}">
                             <img class="img-80 img-fluid" src="{comment['author'].avatar.url}" alt="">
                             <small>{comment['author']}</small>
                         </a>
                     </span> | Published: {comment['timestamp']}
                     <hr>
                     <p>{comment['text']}</p>
                     <a href="#" class="reply" data-id="{comment['id']}" data-parent={comment['parent_id']}>Reply</a>
                     <form action="" method="post" class="comment-form form-group" id="form-{comment['id']}" style="display: none;">
                         <textarea type="text" class="form-control" name="comment-text"></textarea><br>
                         <input type="submit" class="btn btn-primary submit-reply" data-id="{comment['id']}" data-submit-reply="{comment['parent_id']}" value="Submit">
                     </form>
                 </div>
             </li>
             """
        if comment.get('children'):
            i += comments_filter(comment['children'])
    return mark_safe(res.format(i))
