from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.



class VisitorAdmin(admin.ModelAdmin):
    list_display = ('display_captured_photo','name', 'contact','formatted_date_added','get_time_in', 'get_time_out','calculate_stay_duration', 'address', 'purpose', 'department')
    search_fields = ('name', 'department')

    def formatted_date_added(self, obj):
        return obj.date.strftime('%Y-%m-%d')
    formatted_date_added.short_description = 'Date'

    def display_captured_photo(self, obj):
        return format_html('<div style="border-radius: 50%; overflow: hidden; width: 50px; height: 50px;"><img src="{}" style="width: 100%; height: 100%;" /></div>', obj.captured_photo.url)

    display_captured_photo.short_description = 'Captured Photo'

    def get_time_in(self, obj):
        time_in = timezone.localtime(obj.time_in, timezone=timezone.get_current_timezone())
        return time_in.strftime('%I:%M %p')  # Format as 12-hour with AM/PM
    get_time_in.short_description = 'Time In'

    def get_time_out(self, obj):
        if obj.time_out:
            time_out = timezone.localtime(obj.time_out, timezone=timezone.get_current_timezone())
            return time_out.strftime('%I:%M %p')  # Format as 12-hour with AM/PM
        else:
            return None
    get_time_out.short_description = 'Time Out'

    def calculate_stay_duration(self, obj):
        duration = obj.calculate_stay_duration()
        return str(duration).split('.')[0] if duration else None
    calculate_stay_duration.short_description = 'Stay Duration'


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('visitor', 'display_item_1', 'display_item_2', 'display_item_3', 'display_item_4',
                    'display_item_5', 'display_item_6', 'display_item_7', 'display_item_8', 'display_item_9', 'comment')

    def get_item_display(self, item_value):
        for value, label in Feedback.RATING_CHOICES:
            if value == item_value:
                return label
        return item_value

    def display_item_1(self, obj):
        return self.get_item_display(obj.item_1)
    display_item_1.short_description = 'SQD0'

    def display_item_2(self, obj):
        return self.get_item_display(obj.item_2)
    display_item_2.short_description = 'SQD1'

    def display_item_3(self, obj):
        return self.get_item_display(obj.item_3)
    display_item_3.short_description = 'SQD2'

    def display_item_4(self, obj):
        return self.get_item_display(obj.item_4)
    display_item_4.short_description = 'SQD3'

    def display_item_5(self, obj):
        return self.get_item_display(obj.item_5)
    display_item_5.short_description = 'SQD4'

    def display_item_6(self, obj):
        return self.get_item_display(obj.item_6)
    display_item_6.short_description = 'SQD5'

    def display_item_7(self, obj):
        return self.get_item_display(obj.item_7)
    display_item_7.short_description = 'SQD6'

    def display_item_8(self, obj):
        return self.get_item_display(obj.item_8)
    display_item_8.short_description = 'SQD7'

    def display_item_9(self, obj):
        return self.get_item_display(obj.item_9)
    display_item_9.short_description = 'SQD8'
    
class AverageFeedbackAdmin(admin.ModelAdmin):
    list_display = ('get_item_description', 'average_rating', 'rating_description')
    ordering = ['item_number']
    
    # Determine the rating range based on the average rating
    
    
    def get_item_description(self, obj):
        item_descriptions = {
            1: 'SQDO. I am satisfied with the service that I availed.',
            2: 'SQD1. I spent a reasonable amount of time for my transaction.',
            3: "SQD2. The office followed the transaction's requirements and steps based on the information provided.",
            4: "SQD3. The steps (including payment) I needed to do for my transaction were easy and simple.",
            5: "SQD4. I easily found information about my transaction from the office or its website.",
            6: "SQD5. I paid a reasonable amount of fees for my transaction.",
            7: 'SQD6. I feel the office was fair to everyone, or "walang palakasan", during my transaction.',
            8: "SQD7. I was treated courteously by the staff, and (if asked for help) the staff was helpful.",
            9: "SQD8. I got what I needed from the government office, or (if denied) denial of the request was sufficiently explained to me.",
        }
        
        return item_descriptions.get(obj.item_number, f'Item {obj.item_number}')
    
      
    
    get_item_description.short_description = 'Item Description'

admin.site.register(AverageFeedback, AverageFeedbackAdmin)

admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Feedback, FeedbackAdmin)
