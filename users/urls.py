from django.urls import path
from .views import register_candidate, login_view, candidate_list, logout_view

urlpatterns = [
    path("register/", register_candidate, name="register"),
    path("login/", login_view, name="login"),
    path("candidates/", candidate_list, name="candidate_list"),
    path('logout/', logout_view, name='logout'),

]
