from django.shortcuts import render
from datetime import date
import requests, random, os

# Create your views here.
def index(request):
    context = {'msg': 'hello', 'name':'John'}
    return render(request, 'index.html', context)

# Valentine's Day Check
def isval(request):
    res = False
    if date.today().strftime("%m%d") == '0214':
        res = True
    return render(request, 'isval.html', {'res': res})

# Cubed number
def cube(request, number):
    res = number**3
    return render(request, 'cube.html', {'res': res})

# Palindrome Check
def ispal(request, words):
    res = False
    if words == words[::-1]:
        res = True
    return render(request, 'ispal.html', {'res': res})
    
# Randome Images
def image(request):
    return render(request, 'image.html')
    
# 사용자의 입력을 받을 페이지
def new(request):
    return render(request, 'new.html')

# artii API를 통해 ascii 아트로 변환하여 보여주는 페이지
def artii(request):
    # request.args.get
    word = request.GET.get('word')
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text.split("\n")
    font = random.choice(fonts)
    url = 'http://artii.herokuapp.com/make?text={}&font={}'
    res = requests.get(url.format(word, font)).text
    return render(request, 'artii.html', {'res': res, 'font': font})


# 사용자로부터 단어를 입력 받아 /result로 넘겨줌
def papago(request):
    return render(request, 'papago.html')

naver_id = os.getenv('NAVER_ID')
naver_secret = os.getenv('NAVER_SECRET')
headers = {'X-Naver-Client-Id': naver_id, 'X-Naver-Client-Secret': naver_secret}
url = "https://openapi.naver.com/v1/papago/n2mt"

# PAPAGO API 검색 결과를 보여줌
def result(request):
    word = request.GET.get('word')
    data = {'source': 'en', 'target': 'ko', 'text': word}
    res = requests.post(url, headers=headers, data=data)
    res_dict = res.json() # json parse해서 넘겨줌
    res = res_dict.get('message').get('result').get('translatedText')
    return render(request, 'result.html', {'res': res})