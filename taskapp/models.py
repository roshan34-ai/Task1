from pyexpat import model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    TEAMLEADER = 1
    TEAMMEMBER = 2
    USER = 3

    ROLE_CHOICES = (
        (TEAMLEADER, 'team_leader'),
        (TEAMMEMBER, 'team_member'),
        (USER, 'user')
    )

    
    name = models.CharField(max_length=100, default=False)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=13, default=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



class Team(models.Model):
    name = models.CharField(max_length=100)
    team_leader = models.ForeignKey(CustomUser, related_name="Team", on_delete=models.CASCADE)
    team_membars = models.ManyToManyField(CustomUser)
    
    def get_team_membars(self):
        return "\n".join([p.name for p in self.team_membars.all()])

    def __str__(self) -> str:
        return self.name



class Task(models.Model):
    ASSIGNED = 1
    PROGRESS = 2
    UNDER_REVIEW = 3
    DONE = 4

    STATUS_CHOICES = (
        (ASSIGNED, 'assigned'),
        (PROGRESS, 'progress'),
        (UNDER_REVIEW, 'under_review'),
        (DONE, 'done')
    )

    name = models.CharField(max_length=50)
    team = models.ManyToManyField(Team, related_name="Team")
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, blank=True,)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now_add=True)
    

    def get_team(self):
        return "\n".join([p.name for p in self.team.all()])
    
    def __str__(self) -> str:
        return self.name