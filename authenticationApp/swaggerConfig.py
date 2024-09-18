from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Authentication App API",
        default_version='v1',
        description="API documentation for Authentication  project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@authenticationApp.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
