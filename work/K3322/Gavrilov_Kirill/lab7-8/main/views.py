from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import ContactMessage


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message'],
                score=int(form.cleaned_data['score']) if form.cleaned_data.get('score') else None,
                service=form.cleaned_data.get('service', []),
            )
            messages.success(request, "Сообщение успешно отправлено!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})


