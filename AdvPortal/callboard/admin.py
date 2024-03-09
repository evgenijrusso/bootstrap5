from django.contrib import admin
from .models import AdvUser, Advert, Category, Comment, AdditionalImage

# Register your models here.

admin.site.register(AdvUser)
admin.site.register(Advert)
admin.site.register(AdditionalImage)
admin.site.register(Category)
admin.site.register(Comment)

