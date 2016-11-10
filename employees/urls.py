from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from .employeesapp import views


urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^employees/', views.EmployeesList.as_view()),
    url(r'^employees/details/(?P<pk>[0-9]+)/$/', views.EmployeesDetails.as_view()),
    url(r'^$', RedirectView.as_view(url='/employees/'), name='redirect_to_employees'),
)

urlpatterns = format_suffix_patterns(urlpatterns)