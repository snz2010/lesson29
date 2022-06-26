from django.urls import path
#from rest_framework import routers

from .views import LocView, LocDetailView, LocDeleteView, LocUpdateView, LocationViewSet#LocCreateView,

#router = routers.SimpleRouter()
#router.register(r'location', LocationViewSet) # регистрируем вьюсет
#urlpatterns = [
    #path('', LocView.as_view(),name='loc_index_url'),
    #path('<int:pk>/', LocDetailView.as_view(),name='loc_detail_url'),
    #path('create/', LocCreateView.as_view(),name='loc_create_url'),
    ###path('create/', LocationViewSet.as_view({'post': 'list'}),name='loc_create_url'),
    #path('<int:pk>/update/', LocUpdateView.as_view(),name='loc_update_url'),
    #path('<int:pk>/delete/', LocDeleteView.as_view(),name='loc_delete_url'),
#]
#urlpatterns += router.urls # добавляем роутер к остальным маршрутам