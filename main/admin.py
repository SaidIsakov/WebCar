from django.contrib import admin
from .models import Category,Cars
# Register your models here.


admin.site.register(Category)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    
    
admin.site.register(Cars, PostAdmin)