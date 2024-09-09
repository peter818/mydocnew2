from django.contrib import admin

# Register your models here.
from .models import Listing,Realtor

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'prices', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)  # 确保 'is_published' 在 'list_display' 中
    search_fields = ('title', 'description', 'address', 'price')
    list_per_page = 25
    
    def prices(self, obj):
        return obj.prices
    
admin.site.register(Listing, ListingAdmin)  
    
#class ListingAdmin(admin.ModelAdmin):
    #list_display = ('id', 'title', 'is_published', 'prices', 'list_date', 'realtor')
    #list_display_links = ('id,' 'title')
    #list_display_links = None
    #list_filter = ('realtor',)
    #list_editable = ('is_published',)
    #search_fields = ('title', 'description', 'address', 'price')
    #list_per_page = 25
    

