import os
from django.conf import settings

emailTemplateConfigs = {
    "PASSWORD_RESET_TEMPLATE": os.path.join(settings.BASE_DIR, "emailService", "templates","password-reset.html")
}