from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

PAY_TYPE = (
)
class Account( AbstractBaseUser ):
    account_id = models.EmailField(primary_key=True)
    pay_type = models.ForeignKey("Subscribe", related_name="subscribe", on_delete=models.CASCADE,
                                 db_column = "subscribe_type")
    personality_id = models.ForeignKey("Personality", related_name="personal",
                                       on_delete=models.CASCADE, db_column="personal")
class Personality() :
    pid = models.AutoField(primary_key=True)
    name = models.CharField(help_text='각 개인 계정 이름', blank=False, null=False)
    Recommend_id = models.IntegerField()
    watch_list = models.ForeignKey(
        help_text="시청한 컨텐츠 기록", related_name="content", on_delete=models.CASCADE
    )

class Subscribe():
    type_id = models.AutoField(primary_key = True )
    allow_account = models.IntegerField( help_text="하나의 어카운트 당, 허용되는 각 계정의 수",
        blank=False, null= False)
    allow_device = models.IntegerField(help_text="디바이스에서 사용가능",
                                       blank=False, null= False)
    limit_per_watch = models.IntegerField( help_text = "시청 가능 횟수",
                                           blank=False, null=False)
    HD_Quality = models.BooleanField(default=False, blank=False, null=False)
    UHD_Qulity = models.BooleanField(default=False, blank=False, null=False)

