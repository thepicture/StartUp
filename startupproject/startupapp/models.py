import django.contrib.auth.models
from django.db import models
from django.contrib.postgres.fields import ArrayField


class TypeOfUser(models.Model):
    """Defines the type of an user."""
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Region(models.Model):
    """Defines the region of the startup or an user."""
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class User(models.Model):
    """Defines the user.

    User's image can be null.

    An user can have one or more emails and phones.
    Usually, it is not necessary to have multiple emails,
    so the system can check multiplicity.
    Leave it for the scalability in the future.

    """

    login = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64)
    type = models.ForeignKey(TypeOfUser, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    user_image = models.ImageField(null=True)
    register_date = models.DateTimeField()
    emails = ArrayField(models.CharField(max_length=128))
    phones = ArrayField(models.CharField(max_length=64))
    money_in_rubles = models.DecimalField(decimal_places=2,
                                          default=0,
                                          max_digits=9)

    def __str__(self):
        return self.login


class UserLoginHistory(models.Model):
    """Defines the user login history.

    Must have IPv4 or IPv6 ip address,
    and must say if the login was successful
    at the given datetime.

    """
    is_success = models.BooleanField()
    ip_address = models.GenericIPAddressField()
    login_datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.login_datetime


class Category(models.Model):
    """Defines the category of a startup."""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class StartUp(models.Model):
    """Defines the startup.

    StartUp must have at least one creator.

    If the first creator assigns the rights
    to the another creator,
    another creator yields ability to delete
    the current startup, so we need password
    checking of the original creator.

    Must have description, otherwise it is impossible
    to identify what is the purpose of the startup.

    Can have zero or one hashtags. They act like categories,
    but more precise.

    """
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_actual = models.BooleanField()
    creation_datetime = models.DateTimeField()
    description = models.CharField(max_length=2048)
    max_members_count = models.SmallIntegerField()

    def __str__(self):
        return f'{self.name}.{self.creation_datetime}'


class TypeOfTransaction(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class UserStartupInvestHistory(models.Model):
    """Defines the startups investment history of the user."""

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    startup = models.ForeignKey(StartUp, on_delete=models.PROTECT)
    invest_type = models.ForeignKey(TypeOfTransaction,
                                    on_delete=models.PROTECT)
    invest_datetime = models.DateTimeField()
    invested_money = models.DecimalField(max_digits=9,
                                         decimal_places=2)

    def __str__(self):
        return f'{self.user.login}.' \
               f'{self.invest_type.name}.' \
               f'{self.invest_datetime}'


class StartUpComment(models.Model):
    """Defines the comment of the startup."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
    post_datetime = models.DateTimeField()
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.login} ({self.post_datetime}):{self.text}'


class StartUpImage(models.Model):
    """Defines the image set of the startup."""
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=64)
    image_description = models.CharField(max_length=2048)
    upload_datetime = models.DateTimeField()
    image_blob = models.ImageField()
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL,
                             null=True)

    def __str__(self):
        return f'{self.user}:{self.image_title}'


class RoleOfStartUp(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class StartUpOfUser(models.Model):
    """Defines the user's role in the startup."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleOfStartUp, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.login}, {self.startup.name}, {self.role.name}'


class HashTag(models.Model):
    """Defines the set of hashtags for startups."""
    text = models.CharField(max_length=32)
    startups = models.ManyToManyField(StartUp)

    def __str__(self):
        return self.text
