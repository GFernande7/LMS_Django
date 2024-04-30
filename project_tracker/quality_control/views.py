from django.shortcuts import get_object_or_404, redirect, render
from .forms import BugReportForm
from .models import BugReport, FeatureRequest
from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView

def index(request):
    return render(request, 'quality_control/index.html')

#-------------------------------Function-Based Views------------------------------------------

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bug_list': bugs})

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'feature_list': features})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def feature_detail(request, feature_id):
    feature = get_object_or_404(BugReport, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

#---------------------------------Class-Based Views-----------------------------------------------------

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')
    
class BugsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugs_list.html'
    
class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    
class FeaturesListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/features_list.html'
    
class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'

def create_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def create_feature(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})
