from django import forms
from django.utils.html import format_html

class WebcamCaptureWidget(forms.FileInput):
    def render(self, name, value, attrs=None, renderer=None):
        # Render the default file input field
        input_html = super().render(name, value, attrs)

        # Customize the rendering to include "Take Photo" and "Clear" buttons
        output = format_html(
            '<div class="webcam-capture-widget">'
            '<div class="webcam-capture-buttons">'
            '<button type="button" class="btn btn-danger" onclick="clearImage(\'{}\')">Clear</button>'
            '</div>'
            '{}'
            '</div>',
            name, name, input_html
        )

        return output
