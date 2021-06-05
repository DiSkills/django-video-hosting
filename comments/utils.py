

def get_children(queryset_child):
    """ Get comments children """

    res = []
    for comment in queryset_child:
        c = {
            'id': comment.id,
            'text': comment.text,
            'timestamp': comment.timestamp.strftime('%d-%m-%Y %H:%m'),
            'author': comment.user,
            'is_child': comment.is_child,
            'parent_id': comment.get_parent,
        }
        if comment.comment_children.exists():
            c['children'] = get_children(comment.comment_children.all())
        res.append(c)
    return res


def create_comments_tree(queryset):
    """ Create comments tree """

    res = []
    for comment in queryset:
        c = {
            'id': comment.id,
            'text': comment.text,
            'timestamp': comment.timestamp.strftime('%d-%m-%Y %H:%m'),
            'author': comment.user,
            'is_child': comment.is_child,
            'parent_id': comment.get_parent,
        }
        if comment.comment_children:
            c['children'] = get_children(comment.comment_children.all())
        if not comment.is_child:
            res.append(c)
    return res
