from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #-------------------------------Function-Based Views------------------------------------------
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.bug_detail, name='bug_id'),
    path('features/<int:feature_id>/', views.feature_detail, name='feature_id'),

    #---------------------------------Class-Based Views-------------------------------------------
    # path('', views.IndexView.as_view(), name='index'),
    # path('bugs/', views.BugsListView.as_view(), name='bug_list'),
    # path('features/', views.FeaturesListView.as_view(), name='feature_list'),
    # path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_id'),
    # path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_id'),
]
