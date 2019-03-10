from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password,  **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        # if extra_fields.get('is_superuser', True):
        #     raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)
    

class CustomUser(AbstractUser):
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'
    
    email = models.EmailField('メールアドレス', unique=True)
    username = models.CharField('ユーザー名',
                                max_length=150,
                                blank=True,
                                null=True,
                                help_text="半角アルファベット、半角数字、@/./+/-/_で150文字以下にしてください",
                                validators=[AbstractUser.username_validator]
                                )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()