from django.db import models
from django.utils import timezone

class item(models.Model):
    stat = models.CharField(max_length=12)  #상태
    make_date = models.DateField()          #구분
    dn = models.CharField(max_length=4)     #주/야
    line = models.CharField(max_length=8)   #등록라인
    line_des = models.CharField(max_length=48)  #등록라인내역
    defect_model_des = models.CharField(max_length=48)    #불량품번내역
    defect_part_code = models.CharField(max_length=4)   #귀책처
    defect_part_des = models.CharField(max_length=16)   #귀책처내역
    defect_code = models.CharField(max_length=8)        #불량코드
    defect_category = models.CharField(max_length=48)        #불량내역
    defect_amount = models.IntegerField()               #불량수량
    defect_des = models.CharField(max_length=128)       #불량현상
    defect_action = models.CharField(max_length=128)    #조치내용
    defect_objection = models.CharField(max_length=128) #이의제기내역
    updateDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s %d" % (self.line, self.defect_amount)
