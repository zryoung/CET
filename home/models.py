from django.db import models


# Create your models here.
from login.models import User
from .fields import RestrictedFileField


class exam_entry_table(models.Model):
    # 考点信息表
    exam_id = models.CharField(verbose_name="考试编号", max_length=10)
    exam_type = models.CharField(verbose_name="考试类别", max_length=128)
    exam_point = models.CharField(verbose_name="考点", max_length=128)
    exam_time = models.CharField(verbose_name="考试时间", max_length=128)
    number = models.IntegerField(verbose_name="容量")
    entry_number = models.IntegerField(verbose_name="已报名数量", default=0)

    def __str__(self):
        return self.exam_point

    class Meta:
        # ordering = ['c_time']
        verbose_name = '考点'
        verbose_name_plural = '考点信息表'


class user_entry_table(models.Model):
    # 用户考试信息表
    email = models.EmailField(verbose_name="邮箱")
    exam_id = models.CharField(verbose_name="考试编号", max_length=10)
    exam_point = models.CharField(verbose_name="考点", max_length=128)

    def __str__(self):
        return self.email

    class Meta:
        # ordering = ['c_time']
        verbose_name = '用户考试信息'
        verbose_name_plural = '用户考试信息表'


class user_data(models.Model):
    # 用户信息表
    user_name = models.CharField(verbose_name="用户名", max_length=128, unique=True)
    user_true_name = models.CharField(verbose_name="真实姓名", max_length=128, null=True)
    user_id = models.CharField(verbose_name="身份证号", max_length=18, null=True)
    # user_img =
    user_school = models.CharField(verbose_name="在读学校", max_length=128)
    user_f_score = models.IntegerField(verbose_name="四级成绩", default=0)
    user_s_score = models.IntegerField(verbose_name="六级成绩", default=0)

    def __str__(self):
        return self.user_name

    class Meta:
        # ordering = ['c_time']
        verbose_name = '用户名'
        verbose_name_plural = '用户信息表'


def upload_file(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.name.id, ext)
    return '{}'.format(filename)


class Student(models.Model):
    '''用户表'''

    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.CharField('姓名', max_length=20)
    idCard = models.CharField('身份证号', max_length=18, unique=True)
    # password = models.CharField(verbose_name="密码", max_length=256)
    # sex = models.CharField(verbose_name="性别", max_length=32, choices=gender, default='男')
    phone1 = models.CharField('联系电话1', max_length=20)
    phone2 = models.CharField('联系电话2', max_length=20, null=True, blank=True)
    primarySchool = models.CharField('毕业小学', max_length=50, null=True, blank=True)
    juniorSchool = models.CharField('毕业初中', max_length=50)
    testScore1 = models.DecimalField('初三上学期期中考成绩', max_digits=5, decimal_places=2, null=True, blank=True)
    testRank1 = models.IntegerField('初三上学期期中考年级排名', null=True, blank=True)
    testScore2 = models.DecimalField('初三上学期期末考成绩', max_digits=5, decimal_places=2, null=True, blank=True)
    testRank2 = models.IntegerField('初三上学期期末考年级排名', null=True, blank=True)
    specialty = models.CharField('特长', max_length=200, null=True, blank=True)
    photo = models.ImageField('照片', upload_to=upload_file)
    zip_file = RestrictedFileField('证明文件', upload_to=upload_file, null=True, blank=True,
                                   content_types=['application/zip', 'application/octet-stream'], max_upload_size=20971520)
    # email = models.EmailField(verbose_name="邮箱", unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '学生'
        verbose_name_plural = '学生'


class Certification(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    classRoom = models.CharField('试室号', max_length=50)
    seatNo = models.CharField('座位号', max_length=20)

    class Meta:
        verbose_name = '准考证'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


