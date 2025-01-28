from django.contrib import admin
from Services.models import StockList, Member, Attendance, Salary


class ServicesAdmin(admin.ModelAdmin):
    list_display=('date','opening','daily_use','balance')

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('member', 'date', 'time_in', 'time_out', 'present')
    list_filter = ('date', 'present')  # Filter by date and present status for easy management

# Register your models here.
admin.site.register(StockList, ServicesAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Salary)
