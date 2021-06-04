from .models import Category


def category_context_processors(request):
    """ Categories on pages """

    context = {'categories': Category.objects.all()}
    return context
