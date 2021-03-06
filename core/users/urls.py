from django.urls import path

from core.users.views import (login_page,
                              home,
                              logout_view,
                              )

app_name = 'users'
urlpatterns = [
    path('login/', login_page, name='login'),
    path('home/', home, name='home'),
    path('logut/', logout_view, name='logout'),

]
