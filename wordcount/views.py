from django.http import HttpResponse
from django.shortcuts import render
#import collections
import operator

def home(request):
    return render(request, "home.html") #{'hithere':'This is me'}),'name':'aman'})

def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)

    wordlist=fulltext.split()
    worddictionary={}
    #worddictionary= collections.Counter(wordlist)
    for word in wordlist:
        if word.isalpha():
            if word in worddictionary:
                worddictionary[word]+=1
            else:
                worddictionary[word]=1
        else:continue
    sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddictionary':sortedwords})

def about(request):
    return render(request,'about.html')

"""def eggs(request):
    return HttpResponse("<h1>Eggs are great</h1>")"""