from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html') # Django는 모든 templates 폴더를 동등한 레벨로 찾음