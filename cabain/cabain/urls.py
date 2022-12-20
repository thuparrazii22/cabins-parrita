"""cabain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from cabin_APP import views

urlpatterns = [
    path('registro/', views.registrarse, name='registro'),
    path('nuevo_cliente', views.crear_cliente, name='crear_cliente'),
    path('nuevo_detalle_factura', views.crear_deatalle_factura, name='nuevo_detalle_factura'),
    path('producto/', views.producto, name='producto'),
    path('eliminar_producto/<int:id>', views.eliminar_producto, name='eliminar_producto'),

    path('cuenta/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('proyecto_nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('listado_proyecto/', views.listado_proyectos, name='listado_proyectos'),
    path('proyecto/<int:id>', views.proyecto, name='proyecto'),
    path('menu/', views.main_menu, name='menu_principal'),
    
    path('payment_method/', views.payment_method , name='payment_method'),
    path('eliminar_metodo_pago/<int:id>', views.eliminar_metodo_pago, name='eliminar_metodo_pago'),
    path('actualizar_metodo_pago/<int:id>', views.actualizar_metodo_pago, name='actualizar_metodo_pago'),
    
    path('unidad_medida/', views.unidad_medida, name='unidad_medida'),
    path('unidad_medida/<int:id>', views.actualizar_unidad_medida, name='actualizar_unidad_medida'),
    path('unidad_medida_delete/<int:id>', views.eliminar_unidad_medida, name='eliminar_unidad_medida'),
    
    path('maestro/', views.maestro, name='maestro'),
    path('actualizar_maestro/<int:id>', views.actualizar_maestro, name='actualizar_maestro'),
    path('eliminar_maestro/<int:id>', views.eliminar_maestro, name='eliminar_maestro'),
    
    path('nueva_factura/', views.crear_factura, name='crear_factura'), 
    path('listado_factura/', views.listado_factura, name='listado_factura'),
]
