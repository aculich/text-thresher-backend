from django.conf.urls import include, url
from rest_framework import routers
from views import ROUTER
from . import views

urlpatterns = [
    # Add the views we've registered with the default router
    url(r'^', include(ROUTER.urls)),
    url(r'^question/$', views.questions),
    url(r'^question/(?P<id>[0-9]+)$', views.question),
    url(r'^question/(?P<id>[0-9]+)/(?P<ans_id>[0-9]+)$', views.next_question),
    url(r'^post_question/', views.post_question),
    url(r'^submit_answer/', views.submit_answer),
]
