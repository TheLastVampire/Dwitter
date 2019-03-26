from django.db import models

# Create your models here.


class Dweet(models.Model):
    """This class represents the model."""
    dweeterId = models.IntegerField(null=False, default=0)
    text = models.CharField(max_length=256, blank=False)
    likeCount = models.IntegerField(null=False, default=0)

    crDate = models.DateTimeField(auto_now_add=True)
    crBy = models.IntegerField(null=False, default=0)
    lmodDate = models.DateTimeField(auto_now=True)
    lmodBy = models.IntegerField(default=0)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.text)


class Dweeter(models.Model):
    """This class represents the model."""
    username = models.CharField(max_length=16, blank=False)
    pswd = models.CharField(max_length=16, blank=False)
    fullname = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=32, blank=True)

    crDate = models.DateTimeField(auto_now_add=True)
    crBy = models.IntegerField(null=False, default=0)
    lmodDate = models.DateTimeField(auto_now=True)
    lmodBy = models.IntegerField(default=0)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.username)


class Comment(models.Model):
    """This class represents the model."""
    dweetId = models.IntegerField(null=False, default=0)
    commenterId = models.IntegerField(null=False, default=0)
    text = models.CharField(max_length=256, blank=False)

    crDate = models.DateTimeField(auto_now_add=True)
    crBy = models.IntegerField(null=False, default=0)
    lmodDate = models.DateTimeField(auto_now=True)
    lmodBy = models.IntegerField(default=0)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.text)


class Liked(models.Model):
    """This class represents the model."""
    dweetId = models.IntegerField(null=False, default=0)
    dweeterId = models.IntegerField(null=False, default=0)
    likedBy = models.IntegerField(null=False, default=0)

    crDate = models.DateTimeField(auto_now_add=True)
    crBy = models.IntegerField(null=False, default=0)
    lmodDate = models.DateTimeField(auto_now=True)
    lmodBy = models.IntegerField(default=0)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.likedBy)


class FollowedDweeter(models.Model):
    """This class represents the model."""
    dweeterId = models.IntegerField(null=False, default=0)
    followerDweeterId = models.IntegerField(null=False, default=0)

    crDate = models.DateTimeField(auto_now_add=True)
    crBy = models.IntegerField(null=False, default=0)
    lmodDate = models.DateTimeField(auto_now=True)
    lmodBy = models.IntegerField(default=0)
    isActive = models.IntegerField(default=1)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.dweeterId)
