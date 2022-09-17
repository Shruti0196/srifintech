from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def plot(request):
    if request.method=="POST":
        chosenoption = request.POST.get('chosenoption')
        print(chosenoption)
        url = 'https://docker.api.srifintech.com/testassignment'
        payload = { "ticker" : chosenoption }
        response = requests.post(url, data = payload).json()
        print(response)
        return render(request,'result.html')
        

