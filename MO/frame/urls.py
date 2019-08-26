from django.urls import path

from . import views

app_name = 'frame'
urlpatterns =[
    # 汎用ビューの使用に合ったって、urls.pyでは、特別なimportを行わない
    path('', views.IndexPageView.as_view(), name='index'),
    path('portfolio/', views.PortfolioPageView.as_view(), name='portfolio'),
    path('portfolio/photograph/', views.PhotographPageView.as_view(), name='photograph'),
    path('portfolio/video/', views.VideoPageView.as_view(), name='video'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
]
