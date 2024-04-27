import random
import requests
from django.shortcuts import render
def shuffled_list(request):
     response = requests.get('https://freetestapi.com/api/v1/students')
     data = response.json()

     names = [student['name'] for student in data]
     random.shuffle(names)
     return render(request, 'templates/index.html', {"name": names})
  
