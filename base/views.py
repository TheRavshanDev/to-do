from django.shortcuts import render, redirect
from django.views import View
from .models import Todo
from django.contrib import messages

class HomeView(View):
    def get(self, request):
        todos = Todo.objects.filter(user=request.user)
        return render(request, 'bs4_todo_list.html',{'todos':todos})

    def post(self, request):
        todo = Todo.objects.create(
            user=request.user,
            title=request.POST['title']
        )
        return redirect('home')

class DeleteView(View):
    def get(self, request,pk):
        todo = Todo.objects.get(id=pk)
        if request.user == todo.user:
            todo.delete()
            return redirect('home')
        else:
            messages.error(request, "Something went wrong!")
            return redirect('login')