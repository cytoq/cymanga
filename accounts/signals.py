from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User, Group, Permission
from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_migrate)
def create_moderator_group(sender, **kwargs):
    # Create the moderator group if it doesn't exist
    Group.objects.get_or_create(name='moderator')

@receiver(post_migrate)
def assign_permissions_to_moderators(sender, **kwargs):
    moderator_group, created = Group.objects.get_or_create(name='moderator')

    if created:
        # Here you can add specific permissions for the moderator group
        permissions = Permission.objects.filter(codename__in=['edit_comment', 'delete_comment'])
        moderator_group.permissions.set(permissions)
