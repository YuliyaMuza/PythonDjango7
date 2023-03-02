from django.urls import path, include

from .views import PostsList, PostDetail, PostSearchList, PostSearchDetail, PostCreate, PostEdit, PostDelete, \
   CategoryListView, subscribe, IndexView

urlpatterns = [

   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearchList.as_view()),
   path('<int:pk>', PostSearchDetail.as_view()),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('accounts/', include('django.contrib.auth.urls')),
   path('', IndexView.as_view())

]
