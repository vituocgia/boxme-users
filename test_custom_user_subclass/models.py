from boxme_user.models import AbstractBoxmeUser


class MyCustomBoxmeUser(AbstractBoxmeUser):

    class Meta(AbstractBoxmeUser.Meta):
        verbose_name = "MyCustomBoxmeUserVerboseName"
        verbose_name_plural = "MyCustomBoxmeUserVerboseNamePlural"
