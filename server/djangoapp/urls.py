from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # then name the URL

    # path for about view
    path(route='about-us/', view=views.aboutUs, name='about_us'),
    # path for contact us view
    path(route='contact-us/', view=views.contactUs, name='contact_us'),
    # path for registration

    # path for login
    path(route='login/', view=views.login_request, name='login'),
    # path for logout
    path(route='logout/', view=views.logout_request, name='logout'),

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)