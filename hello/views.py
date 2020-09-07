from django.http import HttpResponse
import re
from django.shortcuts import render
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from django.utils import timezone
from hello.models import LogMessage
from django.views.generic import ListView

# Replace the existing home function with the one below
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date =timezone.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})
