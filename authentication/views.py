from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save
        if user is None:
            messagebox.showinfo('Log In Error', "There is no user with those credentials.")

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegistrationPage(FormView):
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        else:
            messagebox.showinfo('Sign Up Error', 'Ensure that passwords match, and have 8 characters, including a '
                'special character. Otherwise, try a different username, since all users must have a unique username.')
        return super(RegistrationPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegistrationPage, self).get(*args, **kwargs)


