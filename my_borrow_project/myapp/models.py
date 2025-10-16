from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
# เราจะตั้งว่าเก็บฐานข้อมูลอะไรไว้บ้าง ในไฟล์นี้

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

# Item ที่เรามีอยู่
class Item(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null = True,
        blank = True
    )

    name = models.CharField(max_length=200,verbose_name= "ชื่อของ")
    description = models.TextField(blank=True,verbose_name="รายละเอียด")
    serial_number = models.CharField(max_length=100 ,unique=True , verbose_name="รหัส")
    total_stock = models.IntegerField(default=1,verbose_name = "จำนวนรวม")
    image = models.ImageField(upload_to='item_images/',blank=True, null=True)

    class Meta:
        verbose_name = "สิ่งของ"
        verbose_name_plural = "สิ่งของ"
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return revers('item_detail',args=[str(self.id)])


# คำขอกับสถานะ
class BorrowRequest(models.Model):
    STATUS_CHOICES = (
        ('PENDING','รออนุมัติ'),
        ('APPROVED','อนุมัติ'),
        ('REJECTED','ถูกปฏิเสธ'),
        ('CANCELLED', 'ยกเลิก'),
        ('RETURNED' , 'คืนแล้ว')
    )
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE,verbose_name="สิ่งของที่ยืม")
    requester = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name="ผู้ยืม")

    quantity = models.IntegerField(default=1,verbose_name="จำนวนที่ยืม")
    request_date =  models.DateTimeField(default=timezone.now,verbose_name="วันที่ร้องขอ")
    start_date = models.DateField(verbose_name="วันที่ยืม")
    end_date = models.DateField(verbose_name="วันที่กำหนดคืน")

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default= 'PENDING',
        verbose_name =  'สถานะ'
    )

    admin_notes = models.TextField(blank=True, null=True,verbose_name="หมายเหตุ")

    class Meta:
        verbose_name = "คำขอยืม"
        verbose_name_plural = "คำขอยืม"
    
    permissions = [
        ("can_approve_reject" , "สามารถอนุมัติและปฏิเสธคำขอ")
    ]
    def __str__(self):
        return f"{self.requester.username} request {self.quantity} x {self.item.name} ({self.status})"


