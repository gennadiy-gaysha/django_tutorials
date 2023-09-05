from django.urls import path
from . import views
# namespaced - пространство имен
app_name='articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    # named capturing group <slug:abc> - is a way to capture a specific part of a URL pattern
    # and give it a name. This is typically used in URL patterns defined for Django
    # views and allows you to extract data from the URL and pass it as a named argument
    # to your view function.
    # <abc> - is the name, what we want to call this group and we convey (capture) this
    # parameter as an argument to article_detail function
    # The "slug" part specifies that this named capturing group is intended to match a
    # slug-like string, which typically includes lowercase letters, numbers, hyphens, and
    # underscores.
    path('<slug:abc>', views.article_detail, name='detail')
]
