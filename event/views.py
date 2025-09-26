from django.shortcuts import render, redirect , get_object_or_404
from .models import Event

# Create your views here.

# Display all Events
def displayEvents(request):
    events = Event.objects.all()
    categories = Event.CATEGORY
    return render(request, 'event/home.html', {'events': events, 'categories': categories})

#Add new event
def createEvent(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        category = request.POST.get('category')

        # Validate category
        if category not in dict(Event.CATEGORY).keys():
            return render(request, 'event/form.html', {'error': 'Invalid category selected'})

        # Create the event
        event = Event.objects.create(
            title=title,
            description=description,
            date=date,
            time=time,
            location=location,
            category=category
        )
        return redirect('home')

    return render(request, 'event/form.html' , {'category': Event.CATEGORY})

#update selected event
def editEvent(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.date = request.POST.get('date')
        event.time = request.POST.get('time')
        location = request.POST.get('location')
        event.category = request.POST.get('category')
        event.save()
        return redirect('home')

    # Pass CATEGORY_CHOICES for the dropdown
    category_choices = Event.CATEGORY
    return render(request, 'event/form.html', {'event': event, 'category': category_choices})

#delete selected event
def deleteEvent(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('home')

#filter events by category
def filterEvent(request, category):
    events = Event.objects.filter(category=category)
    return render(request,'event/home.html',{'events':events})