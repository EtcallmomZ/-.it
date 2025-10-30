from django.contrib import admin
from myapp.models import Item,BorrowRequest,Category

# Register your models here.

# ตัวเพิ่มหมวดหมู่แก้ไขใน /admin ได้เลย
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

# บอกว่าให้สิทธิ์เฉพาะใครบ้าง พวกเรา admin เท่านั้นถึงจะมีสิทธิ์จัดการไฟล์หลังบ้าน
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','serial_number','total_stock')
    list_filter = ('category','total_stock')
    search_fields = ('name','serial_number')

@admin.register(BorrowRequest)
class BorrowRequestAdmin(admin.ModelAdmin):
    list_display = (
        'requester',
        'item',
        'start_date',
        'end_date',
        'status',
        'request_date'
    )

    list_filter = ('status','request_date','item')
    search_fields = ('requester__username','item__name','item_serial_number')
    readonly_fields = ('request_date','requester','item','quantity')

    # เปลี่ยนได้เฉพาะ admin ก็คือพวกเรา
    fields =(
        'requester',
        'item',
        'quantity',
        'start_date',
        'end_date',
        'status',
        'admin_notes'

    )
    actions = ['approve_requests','reject_requests']

    def approve_requests(self,request,queryset):
        queryset.update(status= 'APPROVED')
        self.message_user(request,f"{queryset.count()} คำขอถูกอนุมัติแล้ว")
    approve_requests.short_description = "อนุมัติคำขอที่เลือก"

    def reject_requests(self,request,queryset):
        queryset.update(status='REJECTED')
        self.message_user(request,f"{queryset.count()} คำขอถูกปฏิเสธแล้ว")
    reject_requests.short_description = " ปฏิเสธคำขอที่เลือก"