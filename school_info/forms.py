from django import forms

from school_info.models import Teacher, Group


class TeacherForm(forms.ModelFormForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "birth_date"]

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) > 50:
            raise forms.ValidationError("Name is too long!")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if len(last_name) > 50:
            raise forms.ValidationError("Surname is too long!")
        return last_name


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["group_name", "teacher_name"]

    def clean_group_name(self):
        group_name = self.cleaned_data["group_name"]
        if len(group_name) > 50:
            raise forms.ValidationError("Name is too long!")
        return group_name
