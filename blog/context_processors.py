from .models import Category

def basetest(request):

    categories = Category.objects.values_list("title", flat=True)
    return {
        'categories': categories
    }