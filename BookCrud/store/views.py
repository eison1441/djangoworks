from django.shortcuts import render,redirect

# Create your views here.

from django.views.generic import View

from store.forms import BookForm

from store.models import Book

from django.db.models import Q

class BookCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=BookForm()

        return render(request,"book_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BookForm(form_data,files=request.FILES)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Book.objects.create(
                title=data.get("title"),
                auther=data.get("auther"),
                price=data.get("price"),
                genre=data.get("genre"),
                language=data.get("language"),
                year=data.get("year"),
                image=data.get("image"),
            )

            return redirect("book_all")
        
        return render(request,"book_add.html",{"form":form_instance})
    

class BookListView(View):
    def get(self,request,*args,**kwargs):

        search_text=request.GET.get("search")
        # print(">>>>>>",search_text,"<<<<<<")



        qs=Book.objects.all()


        if search_text:

            qs=qs.filter(Q(title__contains=search_text)|Q(auther__contains=search_text))

        return render(request,"book_list.html",{"data":qs})
    

class BookDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Book.objects.get(id=id)

        return render(request,"book_detal.html",{"data":qs})
    

class BookDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Book.objects.get(id=id).delete()

        return redirect("book_all")
    
class BookUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        book_obj=Book.objects.get(id=id)

        book_dict={

            "title":book_obj.title,
            "auther":book_obj.auther,
            "price":book_obj.price,
            "genre":book_obj.genre,
            "language":book_obj.language,
            "year":book_obj.year,
            

        }

        form_instance=BookForm(initial=book_dict)
        

        return render(request,"book_update.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=BookForm(form_data,files=request.FILES)

        id=kwargs.get("pk")

        if form_instance.is_valid():

            # form_instance.save()

            data=form_instance.cleaned_data

            Book.objects.filter(id=id).update(**data)

            return redirect("book_all")
        
        return render(request,"book_update.html",{"form":form_instance})

