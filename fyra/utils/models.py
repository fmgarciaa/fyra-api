"""Django models utilities."""

# Django
from django.db import models

# Django-Extensions
from django_extensions.db.fields import ShortUUIDField
import shortuuid


class FyraAbstractModels(models.Model):
    """Fyra Abstract base model.

    CRideModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
      + created (DateTime): Store the datetime the objects was created.
      + modified (DateTime): Store the datetime the objects was modified
      + uuid (Slug): Store unique uuid field to querysets
      + is_remover(Boolean): Indicates if the item has been deleted
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the object was last modified'
    )

    uuid = ShortUUIDField(unique=True, editable=False, default=shortuuid.uuid)

    is_removed = models.BooleanField(
        'remove status',
        default=False,
        help_text='used to signal that it is removed'
    )

    class Meta:
        """Meta options."""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
