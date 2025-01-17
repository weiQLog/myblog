from django.shortcuts import render, redirect
from account.models import MyUser
from album.models import AlbumInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import ArticleTag, ArticleInfo, Comment
from django.urls import reverse
from django.db.models import F


def article(request, id, page):
    album = AlbumInfo.objects.filter(user_id=id)
    tag = ArticleTag.objects.filter(user_id=id)
    user = MyUser.objects.filter(id=id).first()
    if not user:
        return redirect(reverse('register'))
    ats = ArticleInfo.objects.filter(author_id=id).order_by('-created')
    paginator = Paginator(ats, 10)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger:
        pageInfo = paginator.page(1)
    except EmptyPage:
        pageInfo = paginator.page(paginator.num_pages)
    return render(request, 'article.html', locals())


def detail(request, id, aId):
    album = AlbumInfo.objects.filter(user_id=id)
    tag = ArticleTag.objects.filter(user_id=id)
    user = MyUser.objects.filter(id=id).first()
    if request.method == 'GET':
        ats = ArticleInfo.objects.filter(id=aId).first()
        atags = ArticleInfo.objects.get(id=aId).article_tag.all()
        cms = Comment.objects.filter(article_id=aId).order_by('-created')
        if not request.session.get('reading' + str(id) + str(aId), ''):
            reading = ArticleInfo.objects.filter(id=aId)
            reading.update(reading=F('reading') + 1)
            request.session['reading' + str(id) + str(aId)] = True
        return render(request, 'detail.html', locals())
    else:
        commentator = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        value = {'commentator': commentator,
                 'content': content, 'article_id': aId}
        Comment.objects.create(**value)
        kwargs = {'id': id, 'aId': aId}
        return redirect(reverse('detail', kwargs=kwargs))