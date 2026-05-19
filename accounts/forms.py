from django import forms

class StudentForm(forms.Form):

    student_name = forms.CharField(
        max_length=100
    )