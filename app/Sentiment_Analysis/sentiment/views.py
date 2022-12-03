from django.shortcuts import render, redirect
from django.views import View
from .models import SentimentsData
import random


def analyised_data(input_text):
    """
        Return analyised value of inout text.
    """
    remarks_list = ["Postive", "Negative"]
    return random.choice(remarks_list)


class DashoardView(View):
    """
        Dashboard View.
    """
    def get(self, request):
        sentiment_obj = SentimentsData.objects.order_by('-created_on')
        context = {
            'sentiments_data':sentiment_obj
        }
        return render(request, "index.html", context)

    def post(self, request):
        input_text = request.POST.get('input_text')
        output_remarks = analyised_data(input_text)
        dict_data = {
            'remarks':output_remarks,
            'input_txt':input_text
        }
        obj = SentimentsData.objects.create(**dict_data)
        return redirect('/')


class RemoveSentiment(View):
    """
        Delete a sentiment data with given ID.
    """
    def get(self, request, pk):
        obj = SentimentsData.objects.filter(id=pk).delete()
        return redirect('/')