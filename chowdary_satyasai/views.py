from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from pathlib import Path
from .forms import PersonForm

def person_list(request):
    people = Person.objects.all()
    print(Path(__file__).resolve().parent/'templates')
    return render(request, 'person_list.html', {'people': people})

def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'person_detail.html', {'person': person})

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(initial=request.POST)  # Pass the filled form data
        
    return render(request, 'person_form.html', {'form': form, 'create_person': True})

def edit_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_detail', pk=person.pk) 
    else:
        form = PersonForm(instance=person)
    
    return render(request, 'person_form.html', {'form': form, 'create_person': False})


def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)

    if request.method == 'POST':
        confirm = request.POST.get('confirm', '')

        if confirm == 'yes':
            person.delete()
            return redirect('person_list')

    return render(request, 'confirm_delete.html', {'person': person})
