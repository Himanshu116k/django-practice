from django.contrib import admin
from .models import ChaiVarity,ChaiCertificate,ChaiReview,Store

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiCertificateInline(admin.ModelAdmin):
    list_display=('chai','certificate_no')

class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    list_filter = ('type','date_added') 
    inlines = [ChaiReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_varities',)

admin.site.register(ChaiVarity,ChaiVarityAdmin) 
admin.site.register(Store,StoreAdmin) 
admin.site.register(ChaiCertificate,ChaiCertificateInline) 
# admin.site.register(ChaiReview,ChaiReviewInline)