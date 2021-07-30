from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path(
        "thanks/", TemplateView.as_view(template_name="pages/thanks.html"), name="thanks"
    ),
    path(
        "reportcreatedsucessfully/", TemplateView.as_view(template_name="reports/reportcreatedsucessfully.html"), name="reportcreatedsucessfully"
    ),
    path (
        "reportslist/", TemplateView.as_view(template_name="reports/reportslist.html"), name="reportslist"
    ),
    path (
        "faqslist/", TemplateView.as_view(template_name="faqs/faqslist.html"), name="faqslist"
    ),
    path(
        "reportscreate/", TemplateView.as_view(template_name="reports/reportscreate.html"), name="reportscreate"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("reports/", include("sodp.reports.urls", namespace = "reports")),
    path("requestdemo/", include("sodp.requestdemo.urls", namespace = "requestdemo")),
    path("faqs/", include("sodp.faqs.urls", namespace = "faqs")),
    path("users/", include("sodp.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path("views/", include("sodp.views.urls", namespace = "views")),
    # Your stuff: custom urls includes go here

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
