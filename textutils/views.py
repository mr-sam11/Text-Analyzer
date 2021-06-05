from django.http import HttpResponse
from django.shortcuts import render

def index(request):

       return render(request,'index.html')

def analyze(request):
       #get the data from index page
       djtext = request.POST.get('text', 'default')
       removepunc = request.POST.get('removepunc', 'off')
       fullcaps =request.POST.get('fullcaps','off')
       newlineremover=request.POST.get('newlineremover','off')
       extra =request.POST.get('extraspaceremover','off')
       charcount=request.POST.get('charcount','off')
       # bydefault it will return on

         # analyze text

       if removepunc == "on":


           analyzed =""
           punctuations = ''''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
           for char in djtext:
                if char not in punctuations:
                   analyzed=analyzed+char
           params = {'purpose':'Removed punctuatuions','analyzed_text':analyzed}
           djtext = analyzed

       #capitalize Text
       if fullcaps == "on":
              analyzed = ""
              for char in djtext:
                     analyzed = analyzed + char.upper()

              params = {'purpose':'Change to Upper Case','analyzed_text':analyzed}

              djtext=analyzed

       #newlineremover
       if newlineremover == "on":
             analyzed=""
             for char in djtext:
                    if char != "\n" and char!="\r":
                           analyzed = analyzed + char

             params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}

             djtext = analyzed

       if extra == "on":
              analyzed = ""
              for index,char in enumerate(djtext):
                  if not(djtext[index] == " " and  djtext[index+1] == " "):
                         analyzed =analyzed + char

              params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}

              djtext = analyzed

        #Charecter Counter
       if  charcount == "on":
              count = 0
              for index in range(0,len(djtext)):
                     if djtext[index]!='':
                            count=count+1;

              params = {'purpose': 'count charecter', 'analyzed_text': count}

              djtext = analyzed

       #check box is on
       if(removepunc != "on"  and   charcount != "on" and extra != "on" and  fullcaps != "on" and  newlineremover != "on") :
             return HttpResponse("Error")
       return render(request, 'analyze.html', params)