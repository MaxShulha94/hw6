from django import forms

from .models import Group


class TeacherForm(forms.Form):
    first_name = forms.CharField(label="Teacher's first name", max_length=150)
    last_name = forms.CharField(label="Teacher's last name", max_length=50)
    birth_date = forms.DateField(label="Teacher's birthdate 'YYYY-MM-DD'")

    def clean_name(self):
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        birth_date = self.cleaned_data["birth_date"]
        if len(first_name) > 50:
            raise forms.ValidationError("Name is too long!")
        return first_name, last_name, birth_date


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_name', 'teacher_name']

    def clean_name(self):
        group_name = self.cleaned_data["group_name"]
        if len(group_name) > 50:
            raise forms.ValidationError("Name is too long!")
        return group_name
