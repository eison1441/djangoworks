from django import forms


class BookForm(forms.Form):

    title=forms.CharField()

    auther=forms.CharField()

    price=forms.IntegerField()

    genre=forms.CharField()

    language=forms.CharField()

    year=forms.CharField()