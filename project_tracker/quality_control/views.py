from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bug_report_url = reverse('quality_control:bug_list')
    feature_request_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_report_url}'>Список всех багов</a><br /><a href='{feature_request_url}'>Запросы на улучшения</a>"
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse('Список отчетов об ошибках')

def feature_list(request):
    return HttpResponse('Список запросов на улучшение')

def bug_detail(request, bug_id):
    return HttpResponse(f'Детали бага {bug_id}')

def feature_id_detail(request, feature_id):
    return HttpResponse(f'Детали бага {feature_id}')