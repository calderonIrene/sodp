from django.urls import path
from sodp.requestdemo.views import DemoFormView

app_name = "requestdemo"

urlpatterns = [
     path( "newrequestdemo/", DemoFormView.as_view(), name = 'demo') 
]
