from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return f"Name: {self.first_name}, Surname: {self.last_name}, Date of birth: {self.birth_date};"


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    teacher_name = models.ForeignKey(
        Teacher, on_delete=models.PROTECT, related_name="groups", default=None
    )

    def __str__(self):
        return self.group_name
