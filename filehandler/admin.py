from django.contrib import admin
from .models import ProfileData


# add this class here to display values in admin side

class ProfileDataAdmin(admin.ModelAdmin):
    list_display = ('name','profileFile')

# Register your models here.
admin.site.register(ProfileData,ProfileDataAdmin)