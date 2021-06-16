from django.contrib import admin
from .models import Level, Word

admin.site.site_header = 'Hindi Script App admin'
admin.site.site_title = 'Hindi Script App admin'
#admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = 'Hindi Script App administration'

# Register your models here.
admin.site.register(Level)
admin.site.register(Word)
