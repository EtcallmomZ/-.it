from django.contrib import admin
from myapp.models import Person

# Register your models here.
# บอกว่าให้สิทธิ์เฉพาะใครบ้าง user จะเห็นหน้าเว็บคนละแบบ
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