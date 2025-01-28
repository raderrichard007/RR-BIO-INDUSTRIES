from django import forms
from .models import Member,Attendance

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['member', 'date', 'time_in', 'time_out', 'present']
