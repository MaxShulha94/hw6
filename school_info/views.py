from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

from .forms import TeacherForm, GroupForm
from .models import Teacher, Group


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
        return redirect("teachers_list")
    return render(request, "teacher_form.html", {"form": form})


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers_list.html", {"teachers": teachers})


def group_form(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})
    form = GroupForm(request.POST)
    if form.is_valid():
        group_name = form.cleaned_data["group_name"]
        teacher_id = form.cleaned_data["teacher_name"].id
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            raise Http404("Teacher does not exist")
        g = Group.objects.create(group_name=group_name, teacher_name=teacher)
        return redirect("groups_list")
    return render(request, "group_form.html", {"form": form})


def groups_list(request):
    groups = Group.objects.all()
    return render(request, "groups_list.html", {"groups": groups})


def print_groups(request):
    groups = Group.objects.all()
    group_list = "\n".join(
        [
            f"Group`s name: {group.group_name}, Curator: {group.teacher_name} "
            for group in groups
        ]
    )
    return HttpResponse(group_list)
