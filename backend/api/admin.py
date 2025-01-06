from django.contrib import admin
from .models import CustomUser, Document, Course, Resource, Notification, Profile

admin.site.register(CustomUser)

# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('document_name', 'document_category', 'document_status', 'document_deadline')
    list_filter = ('document_category', 'document_status')
    search_fields = ('document_name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_title', 'course_unit', 'level')
    list_filter = ('level', 'current_semester')
    search_fields = ('course_code', 'course_title')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('category',)
    list_filter = ('category',)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('notification_subject', 'notification_date', 'is_read')
    list_filter = ('is_read', 'notification_date')
    search_fields = ('notification_subject', 'notification_body')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'matric_number', 'department', 'level')
    list_filter = ('department', 'level')
    search_fields = ('user__username', 'matric_number')