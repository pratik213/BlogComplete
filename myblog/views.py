from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy

class HomeView(ListView):
    model=Post
    template_name="home.html"
    # ordering=['-id']
    ordering=['-post_date']

    def get_context_data(self,*args ,**kwargs):
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args ,**kwargs)
        context["cat_menu"]=cat_menu
        return context
    




class ArticleDetail(DetailView):
    model=Post
    template_name="articles_detail.html"

    def get_context_data(self,*args ,**kwargs):
        cat_menu=Category.objects.all()
        context=super(ArticleDetail,self).get_context_data(*args ,**kwargs)
        stuff=get_object_or_404(Post,id=self.kwargs['pk'])

        liked=False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked=True
        total_likes=stuff.total_likes()
        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name="add_post.html"
    # fields='__all__'

class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name="add_comment.html"
    # fields='__all__'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)



class AddCategoryView(CreateView):
    model=Category
    # form_class=PostForm
    template_name="add_category.html"
    fields='__all__'

class EditPost(UpdateView):
    model=Post
    form_class=PostForm
    template_name="update_post.html"
    # fields=['title','body']

class DeletePost(DeleteView):
    model=Post
    template_name="delete.html"
    success_url="/"


def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    return render(request, "categories.html",{'cats':cats.title().replace('-',' '),'category_posts':category_posts})


def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request, "categories_list.html",{'cat_menu_list':cat_menu_list})


def LikeView(request,pk):
    post=get_object_or_404(Post,id=request.POST.get('post_id'))
    liked=False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        liked=False
    else:
        post.like.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article_detail',args=[str(pk)]))
