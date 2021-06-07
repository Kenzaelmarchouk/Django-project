from django.contrib import admin
from .models import Article
from .models import Formule
from .models import Formule1
from .models import Formule2
# Register your models here.
admin.site.register(Article)
admin.site.register(Formule)
admin.site.register(Formule1)
admin.site.register(Formule2)
