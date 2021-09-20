from django.db import models


def product_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/product_<id>/<filename>
    return 'store/media/product_{0}_{1}'.format(instance.id, filename)


class TimeStampMixin(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True