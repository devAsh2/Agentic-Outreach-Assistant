from django.urls import path
from .views import GenerateOutreachView


urlpatterns = [
    # this is mapping the url api/generate/ to our view
    path('generate/',GenerateOutreachView.as_view(), name='generate-outreach'),
]