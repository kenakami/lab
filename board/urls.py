from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feed', views.FeedView.as_view(), name='feed'),
    path('catalog', views.CatalogListView.as_view(), name='catalog'),
    path('thread/<int:pk>', views.ThreadDetailView.as_view(), name='thread-detail'),

    path('create-thread', views.create_thread, name='create-thread'),
    path('thread/<int:pk>/reply', views.reply, name='reply'),
]

