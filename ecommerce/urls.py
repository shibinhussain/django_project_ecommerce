from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    
    path('login/', views.login),
    path('login1/', views.go),
    path('admin1/', views.admin),
    path('signup/', views.signup),
    path('custcreate/', views.custCreate),
    path('custhome/', views.custhome),

    path('pdt-detail/', views.pdt_detail),
    path('pdt-insert/', views.pdt_insert),

    path('pdt-view/', views.pdt_view),
    path('edit/<int:id>', views.pdt_edit),
    path('pdt-update/<int:id>', views.pdt_update),
    path('delete/<int:id>', views.delete),

    path('complaints/', views.complaint),
    path('seller_details/', views.seller),
    path('sel_insert/', views.sel_insert),

    path('view-seller/', views.view_sel),
    path('edit1/<int:id>', views.sel_edit),
    path('sell-update/<int:id>', views.sell_update),
    path('sel_delete/<int:id>', views.sel_delete),

    #customerpage
    path('cusproduct/', views.cusProduct),
    path('orders_pdts/<int:id>', views.cusOrderPdts),
    path('orderpdtsub/', views.orderPdtSub),

    #review section

    path('review/', views.review),
    path('add-review/', views.add_review),

]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
