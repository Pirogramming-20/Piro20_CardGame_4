from django.urls import path, include

app_name = 'game'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),
    path('game/', include('game.urls'))
]