from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .models import Film, Genre
from .forms import FilmForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def toggle_like(request, pk):
    film = Film.objects.get(pk=pk)
    if request.user in film.likes.all():
        film.likes.remove(request.user)
    else:
        film.likes.add(request.user)
    return HttpResponseRedirect(reverse('film_detail', args=[pk]))


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class FilmListView(ListView):
    model = Film
    template_name = 'cineboard/film_list.html'
    context_object_name = 'films'

    def get_queryset(self):
        queryset = Film.objects.all()

        search = self.request.GET.get('q')
        genre = self.request.GET.get('genre')
        sort = self.request.GET.get('sort')

        if search:
            queryset = queryset.filter(title__icontains=search)

        if genre:
            queryset = queryset.filter(genre__slug=genre)

        if sort == 'rating':
            queryset = queryset.order_by('-rating')
        else:
            queryset = queryset.order_by('-created_at')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context

  



class FilmDetailView(DetailView):
    model = Film
    template_name = 'cineboard/film_detail.html'
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.film = self.object
                comment.user = request.user
                comment.save()
        return redirect('film_detail', pk=self.object.pk)
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj



class FilmCreateView(LoginRequiredMixin, CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'cineboard/film_form.html'
    success_url = reverse_lazy('film_list')


class FilmUpdateView(LoginRequiredMixin, UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'cineboard/film_form.html'
    success_url = reverse_lazy('film_list')


class FilmDeleteView(LoginRequiredMixin, DeleteView):
    model = Film
    template_name = 'cineboard/film_confirm_delete.html'
    success_url = reverse_lazy('film_list')




    
  


