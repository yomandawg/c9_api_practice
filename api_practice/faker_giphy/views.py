from django.shortcuts import render
from .models import Job
from faker import Faker
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def pastlife(request):
    return render(request, 'pastlife.html')
    
def result(request):
    name = request.GET.get('name')
    fake = Faker('ko_KR')

    person = Job.objects.filter(name=name).first()
    if person:
        job = person.job
    else:
        job = fake.job()
        person = Job(name=name, job=job)
        person.save()
    
    api_key = 'ca6434XaDdudJeioOqvblYqQatskcaaY'
    data = requests.get(f"http://api.giphy.com/v1/gifs/search?q={job}&api_key={api_key}&limit=1").json()
    try: image = data.get('data')[0].get('images').get('fixed_width').get('url')
    except: image = ''
    

    try: naver_image = naver_data
    except: naver_image = ''

    context = {'name': name, 'job': job, 'image': image}
    return render(request, 'result.html', context)