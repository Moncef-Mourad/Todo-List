from django.contrib import admin
from .models import Todo,DeletedTask,ModificationHistory
# Register your models here.

admin.site.register(Todo)
admin.site.register(DeletedTask)
admin.site.register(ModificationHistory)

