from django.template import Library
from django.utils.html import mark_safe

register = Library()


@register.filter
def comments_filter(comments_list):
    res = """
          <ul>
              {}
          </ul>
          """
    i = ''
    for comment in comments_list:
        i += f"""
             <li>
                 {comment['id']}
             </li>
             """
        if comment.get('children'):
            i += comments_filter(comment['children'])
    return mark_safe(res.format(i))
