from django.contrib import admin

# Register your models here.
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
  list_display = ('name','email', 'contact_date')
  list_display_links = ('name', 'email')
  search_fields = ('name','email')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)
