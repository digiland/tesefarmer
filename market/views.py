from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views import generic
from .forms import CustomUserCreationForm, ImageForm, PostForm
from .models import Post, Image
from django.forms import modelformset_factory

# Create your views here.


class LandingPageView(generic.TemplateView):
    template_name = 'market/landing_page.html'


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class MarketView(generic.ListView):
    template_name = 'market/market.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Post.objects.all()


def add_post_view(request):

    ImageFormSet = modelformset_factory(Image, form=ImageForm, extra=3)
    if request.method == 'GET':
        post_form = PostForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        return render(request, 'market/add_post.html', {'post_form': post_form, 'formset': formset})
    elif request.method == 'POST':
        post_form = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES)

        if post_form.is_valid() and formset.is_valid():
            post_obj = post_form.save()

            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    Image.objects.create(image=image, post=post_obj)
                print("image added")
            return render(request, 'market/landing_page.html')
        else:
            print(post_form.errors, formset.errors)


def gallery_view(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'market/gallery.html', {'post': post})
