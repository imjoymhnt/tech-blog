from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('<int:pk>/details/',views.DetailPageView.as_view(), name='detail')

]

