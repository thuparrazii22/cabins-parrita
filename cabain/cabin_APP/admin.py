from django.contrib import admin
from . import models as m
# Register your models here.

admin.site.register(m.Commune)
admin.site.register(m.Region)
admin.site.register(m.City)
admin.site.register(m.PaymentMethod)
admin.site.register(m.Bank)
admin.site.register(m.MeasureUnit)
admin.site.register(m.Product)
admin.site.register(m.Client)
admin.site.register(m.Bill)
admin.site.register(m.BillDetail)
admin.site.register(m.Project)
admin.site.register(m.ProjectDetail)
admin.site.register(m.Worker)
admin.site.register(m.ProjectWorker)
admin.site.register(m.Proveedor)
