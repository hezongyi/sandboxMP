from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class Menu(models.Model):

    name = models.CharField(max_length=30, unique=True, verbose_name="菜单名")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父菜单")
    icon = models.CharField(max_length=50, null=True, blank=True,verbose_name="图标")
    code = models.CharField(max_length=50, null=True, blank=True, verbose_name="编码")
    url = models.CharField(max_length=128, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '菜单'
        verbose_name_plural = verbose_name

    @classmethod
    def get_menu_by_request_url(clscls, url):
        return dict(menu=Menu.objects.get(url=url))


class Role(models.Model):

    name = models.CharField(max_length=32, unique=True, verbose_name="角色")
    permissions = models.ManyToManyField("Menu", blank=True, verbose_name="URL授权")
    desc = models.CharField(max_length=50, blank=True, null=True, verbose_name="描述")


class Structure(models.Model):

    type_choice = (("unit", "单位"), ("department", "部门"))
    name = models.CharField(max_length=60, verbose_name="名称")
    type = models.CharField(max_length=20, choices=type_choice, default="department")
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="父类架构")


    class Meta:
        verbose_name = "组织架构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):

    name = models.CharField(max_length=20, default="", verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    gender = models.CharField(max_length=10, choices=(("male", "男"), ("female", "女")), default="male", verbose_name="性别")
    mobile = models.CharField(max_length=11, default="", verbose_name="手机号码")
    email = models.EmailField(max_length=50, verbose_name="邮箱")
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.jpg", max_length=100, null=True, blank=True)
    department = models.ForeignKey("Structure", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="部门")
    post = models.CharField(max_length=50, null=True, blank=True, verbose_name="职位")
    superior = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="上级主管")
    roles = models.ManyToManyField("Role", verbose_name="角色", blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.name
