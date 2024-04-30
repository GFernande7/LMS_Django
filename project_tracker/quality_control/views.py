from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

def index(request):
    bug_report_url = reverse('quality_control:bug_list')
    feature_request_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_report_url}'>Список всех багов</a><br /><a href='{feature_request_url}'>Запросы на улучшения</a>"
    return HttpResponse(html)

#-------------------------------Function-Based Views------------------------------------------

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a>-{bug.status}</li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список улучшений</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a>-{feature.status}</li>'
    features_html += '</ul>'
    return HttpResponse(features_html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
    response_html += f'<p>status: {bug.status}<br />priority: {bug.priority}<br />project: {bug.project}<br />task: {bug.task}</p>'
    return HttpResponse(response_html)

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>'
    response_html += f'<p>status: {feature.status}<br />priority: {feature.priority}<br />project: {feature.project}<br />task: {feature.task}</p>'
    return HttpResponse(response_html)

#---------------------------------Class-Based Views-----------------------------------------------------

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_report_url = reverse('quality_control:bug_list')
        feature_request_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bug_report_url}'>Список всех багов</a><br /><a href='{feature_request_url}'>Запросы на улучшения</a>"
        return HttpResponse(html)
    
class BugsListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = '<h1>Список багов</h1><ul>'
        for bug in bugs:
            bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
        bugs_html += '</ul>'
        return HttpResponse(bugs_html)
    
class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
        response_html += f'<p>status: {bug.status}<br />priority: {bug.priority}<br />project: {bug.project}<br />task: {bug.task}</p>'
        return HttpResponse(response_html)
    
class FeaturesListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        features_html = '<h1>Список улучшений</h1><ul>'
        for feature in features:
            features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
        features_html += '</ul>'
        return HttpResponse(features_html)
    
class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>'
        response_html += f'<p>status: {feature.status}<br />priority: {feature.priority}<br />project: {feature.project}<br />task: {feature.task}</p>'
        return HttpResponse(response_html)    