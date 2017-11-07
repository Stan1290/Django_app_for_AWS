from .models import Users
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm



class IndexView(generic.ListView):
    model = Users
    template_name = 'acc_views/index.html'

    def get_queryset(self):
        return Users.objects.all()


class DetailView(generic.DetailView):
    model = Users
    template_name = 'acc_views/detail.html'


class AddUser(CreateView):
    model = Users
    template_name = 'acc_views/users_form.html'
    fields = ['first_name', 'last_name', 'email_address', 'user_picture']


class DeleteUser(DeleteView):
    model = Users
    success_url = reverse_lazy('acc_views:index')

class EditUser(UpdateView):
    model = Users
    fields = ['first_name', 'last_name', 'email_address', 'user_picture']

class UserFormView(View):
    form_class = UserForm
    template_name = 'acc_views/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

        #display filled out form and add it to the database
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

             #cleanned(normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.username = username
            user.set_password(password)
            user.save()


             #returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                     login(request, user)
                     return redirect('acc_views:index')

        return render(request, self.template_name, {'form': form})
























