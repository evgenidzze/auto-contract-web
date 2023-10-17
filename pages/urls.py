from django.urls import path
from django.views.generic import RedirectView

from pages.views import Page1Create, Page2, Page3, Page4, get_departments, Page1Update

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=True)),
    path('page1/', Page1Create.as_view(), name='page_1'),
    path('page1/<int:pk>', Page1Update.as_view(), name='page_1_update'),
    path('page2/<int:pk>', Page2.as_view(), name='page2'),
    path('page3/<int:pk>', Page3.as_view(), name='page3'),
    path('page4/<int:pk>', Page4.as_view(), name='page4'),
    path('get_departments/', get_departments, name='ajax_load_cities'),
]
