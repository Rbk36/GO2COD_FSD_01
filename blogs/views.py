from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
class Home(ListView):
    model=Post
    template_name='home.html'
    ordering=['-id']
    
class PostDetail(DetailView):
    model=Post
    template_name='post_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context=super(PostDetail, self).get_context_data(*args, **kwargs)
        my_like=get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes=my_like.total_likes()
        context["total_likes"]=total_likes
        return context
    
class AddPost(CreateView):
    model=Post
    form_class=PostForm
    template_name='addpost.html'
    success_url= reverse_lazy('home')
    #fields= '__all__'
class EditPost(UpdateView):
    model=Post
    form_class=EditForm
    template_name='edit_post.html'
    success_url= reverse_lazy('home')
    #fields=['title','body']
class DeletePost(DeleteView):
     model=Post
     template_name='delete_post.html'
     success_url= reverse_lazy('home')
     
def LikeView(request, pk):
   post=get_object_or_404(Post, id=pk)
   post.likes.add(request.user)
   return HttpResponseRedirect(reverse('post detail', args=[str(pk)])) 
   #success_url= reverse_lazy('home')
 

        
def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': form})