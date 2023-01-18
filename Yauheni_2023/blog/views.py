from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm



def blog_index(request):
    posts = Post.objects.all().order_by('-created_on') # сортировка в обратном порядке
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm() # создал экземпляр формы
    if request.method == 'POST': # если в реквесте, который пришел со страницы есть метод пост, тогда создается экземпляр класса с данными, которые пришли из реквест пост
        form = CommentForm(request.POST)
        if form.is_valid():# если форма валидная: всё хорошо, ошибок нет,все поля заполнены правильно, то создаем экземплат класса, чтобы записать туда данные
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post = post
            )
            comment.save()
            form = CommentForm()
        else:
            pass
    else:
        form = CommentForm()


    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments":comments,
        "form":form
    }
    return render(request, "blog_detail.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by('-created_on')
    context={
        'posts':posts,
        'categories':category
    }
    return render(request, "blog_category.html", context)