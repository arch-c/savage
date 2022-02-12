from django.contrib import admin
from .models import (Member, Product, Game, Partner)

admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Game)
admin.site.register(Partner)