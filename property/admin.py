from django.contrib import admin

from .models import Flat, Complain, Owner


class PropertyInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ['owner', 'flat']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town',
                     'address',
                     'owner']
    readonly_fields = ['created_at']
    list_display = ['address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',
                    'owner_pure_phone',
                    'owners_phonenumber']
    list_editable = ['new_building']
    list_filter = ['new_building',
                   'rooms_number',
                   'has_balcony']
    raw_id_fields = ['liked_by']


@admin.register(Complain)
class ComplainsAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']
    list_display = ['user', 'flat', 'complaint_text']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    inlines = [
        PropertyInline
    ]
    exclude = ['flat']
