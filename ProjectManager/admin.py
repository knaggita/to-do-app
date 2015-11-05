import django.contrib.admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Q
from ProjectManager.models import ActionPlan, Contact, Task
from django.contrib.auth import authenticate


class StaffAdmin(UserAdmin):
    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        qs = qs.filter(Q(is_staff=True) | Q(is_superuser=True))
        return qs


class ContactAdmin(django.contrib.admin.ModelAdmin):
    model = Contact
    extra = 4


class ActionPlanAdmin(django.contrib.admin.ModelAdmin):
    model = ActionPlan
    extra = 6


django.contrib.admin.site.unregister(User)
django.contrib.admin.site.register(User, StaffAdmin)
django.contrib.admin.site.register(ActionPlan, ActionPlanAdmin)
django.contrib.admin.site.register(Contact, ContactAdmin)

