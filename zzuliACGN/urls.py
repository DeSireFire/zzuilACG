"""zzuliACGN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
# from django.views import static
# from django.conf.urls.static import static
from . import view
handler404 = view.page_not_found
urlpatterns = [
    path('NTadmin/', admin.site.urls),
    path('', include('ZA_Show.urls')),
    path('user/', include('ZA_User.urls')),
    path('bulding/', handler404),
    # path('', include('ZA_Index.urls')),

    # 增加以下一行，以识别静态资源
    # path(r'^static/(?P<path>.*)$', settings.static.serve, {'document_root':settings.STATIC_ROOT}),

]
# 配置异常页面
# handler403 = view.page_permission_denied
# handler404 = view.page_not_found
# handler500 = view.page_inter_error