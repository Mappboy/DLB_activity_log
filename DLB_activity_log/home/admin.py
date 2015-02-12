__author__ = 'Drogon'
from models import Linker, Dataset, Batch, Stage, Client, DLUId
from django.contrib import admin

#class IDInline(admin.StackedInline):
#    model = DLUId
#
#class LinkInline(admin.StackedInline):
#    model = Linker
#
#class ClientInLine(admin.StackedInline):
#    model = Client
#
#class DatasetAdmin(admin.ModelAdmin):
#    inlines = [IDInline, LinkInline, ClientInLine]

admin.site.register(Linker)
admin.site.register(Dataset)
admin.site.register(Batch)
admin.site.register(Stage)
admin.site.register(Client)
admin.site.register(DLUId)