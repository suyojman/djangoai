from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from .models import Contact
from django.views.generic import ListView, DetailView
#home view for Contacts. Contacts are displayed in a list
class IndexView(ListView):
    template_name='contact/index.html'
    context_object_name = 'post_list'
    
    def get_queryset(self):
        return Contact.objects.all()
#Detail view (view Contact detail)
class ContactDetailView(DetailView):
    model=Contact
    template_name = 'contact/post-detail.html'

#New Contact view (Create new Contact)
def postview(request):
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = ContactForm()
    return render(request,'contact/post.html',{'form': form})

#Edit a Contact
def edit(request, pk, template_name='contact/edit.html'):
    contact= get_object_or_404(Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#Delete Contact
def delete(request, pk, template_name='contact/confirm_delete.html'):
    contact= get_object_or_404(Contact, pk=pk)    
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})