from django.contrib import admin
from candidates.models import CandidateJobMap
from .models import Job


class CandidateInline(admin.TabularInline):
    model = CandidateJobMap

    def get_readonly_fields(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return []
        else:
            return ('candidate',)


class JobAdmin(admin.ModelAdmin):
    exclude = ('creater',)
    list_display = ('position_name', 'creater',)
    inlines = (CandidateInline,)

    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Job.objects.all()
        else:
            return Job.objects.filter(creater=request.user)

    def get_list_display(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return ('position_name', 'creater',)
        else:
            return ('position_name',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # assign the creater only on creation and not update
            obj.creater = request.user
            obj.save()


admin.site.register(Job, JobAdmin)
