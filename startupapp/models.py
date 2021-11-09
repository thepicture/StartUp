from django.db import models


class TypeOfUser:
    name = models.CharField(max_length=64)


class Region:
    name = models.CharField(max_length=512)


class User:
    login = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    middle_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64)
    type = models.ForeignKey(TypeOfUser, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    user_image = models.ImageField()


class UserEmail:
    email_address = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserPhoneNumber:
    number = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class UserLoginHistory:
    is_success = models.BooleanField()
    ip_address = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class TypeOfInvestment:
    name = models.CharField(max_length=128)


class Category:
    name = models.CharField(max_length=128)


class StartUp:
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    is_actual = models.BooleanField()
    creation_datetime = models.DateTimeField()
    description = models.CharField(max_length=2048)
    max_members_count = models.SmallIntegerField()


class UserStartupInvestHistory:
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    startup = models.ForeignKey(StartUp, on_delete=models.PROTECT)
    invest_type = models.ForeignKey(TypeOfInvestment, on_delete=models.PROTECT)
    invest_datetime = models.DateTimeField()
    invested_money = models.DecimalField()


class StartUpComment:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=2048)
    post_datetime = models.DateTimeField()
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)


class StartUpImage:
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=64)
    image_description = models.CharField(2048)
    upload_datetime = models.DateTimeField()
    image_blob = models.ImageField()


class RoleOfStartUp:
    name = models.CharField(max_length=128)


class StartUpOfUser:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleOfStartUp, on_delete=models.CASCADE)


class HashTag:
    text = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class HashTagOfStartUp:
    startup = models.ForeignKey(StartUp, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(HashTag, on_delete=models.CASCADE)
