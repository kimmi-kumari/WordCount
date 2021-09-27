from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    text = request.GET['text']
    wordList = text.split()
    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'text': text, 'sortedWords': sortedWords})

def about(request):
    return render(request, 'about.html')
