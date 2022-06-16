from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# Login decorathor
from django.contrib.auth.decorators import login_required
# Staff decorathor
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('django/', admin.site.urls),
    path('', core_views.LandingView.as_view(), name='landing'),
    path('ley/', core_views.ley, name='ley'),
    path('asambleas/', core_views.asambleas, name='asambleas'),
    path('proceso/', core_views.ProcesoListView.as_view(), name='procesos'),
    path('proceso/<pk>/', core_views.ProcesoDetailView.as_view(), name='proceso'),

    path('admin/proceso/', staff_member_required(core_views.ProcesoListView.as_view(template_name="core/admin_proceso.html")), name='admin_procesos'),
    path('admin/proceso/crear/', staff_member_required(core_views.ProcesoCreate.as_view()), name='admin_proceso_crear'),
    path('admin/proceso/<pk>', staff_member_required(core_views.ProcesoUpdateView.as_view())),
    path('admin/proceso/<pk>/eliminar/', staff_member_required(core_views.ProcesoDeleteView.as_view())),   

    path('perfil/', login_required(core_views.perfil), name='perfil'),

    path('cuenta/', include('django.contrib.auth.urls')),
    path('salir/', auth_views.LogoutView.as_view(), name='salir'),
    path('ingreso/', auth_views.LoginView.as_view(), name='ingreso'),
    path('password/', auth_views.PasswordChangeView.as_view()),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)