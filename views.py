# i have created this file    -  tanishk
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


# return HttpResponse("home")

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')


    #check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = ''':()-[]{};'"\,<>./?@#$%^&*_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        tani = {'purpose': 'removepunc', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', tani)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        tani = {'purpose': 'fullcaps', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', tani)

    if newlineremove == "on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        tani = {'purpose': 'newlineremove', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', tani)

    if extraspaceremover == "on":
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index] ==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        djtext = analyzed
        tani = {'purpose': 'extraspaceremover', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', tani)

    if charcount == "on":
        anal=0
        for char in djtext:
            anal=anal+1
        tani = {'purpose': 'charcount', 'analyzed_text': anal}
        #return render(request,'analyze.html',tani)

    if (removepunc != "on" and newlineremove != "on" and extraspaceremover != "on" and fullcaps != "on" and charcount != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', tani)


# def capfirst(request):
# return HttpResponse(''' "capitalizefirst" <a href="http://127.0.0.1:8000/newlineremove"> newlinrmv </a>''')

'''def newlineremove(request):
    return HttpResponse("newlineremove <a href='/'>back</a>")

def spaceremover(request):
    return HttpResponse("spaceremover")

def charcount(request):
    return HttpResponse("charcount")

'''
