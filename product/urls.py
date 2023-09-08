from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('<slug:category_slug>/', views.category,name="category"),

    path('detail/<slug:subcategory_slug>/', views.subcategory,name="subcat"),

    path('search',views.search,name="search"),
    path('<slug:subcategory_slug>/<slug:product_slug>/', views.product,name="product"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)