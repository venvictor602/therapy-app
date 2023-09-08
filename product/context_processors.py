from product.models import Category,SubCategory

def main_categories(request):
    categories=Category.objects.all()
    return{'main_categories':categories}

def submain_categories(request):
    subcategories=SubCategory.objects.all()
    return{'submain_categories':subcategories}