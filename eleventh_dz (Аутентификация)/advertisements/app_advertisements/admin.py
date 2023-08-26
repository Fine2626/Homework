from django.contrib import admin
from .models import Advertisement

from django.utils.html import format_html

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'auction', 'updated_date', 'display_image']
    list_filter = ['auction', 'created_at']
    actions = ["make_auction_as_false", "make_auction_as_true"]
    fieldsets = (
        ('Общие', {"fields": ('title', 'description', 'image')}),
        ('Финансы', {"fields": ('price', 'auction'), "classes": ['collapse']})
    )

    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display(description="Изображение")
    def display_image(self, adv):
        if adv.image: 
            return format_html('<img src="{}" alt="" style="width: 50px; height: 50px;">', adv.image.url)
        else:
            return format_html('<img src="/static/img/adv.png" alt="" style="width: 50px; height: 50px;">')

admin.site.register(Advertisement, AdvertisementAdmin)