from django.contrib import admin
from TM_User.models import Users
from TM_User.models import ExternalSyllabus
from TM_User.models import PSUSyllabus
from TM_User.models import TransferRequest
# Register your models here.
admin.site.register(Users)
admin.site.register(ExternalSyllabus)
admin.site.register(PSUSyllabus)
admin.site.register(TransferRequest)