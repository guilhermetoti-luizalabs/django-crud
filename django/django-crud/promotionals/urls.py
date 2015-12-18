from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^$', views.PromotionalList.as_view(), name='promotional_list'),
    url(r'^new$', views.PromotionalCreate.as_view(), name='promotional_new'),
    url(
        r'^edit/(?P<pk>\d+)$',
        views.PromotionalUpdate.as_view(),
        name='promotional_edit'
    ),
    url(
        r'^delete/(?P<pk>\d+)$',
        views.PromotionalDelete.as_view(),
        name='promotional_delete'
    ),
)
