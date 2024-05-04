from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #-------------------------------Function-Based Views------------------------------------------
    # path('', views.index, name='index'),
    # path('bugs/', views.bug_list, name='bug_list'),
    # path('features/', views.feature_list, name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_id'),
    # path('features/<int:feature_id>/', views.feature_detail, name='feature_id'),
    # path('bugs/new/', views.create_bug, name='create_bug'),
    # path('feature/new/', views.create_feature, name='create_feature'),
    # path('bugs/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    # path('features/<int:feature_id>/update/', views.update_feature, name='update_feature'),
    # path('bugs/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    # path('features/<int:feature_id>/delete/', views.delete_bug, name='delete_feature'),

    #---------------------------------Class-Based Views-------------------------------------------
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugsListView.as_view(), name='bug_list'),
    path('features/', views.FeaturesListView.as_view(), name='feature_list'),
    path('bugs/new/', views.BugCreateView.as_view(), name='create_bug'),
    path('feature/new/', views.FeatureCreateView.as_view(), name='create_feature'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('bugs/<int:bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug'),
    path('features/<int:feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_feature'),
    path('bugs/<int:bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('features/<int:feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]
