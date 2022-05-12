from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),

    # path('search', views.search, name="search"),

    path('profile/', views.profile, name="profile"),
    path("reset-password", views.reset_password, name="reset-password"),

    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('logout/', views.signout, name="logout"),

    # Test path for checking the browser, IP-address, and device info of the user
    path('browser/', views.get_browser_info, name='browser'),

    path('media/<media_id>/done', views.mark_as_done, name='mark-as-done'),

    path('device/<int:device_id>/delete',
         views.delete_user_device, name='delete_device'),

    # Path to All trainings Page
    path('trainings/', views.all_trainings, name='trainings'),

    # Path to (Single training - with all modules) Page
    path('trainings/<int:training_id>/modules/',
         views.all_modules, name='all_modules'),

    # Path to (Single training - with all modules) Page
    path('trainings/<int:training_id>/',
         views.resume_all_modules, name='resume_all_modules'),

    # Path to (Single training - with single module - with all videos) Page
    path('trainings/<int:training_id>/modules/<int:module_id>/medias/',
         views.media, name='media'),

    # Path to (Single training - with single module - with single media) Page
    path('trainings/<int:training_id>/modules/<int:module_id>/medias/<int:media_id>/',
         views.media, name='single_media'),

]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
