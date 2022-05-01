from django.contrib import admin
from main.models import Department, Member, Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['member', 'name', 'description', 'date']

    
    '''
    list_filter = ('status', 'created', 'name')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    '''


admin.site.register(Department)
admin.site.register(Member)
