from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):
    def create_user(self, email, password, username, first_name, last_name,
                    reg_num, stream, course, dob, phn_num, gender):
        user= self.model( email=email, username=username,first_name=first_name,last_name=last_name,
                          reg_num=reg_num, stream=stream, course=course, dob=dob, phn_num=phn_num,gender=gender)
        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username, first_name, last_name,
                         reg_num, stream, course, dob, phn_num, gender):
        user = self.create_user(email=email, username=username,password=password, first_name=first_name,
                                last_name=last_name, reg_num=reg_num, stream=stream, course=course, dob=dob,
                                phn_num=phn_num,gender=gender)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email_):
        return self.get(email=email_)

# Regular expression validators
phn_num_regex=RegexValidator(regex=r'^[0-9]{10}')
reg_num_regex=RegexValidator(regex=r'^[0-9A-Za-z]')

# Choices for choice fields
gender_choice = (
    ('Other', 'other'),
    ('Male', 'male'),
    ('Female', 'female')
)
stream_choice = (
    ('it', 'IT'),
    ('ece', 'ECE'),
    ('civil', 'CIVIL'),
    ('eee', 'EEE'),
    ('mech', 'MECH'),
    ('cse', 'CSE')
)
course_choice = (
    ('btech', 'B Tech'),
    ('mtech', 'M Tech'),
    ('mba', 'M Ba'),
    ('msc', 'M Sc'),
    ('bsc','B Sc'),
)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email Address', unique=True,blank=True)
    username = models.CharField(verbose_name='Username', max_length=20, unique=True, blank=True)
    first_name = models.CharField(verbose_name='First Name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Last Name', max_length=30, blank=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    dob = models.DateField(verbose_name='Date of Birth', blank=True)
    reg_num = models.CharField(verbose_name='Registration Number', max_length=10, validators=[reg_num_regex], blank=True)
    phn_num = models.CharField(verbose_name='Phone Number', max_length=10, validators=[phn_num_regex],blank=True)
    gender = models.CharField(verbose_name='Gender',max_length=7, choices=gender_choice, blank=True)
    stream = models.CharField(verbose_name='Stream', max_length=5, choices=stream_choice, blank=True)
    course = models.CharField(verbose_name='Course', max_length=25, choices=course_choice, blank=True)
    is_cr = models.BooleanField(verbose_name='Class Representative', default=False, blank=True)
    is_faculty = models.BooleanField(verbose_name='Faculty', default= False, blank=True)
    is_active = models.BooleanField(verbose_name='Active', default=True, blank=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=False, blank=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username',
                        'dob', 'reg_num', 'phn_num', 'stream',
                        'course', 'gender']

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.email

    def natural_key(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name
