from django.urls import path

from . import views

app_name = 'frame'
urlpatterns =[
    # 汎用ビューの使用に合ったって、urls.pyでは、特別なimportを行わない
    path('', views.IndexPageView.as_view(), name='index'),
    path('portfolio/', views.PortfolioPageView.as_view(), name='portfolio'),

]
