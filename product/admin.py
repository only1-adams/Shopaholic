from django.contrib import admin
from product.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status',]
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 2


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'status', 'image', 'quantity_instock',
                'available',  'slug', 'new_prod','popular', 'bestselling', 'featured']
    list_filter= ['category']
    list_display_links = ['title', 'category', 'status', 'image']
    readonly_fields = ['image_tag']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['new_prod', 'featured']


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(Carousel_a)
admin.site.register(Carousel_b)
admin.site.register(Carousel_c)
admin.site.register(Carousel_d)
