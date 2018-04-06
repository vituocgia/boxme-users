from boxme_user.apps import CustomUserConfig


class CustomUserSubclassConfig(CustomUserConfig):
    name = 'test_boxme_user_subclass'
    verbose_name = "Test Custom User Subclass"
