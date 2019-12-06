from django.contrib import admin
from .models import Post
from .models import blog
from .models import enquery
# Register your models here.
admin.site.register(Post)
admin.site.register(blog)
admin.site.register(enquery)