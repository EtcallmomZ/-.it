from django.contrib import admin
from myapp.models import Item , BorrowRequest
from myapp.models import Item,BorrowRequest

# Register your models here.
# บอกว่าให้สิทธิ์เฉพาะใครบ้าง พวกเรา admin เท่านั้นถึงจะมีสิทธิ์จัดการไฟล์หลังบ้าน
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','serial_number','total_stock')
    search_fields = ('name','serial_number')

@admin.register(BorrowRequest)
class BorrowRequestAdmin(admin.ModelAdmin):
    list_display = (
        'requester',
        'item',
        'start_date',
        'status',
        'request_date'
    )

    list_filter = ('status','request_date','item')
    search_fields = ('requester__username','item_name','serial_number')
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
    action = ['approve_request','reject_request']

    def approve_request(self,request,queryset):
        queryset.update(status= 'APPROVED')
        self.message_user(request,f"{queryset.count()} คำขอถูกอนุมัติแล้ว")
    approve_request.short_description = "อนุมัติคำขอที่เลือก"

    def reject_request(self,request,queryset):
        queryset.update(status='REJECTED')
        self.message_user(request,f"{queryset.count()} คำขอถูกปฏิเสธแล้ว")
    reject_request.short_description = " ปฏิเสธคำขอที่เลือก"