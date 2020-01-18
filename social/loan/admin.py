from django.contrib import admin
from .models import User, Rule, MyUser

admin.site.register(User)
admin.site.register(Rule)
admin.site.register(MyUser)
