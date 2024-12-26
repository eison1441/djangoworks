from django.shortcuts import render

# Create your views here.

from django.views.generic import View

from store.forms import BookForm

from store.models import Book

class BookCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BookForm()

        return render(request,"book_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BookForm(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Book.objects.create(
                title=data.get("title"),
                auther=data.get("auther"),
                price=data.get("price"),
                genre=data.get("genre"),
                language=data.get("language"),
                year=data.get("year")
            )
        return render(request,"book_add.html",{"form":form_instance})