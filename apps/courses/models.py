#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from DjangoUeditor.models import UEditorField


from django.db import models
from organization.models import CourseOrg, Teacher


# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name="课程机构",null=True,blank=True)
    name = models.CharField(max_length=50,verbose_name="课程名")
    desc = models.CharField(max_length=300,verbose_name="课程描述")
    detail=UEditorField(verbose_name=u"课程详情",width=600, height=300,imagePath="course/ueditor/",
                        filePath="course/ueditor/",default='')

    is_banner = models.BooleanField(default=False,verbose_name="是否轮播")
    teacher = models.ForeignKey(Teacher,verbose_name="讲师",null=True,blank=True)
    degree = models.CharField(verbose_name="难度",choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=3)
    learn_times = models.IntegerField(default=0,verbose_name="学习时长（分钟数）")
    students = models.IntegerField(default=0,verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m",verbose_name="封面图",max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name="点击数")
    category = models.CharField(max_length=20,verbose_name="课程类别",default="后端开发")
    tag = models.CharField(default="", verbose_name="课程标签", max_length=10)
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")
    youneed_know = models.CharField(default="",max_length=300,verbose_name="课程须知")
    teacher_tell = models.CharField(default="",max_length=300,verbose_name="老师告诉你")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        #获取课程章节数
        return self.lesson_set.all().count()
    get_zj_nums.short_description = "章节数"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>跳转</>")
    go_to.short_description = "跳转"


    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        #获取课程所有章节
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name="课程")
    name = models.CharField(max_length=100,verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural =verbose_name

    def get_lesson_video(self):
        #获取章节视频
        return self.video_set.all()

    def __unicode__(self):
        return self.name

class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name="章节")
    name = models.CharField(max_length=100,verbose_name="视频名")
    learn_times = models.IntegerField(default=0,verbose_name="学习时长（分钟数）")
    url = models.CharField(max_length=200,default="",verbose_name="访问地址")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural =verbose_name

    def __unicode__(self):
        return self.name

class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name="课程")
    name = models.CharField(max_length=100,verbose_name="名称")
    download = models.FileField(upload_to="course/resource/%Y/%m",verbose_name="资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural =verbose_name
