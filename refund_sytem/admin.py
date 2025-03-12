from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import RefundRequest, UserProfile


class RefundRequestResource(resources.ModelResource):
    class Meta:
        model = RefundRequest


class RefundRequestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RefundRequestResource
    list_display = (
        "order_number",
        "order_date",
        "first_name",
        "last_name",
        "email",
        "status",
    )
    list_filter = ("status", "created_at", "country")

admin.site.register(RefundRequest, RefundRequestAdmin)
admin.site.register(UserProfile)

