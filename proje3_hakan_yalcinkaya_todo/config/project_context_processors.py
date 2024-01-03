from todo.models import category

def global_category_context(request):
    return dict(
        # global_categories = category.objects.all() # bu eski olan
        global_categories = category.objects.filter(is_active=True)
    )