from django.contrib import admin
from .models import Application, Guarantor, Document
# Register your models here.
admin.site.register(Application)
admin.site.register(Guarantor)
admin.site.register(Document)


