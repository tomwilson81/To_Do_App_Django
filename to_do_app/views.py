from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    incomplete = Todo.objects.filter(complete=False).all()
    complete = Todo.objects.filter(complete=True).all()
    context = {
        'incomplete': incomplete,
        'complete': complete
    }
    return render(request, 'index.html', context)

# Create new task
def add(request):
    todo = Todo.objects.create(text=request.POST['todoitem'], complete=False)
    todo.save()
    print(todo)

    return redirect('to_do_app:index')

# Mark task as completed
def complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.complete = True
    todo.save()

    return redirect('to_do_app:index')

# Mark completed task as incomplete
def undo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.complete = False
    todo.save()

    return redirect('to_do_app:index')

# Delete tasks
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return redirect('to_do_app:index')