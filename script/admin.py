from django.contrib import admin
from .models import Level, Word

admin.site.site_header = 'Hindi Script App Admin'
admin.site.site_title = 'Hindi Script App Admin'
admin.site.index_title = 'Hindi Script App Administration'

# Register your models here.
admin.site.register(Level)
admin.site.register(Word)
