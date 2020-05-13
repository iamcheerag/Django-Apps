from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fullformBoxName']
    words = fulltext.split()

    wordDict = {}
    for word in words:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word] =  1

    
    return render(request,'count.html', {'fulltext':fulltext,'count':len(words),'wordDict':sorted(wordDict.items(),key = lambda x : x[0],reverse=True)})  



def about(request):
    return render(request,'about.html')