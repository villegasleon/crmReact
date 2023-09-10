from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Record
import json
from corsheaders import cors_headers
import traceback
import os

# Vista para procesar solicitudes POST y habilitar CORS si es necesario
@csrf_exempt
def home(request):
    if request.method == 'POST':
        # Procesar el inicio de sesión desde React
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Sesión iniciada correctamente'}, status=200)
        else:
            return JsonResponse({'message': 'Hubo un error al iniciar sesión'}, status=400)
    else:
        # Obtener todos los registros para mostrar con React
        records = Record.objects.all()
        records_data = [{'id': record.id, 'name': record.name} for record in records]
        return JsonResponse({'records': records_data})

""""                
def logout_user(request):
    logout(request)
    messages.success(request, "Has cerrado tu sesión")
    return redirect ('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate  and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "¡Te has registrado exitosamente! ¡Bienvenido!")
            return redirect('home')
    else:
        form= SignUpForm()
        return render(request, 'register.html',{'form':form})
    
    return render(request, 'register.html', {'form':form})
    
def customer_record(request, pk):
	if request.user.is_authenticated:
		# Buscamos en los registros mediante Id
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "Debes iniciar sesión para ver esa página")
		return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it= Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Registro eliminado exitosamente")
        return redirect('home')
    else:
        messages.success(request, "Debes iniciar sesión para esta acción")
        return redirect('home')
    
def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Registro guardado")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request, "Debes haber iniciado sesión para esta acción")
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Registro actualizado")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "Es necesario iniciar sesión para esta acción")
		return redirect('home')

def search_record(request):
    user_authenticated = request.user.is_authenticated
    
    if user_authenticated and request.method == "POST":
        form = SearchRecordForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            customer_record = Record.objects.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(addres__icontains=search_query) |  # Cambiar "address" a "addres"
                Q(city__icontains=search_query) |
                Q(state__icontains=search_query) |
                Q(zipcode__icontains=search_query)
            )
        else:
            form = SearchRecordForm()
            customer_record = []
    else:
        form = SearchRecordForm()
        customer_record = []

    return render(request, 'search_record.html', {'form': form, 'customer_record': customer_record})

#Creacion de calendario para eventos, se instalo la libreria pip install django-scheduler
@login_required
def calendar_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            messages.success(request, "Tu evento ha sido registrado")
            return redirect('calendar_view')
    else:
        form = EventForm()

    events = Event.objects.all() 

    context = {
        'form': form,
        'events': events,
    }
    return render(request, 'calendar_view.html', context)

#funcion para visualizar un calendario integrado con los eventos agendados
@login_required
def calendar_activity(request):
    events = Event.objects.all()  # Consulta tus eventos en la base de datos
    serialized_events = []  # Lista para almacenar eventos serializados

    for event in events:
        # Serializa cada evento en el formato necesario para FullCalendar
        serialized_event = {
            'title': event.title,
            'description': event.description,
            'start': event.start_time.isoformat(),  # Asegúrate de formatear las fechas y horas adecuadamente
            'end': event.end_time.isoformat(),
        }
        serialized_events.append(serialized_event)

    # Renderiza la vista 'calendar_activity.html' junto con los datos JSON de los eventos
    return render(request, 'calendar_activity.html', {'events_data': serialized_events})
    """