from django.db import models
from django.conf import settings

# Benutzerprofil
# Vermieter & Mieter wie bei Airbnb

class Profile(models.Model):

    """User-Profil mit Rolle (tenant/landlord), Telefonnummer und Bio."""

    ROLE_CHOISES = (
        ("tenant", "Mieter"),
        ("landlord", "Vermieter"),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOISES, default="tenant")

    def __str__(self):
        return f"{self.user.username} ({self.role})"
