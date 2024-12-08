from django.contrib import admin
from layout.models import LayoutModel, PageModel

admin.site.register([LayoutModel,PageModel])