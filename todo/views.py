from django.shortcuts import render, redirect
from .models import Notes


def delete(request, num):
    Notes.objects.filter(id=num).delete()
    return redirect('home')


def edit(request, num):
    return redirect('home')


def add(request):
    Notes.objects.create(content="")
    return redirect('home')


def home(request, num=0):

    try:
        if request.method == 'POST':
            note_content = request.POST.get('list_content')
            note_edit = request.POST.get('edit')
            if note_edit is not "":
                Notes.objects.filter(id=note_edit).update(content=note_content)

        note_count = Notes.objects.all().count()
        if note_count == 0:
            Notes.objects.create(content="")

        note_count_again = Notes.objects.all().count()
        if note_count == 1:
            note_content_send = Notes.objects.all()
            return render(request, 'index.html', {'note': note_content_send,'x':1})

    except Exception as e:
        print(e)
    note_content_send = Notes.objects.all()
    return render(request, 'index.html', {'note': note_content_send})
