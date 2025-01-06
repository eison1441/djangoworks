from django import forms

from store.models import Book


# class BookForm(forms.Form):

#     title=forms.CharField()

#     auther=forms.CharField()

#     price=forms.IntegerField()

#     genre=forms.CharField()

#     language=forms.CharField()

#     year=forms.CharField()

#     image=forms.ImageField()



class BookForm(forms.ModelForm):

    class Meta:

        model=Book

        fields="__all__"

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "auther":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "price":forms.NumberInput(attrs={"class":"form-control mb-3"}),
            "genre":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "language":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "year":forms.NumberInput(attrs={"class":"form-control mb-3"}),
            "image":forms.FileInput(attrs={"class":"form-control mb-3"})
        }
    