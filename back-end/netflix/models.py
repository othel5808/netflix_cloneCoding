from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser

class Account( AbstractBaseUser ):
    account_id = models.EmailField(primary_key=True)
    pay_type = models.ForeignKey("Subscribe", related_name="subscribe", on_delete=models.CASCADE,
                                 db_column = "subscribe_type")
    personality_id = models.ForeignKey("Personality", related_name="personal",
                                       on_delete=models.CASCADE, db_column="personal")

class Personality :
    pid = models.AutoField(primary_key=True)
    name = models.CharField(help_text='각 개인 계정 이름', blank=False, null=False)
    Recommend_id = models.IntegerField()
    watch_list = models.ForeignKey(
        help_text="시청한 컨텐츠 기록", related_name="content", on_delete=models.CASCADE
    )
    Favorite = models.ForeignKey(
        help_text = "즐겨찾기", related_name="favorite", on_delete=models.CASCADE
    )
    icon = models.ImageField(upload_to='image/', default='0.jpg', blank=False, null=False )


class Subscribe:
    type_id = models.AutoField(primary_key = True )
    allow_account = models.IntegerField( help_text="하나의 어카운트 당, 허용되는 각 계정의 수",
        blank=False, null= False)
    allow_device = models.IntegerField(help_text="디바이스에서 사용가능",
                                       blank=False, null= False)
    limit_per_watch = models.IntegerField( help_text = "시청 가능 횟수",
                                           blank=False, null=False)
    HD_Quality = models.BooleanField(default=False, blank=False, null=False)
    UHD_Qulity = models.BooleanField(default=False, blank=False, null=False)

class Content:
    movie_id = models.AutoField( primary_key=True )
    title= models.CharField( max_length=100 )
    director = models.ForeignKey(
        help_text = "감독 이름", related_name="relevant_person", on_delete=models.CASCADE
    )
    actor = models.ForeignKey(
        help_text = "배우 이름", related_name="relevant_person", on_delete=models.CACADE
    )
    explain= models.TextField( max_length=1000 )
    genre = models.TextField(help_text="장르", max_length = 100 )
    thumbs_up = models.IntegerField( help_text="추천 수", blank=False, null=False )
    thumbs_down = models.IntegerFiel( help_text="비 추천수", blank=False, null=False )
    TplayTime = models.TimeField(help_text="총 플레이 타임")
    mediaLink= models.CharField(help_text= "영상 링크", max_length=100)
    PG = models.ForeignKey(
        help_text="시청 가능 연령 구분", blank=False, null=False
    )
    mainImage= models.CharField(help_text="메인 이미지", blank=False, null=False, max_length=100)
    stealImage=models.CharField(help_text="영상 내 이미지", blank=False, null=False, max_length=100)
    thumbnail=models.CharField(help_text="썸네일 이미지 링크", blankb=False, null=False, max_length=100)
    demo_video = models.CharFiel(help_text="데모 영상 링크", blank=False, null=False, max_length=100)


class PG:
    pg_id = models.AutoField(help_text="그레이드 순번")
    explain = models.CharField(help_text="각 시청 연령별 안내 문구", max_length=200)
    grated_mark=models.CharField(help_text="각 가능 연령별 마크 링크", blank=False, null=False, max_length=100)


