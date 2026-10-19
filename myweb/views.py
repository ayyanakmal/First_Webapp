import operator

from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render (request,'index.html')


def download(request):
    return render(request,'index.html',{'key':'hi'})

def result(request):
    article=request.GET['article']
    word=article.split()
    count=len(word)
    dic_words={}
    for wor in word:
        if wor in dic_words:
            dic_words[wor]+=1
        else:
            dic_words[wor]=1
    sor=sorted(dic_words.items(), key=operator.itemgetter(1),reverse=True)
    return render(request,'result.html',{'article':article,'word_count':count,'dic_words':sor})
