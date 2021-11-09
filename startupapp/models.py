from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class TypeOfUser:
    """Defines the type of an user."""
    name = models.CharField(max_length=64)


class Region:
    """Defines the region of the startup or an user."""
    name = models.CharField(max_length=512)


class User:
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


class UserLoginHistory:
    """Defines the user login history.

    Must have IPv4 or IPv6 ip address,
    and must say if the login was successful
    at the given datetime.

    """
    is_success = models.BooleanField()
    ip_address = models.GenericIPAddressField()
    login_datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category:
    """Defines the category of a startup."""
    name = models.CharField(max_length=128)


class StartUp:
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


class UserStartupInvestHistory:
    """Defines the startups investment history of the user."""
    class TypeOfInvestment(models.TextChoices):
        """Defines the type of investment."""
        WITHDRAW = 'WI', _('Withdraw')
        INVEST = 'IN', _('Invest')

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    startup = models.ForeignKey(StartUp, on_delete=models.PROTECT)
    invest_type = models.CharField(TypeOfInvestment,
                                   on_delete=models.PROTECT,
                                   choices=TypeOfInvestment.choices)
    invest_datetime = models.DateTimeField()
    invested_money = models.DecimalField()


class StartUpComment:
    """Defines the comment of the startup."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
    post_datetime = models.DateTimeField()
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)


class StartUpImage:
    """Defines the image set of the startup."""
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=64)
    image_description = models.CharField(2048)
    upload_datetime = models.DateTimeField()
    image_blob = models.ImageField()


class StartUpOfUser:
    """Defines the user's role in the startup."""
    class RoleOfStartUp(models.TextChoices):
        """Defines an user's role in the startup."""
        MEMBER = 'ME', _('Withdraw')
        MODERATOR = 'MO', _('Moderator')
        CREATOR = 'CR', _('Creator')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)
    role = models.CharField(max_length=128,
                            choices=RoleOfStartUp.choices)


class HashTag:
    """Defines the set of hashtags for startups."""
    text = models.CharField(max_length=32)
    startups = models.ManyToManyField(StartUp)
