from django.contrib import admin
from .models import *

admin.site.site_header = "ezNoteAdmin"
admin.site.site_title = "ezNoteAdmin"
admin.site.index_title = "Easy to manage your notes online!"
admin.site.register(Note)

from django.contrib.auth.models import Group
admin.site.unregister(Group)