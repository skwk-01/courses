from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Courses, Memo
from .forms import CoursesForm, MemoForm

@login_required
def home(request):
    courses = Courses.objects.all()
    memo, created = Memo.objects.get_or_create(id=1, defaults={'memo': 'ここにメモを入力してください'})
    if request.method == 'POST':
        memo_form = MemoForm(request.POST, instance=memo)
        if memo_form.is_valid():
            memo_form.save()
            return redirect('home')
    else:
        memo_form = MemoForm(instance=memo)
        return render(request, 'courses/home.html', {'courses': courses, 'memo': memo, 'memo_form': memo_form})

@login_required
def edit_memo(request):
    memo = Memo.objects.get(id=1)
    if request.method == 'POST':
        new_memo = MemoForm(request.POST)
        if new_memo.is_valid():
            new_memo.save()
            return redirect('home')
        else:
            new_memo = MemoForm()
        return redirect('home')

@login_required
def add_times(request, pk):
    complete_course = get_object_or_404(Courses, pk=pk)
    complete_course.complete_times += 1
    complete_course.save() 
    return redirect('home')

@login_required
def decrease_times(request, pk):
    complete_course = get_object_or_404(Courses, pk=pk)
    complete_course.complete_times -= 1
    complete_course.save() 
    return redirect('home')

@login_required
def setting(request):
    courses = Courses.objects.all()
    new_course_form = CoursesForm()
    return render(request, 'courses/setting.html', {'courses': courses, 'new_course': new_course_form})

@login_required
def add_courses(request):
    if request.method == 'POST':
        new_course = CoursesForm(request.POST)
        if new_course.is_valid():
            new_course.save()
            return redirect('setting')
    else:
        new_course = CoursesForm()
    return render(request, 'courses/setting.html', {'new_course': new_course})

@login_required
def delete_courses(request, pk):
    courses = get_object_or_404(Courses, pk=pk)
    courses.delete()
    return redirect('setting')


