from django.contrib import admin
from .models import Student

admin.site.site_header = 'Student Management Administration'
admin.site.site_title = 'Student Management Admin'
admin.site.index_title = 'Administration Dashboard'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_id',
        'first_name',
        'last_name',
        'gender',
        'date_of_birth',
        'contact_number',
    )
    list_display_links = ('student_id',)
    list_editable = (
        'first_name',
        'last_name',
        'gender',
        'date_of_birth',
        'contact_number',
    )
    search_fields = ('student_id', 'first_name', 'last_name', 'contact_number')
    list_filter = ('gender',)
    ordering = ('last_name', 'first_name')
    list_per_page = 25

    class Media:
        css = {
            'all': ('registration/admin.css',),
        }
