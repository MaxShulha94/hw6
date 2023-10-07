from django.shortcuts import render
from django.http import HttpResponse

from .models import Teacher, Group
from .forms import TeacherForm, GroupForm


def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        t = Teacher.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            birth_date=request.POST["birth_date"],
        )
        print("Teacher was created", t)
    return render(request, "teacher_form.html", {"form": form})


def print_teachers(request):
    teachers = Teacher.objects.all()
    teachers_list = []
    for teacher in teachers:
        if teacher.groups.exists():
            group_name = teacher.groups.first().group_name
        else:
            group_name = "No group."
        teachers_list.append(
            f"Name: {teacher.first_name}, Last name: {teacher.last_name}, Group: {group_name};"
        )
    return HttpResponse("\n".join(teachers_list))


def group_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "group_form.html", {"form": form})
    form = GroupForm(request.POST)
    if form.is_valid():
        g = Group.objects.create(
            group_name=request.POST["group_name"],
            teacher_first_name=request.POST["teacher_first_name"],
            teacher_last_name=request.POST["teacher_last_name"]

        )
        # group_name = request.POST.get("group_name")
        # teacher_first_name = request.POST.get("teacher_first_name")
        # teacher_last_name = request.POST.get("teacher_last_name")
        # teacher = Teacher.objects.filter(
        #     first_name=teacher_first_name, last_name=teacher_last_name
        # ).first()

    return render(request, "group_form.html", {"form": form})



def print_groups(request):
    groups = Group.objects.all()
    group_list = "\n".join(
        [
            f"Group`s name: {group.group_name}, Curator: {group.teacher_name} "
            for group in groups
        ]
    )
    return HttpResponse(group_list)
