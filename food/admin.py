from django.contrib import admin
import food.models as models


class ItemInline(admin.TabularInline):
    inlines = [
        'self',
    ]
    model = models.Item


class ItemGroupAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]
    list_filter = ('vendor__name',)
    search_fields = ('name', 'vendor__name')


class ItemGroupInline(admin.TabularInline):
    model = models.ItemGroup


class VendorAdmin(admin.ModelAdmin):
    inlines = [
        ItemGroupInline,
    ]


class EventAdmin(admin.ModelAdmin):
    filter_horizontal = ('vendors',)


class UserOrderItemInline(admin.TabularInline):
    model = models.UserOrderItem


class UserOrderAdmin(admin.ModelAdmin):
    inlines = [
        UserOrderItemInline,
    ]

admin.site.register(models.Event, EventAdmin)
admin.site.register(models.Vendor, VendorAdmin)
admin.site.register(models.ItemGroup, ItemGroupAdmin)
admin.site.register(models.Order)
admin.site.register(models.UserOrder, UserOrderAdmin)


