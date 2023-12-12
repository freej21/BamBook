from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
import sweetify
from django.contrib.auth.decorators import login_required
import random
from django.shortcuts import get_object_or_404
from django.contrib import messages


#hash the name in feedback



def landing_page(request):
    return render(request, 'book/landing_page.html')

@login_required
def visitors(request):
    visitors = Visitor.objects.all()

    context = {
        'visitors': visitors,
        'title': 'Dashboard',
    }

    return render(request, 'book/visitors.html', context)




from django.core.exceptions import ObjectDoesNotExist

def enter_unique_id(request):
    if request.method == 'POST':
        unique_id_form = UniqueIDForm(request.POST)
        if unique_id_form.is_valid():
            unique_id = unique_id_form.cleaned_data['unique_id']

            try:
                # Check if the unique_id exists in the database
                visitor = Visitor.objects.get(unique_id=unique_id)

                existing_feedback = Feedback.objects.filter(visitor=visitor).exists()

                if existing_feedback:
                    messages.error(request, 'This ID has already provided feedback.', extra_tags='error-auto-dismiss')
                    return redirect('enter-unique-id')  # Redirect to the same page or another appropriate page

                # Redirect to the feedback page with the visitor's ID in the URL
                return redirect('provide-feedback', visitor_id=visitor.id)
                
            except ObjectDoesNotExist:
                messages.error(request, 'Invalid ID', extra_tags='error-auto-dismiss')
        else:
            messages.error(request, 'Invalid ID', extra_tags='error-auto-dismiss')

    else:
        unique_id_form = UniqueIDForm()

    context = {'unique_id_form': unique_id_form}
    return render(request, 'book/unique_id.html', context)


# views.py
def provide_feedback(request, visitor_id):
    visitor = get_object_or_404(Visitor, id=visitor_id)

    if request.method == 'POST':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback = feedback_form.save(commit=False)
            feedback.visitor = visitor
            feedback.save()
            sweetify.toast(request, 'Thanks for feedback', button='Ok', timer=5000)
            return redirect('enter-unique-id')
        else:
            print("Form errors:", feedback_form.errors)
            print("Form data:", request.POST)
    else:
        feedback_form = FeedbackForm()

    feedbacks = Feedback.objects.all()

    # Calculate average ratings for each item dynamically
    

    context = {
        'feedbacks': feedbacks,
        'feedback_form': feedback_form,
        'visitor': visitor,
    }
    return render(request, 'book/feedback.html', context)



def feedback_and_average_rating(request):
    feedbacks = Feedback.objects.all()
    avg_ratings = Feedback.get_average_rating()
    # Create a dictionary with the averages
    context = {
        'avg_rating_item_1': avg_ratings[0],
        'avg_rating_item_2': avg_ratings[1],
        'avg_rating_item_3': avg_ratings[2],
        'avg_rating_item_4': avg_ratings[3],
        'avg_rating_item_5': avg_ratings[4],
        'avg_rating_item_6': avg_ratings[5],
        'avg_rating_item_7': avg_ratings[6],
        'avg_rating_item_8': avg_ratings[7],
        'avg_rating_item_9': avg_ratings[8],
        'feedbacks': feedbacks,
    }

    # Render the template with the context
    return render(request, 'book/feedback_and_average_rating.html', context)

def add_visitor(request):

    if request.method == 'POST':
        visitor_form = VisitorForm(request.POST, request.FILES)
        if visitor_form.is_valid():
            visitor = visitor_form.save(commit=False)
           # Generate an 8-digit random number
            eight_digit_number = random.randint(10000000, 99999999)

            # Get the last two digits of the 8-digit number
            last_two_digits = eight_digit_number % 100

            # Create a 10-digit numeric ID
            numeric_id = f"{eight_digit_number:08d}-{last_two_digits:02d}"

            # Assign the generated numeric ID to the unique_id field
            visitor.unique_id = numeric_id

            # Check if 'photo_data' is in the POST data
            if 'photo_data' in request.POST:
                # Get the Base64-encoded image data
                photo_data = request.POST.get('photo_data', '')
                if photo_data:
                    # Decode the Base64-encoded image data
                    try:
                        image_data = base64.b64decode(photo_data.split(',')[1])
                    except Exception as e:
                        print("Error decoding base64 data:", e)
                        return JsonResponse({'message': 'Error decoding base64 data.'}, status=400)

                    # Save the image data as the 'captured_photo' field
                    visitor.captured_photo.save('captured_photo.jpg', ContentFile(image_data))

            visitor.save()  # Save the visitor model after processing the image

            sweetify.toast(request, 'Successfully Updated Client.', button='Ok', timer=5000)

            return redirect('visitor-receipt')
        

    else:
        visitor_form = VisitorForm()


    context = {
        'title': 'Visitor',
        'form': visitor_form,
    }
    return render(request, 'book/add_visitor.html', context)


def save_captured_photo(request):
    if request.method == 'POST':
        photo_data = request.POST.get('photo_data', '')
        if photo_data:
            try:
                image_data = base64.b64decode(photo_data.split(',')[1])
                visitor = Visitor(captured_photo=ContentFile(image_data, name='captured_photo.jpg'))
                visitor.save()
                return JsonResponse({'message': 'Photo saved successfully.'})
            except Exception as e:
                print("Error saving photo:", e)
                return JsonResponse({'message': 'Error saving photo.'}, status=400)
    
    return JsonResponse({'message': 'Invalid request.'}, status=400)




def visitor_receipt(request):
    receipt = Visitor.objects.latest('id')
    visitor = Visitor.objects.latest('name') 

    context = {
        'receipt': receipt,
        'visitor': visitor,
        'title': "Print Receipt",
    }
    return render(request, 'book/receipt.html', context)


