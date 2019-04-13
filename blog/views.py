from django.shortcuts import render
#.はカレントディレクトリ、もしくはカレントアプリケーションのこと。
#views.pyとmodels.pyは同じディレクトリに置いてあるので.で記述できる
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #{}のなかにテンプレートに渡す値を入れる
    #{}のなかに引数を記述するときは名前と値をセットにする ''で囲んだほうが名前、後ろは値、クエリセットのこと
    return render(request,'blog/post_list.html',{'posts':posts})
