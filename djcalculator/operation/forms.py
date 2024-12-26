from django import forms

class VehicleForm(forms.Form):
    name=forms.CharField()
    running_km=forms.IntegerField()
    OWNER_CHOICE=(
        ("firstowner","First Owner"),
        ("secondowner","Second Owner")
    )
    price=forms.IntegerField()
    FUEL_CHOICE=(
        ("petrol","Petrol"),
        ("disel","Disel")
    )

    fuel_type=forms.ChoiceField(choices=FUEL_CHOICE)

    owner_type=forms.ChoiceField(choices=OWNER_CHOICE)


class BMRFrom(forms.Form):

    weight_in_kg=forms.IntegerField()
    height_in_cm=forms.IntegerField()
    age_in_year=forms.IntegerField()
    Gender_choice=(
        ("male","Male"),
        ("female","Female")
    )
    gender=forms.ChoiceField(choices=Gender_choice)
    activity_choice=(
        (1.2,"SEDENTARY"),
        (1.375,"LIGHTLY ACTIVE"),
        (1.55,"MODERATLY ACTIVE"),
        (1.725,"VERY ACTIVE"),
        (1.9,"EXTRA ACTIVE")
    )
    activity_choice=forms.ChoiceField(choices=activity_choice)

class SingUpForm(forms.Form):
    email=forms.EmailField()
    username=forms.CharField()
    password1=forms.CharField()
    password2=forms.CharField()


class AppoinmentRequestForm(forms.Form):
    First_Name=forms.CharField()
    Last_Name=forms.CharField()
    Contact_number=forms.CharField()
    Email_Address=forms.EmailField()
    Address=forms.CharField()
    street_address=forms.CharField()
    city=forms.CharField()
    state_or_province=forms.CharField()
    postel_or_Zip_Code=forms.CharField()
    Date=forms.DateField()


class BmiForm(forms.Form):
    height=forms.IntegerField()
    weight=forms.IntegerField()
    email=forms.ema


class MilageForm(forms.Form):
    distance=forms.IntegerField()
    consumption=forms.IntegerField()



class EmiForm(forms.Form):
    amount=forms.IntegerField(required=True,error_messages={'required':'please enter amount'})
    interest=forms.IntegerField(required=True,error_messages={'required':'please enter interest'})
    tenure=forms.IntegerField(required=True,error_messages={'required':'please enter year'})



class CalorieForm(forms.Form):

    weight=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    height=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    Gender_choice=(
        ("male","Male"),
        ("female","Female")
    )
    gender=forms.ChoiceField(choices=Gender_choice,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))
    activity_choice=(
        (1.2,"SEDENTARY"),
        (1.375,"LIGHTLY ACTIVE"),
        (1.55,"MODERATLY ACTIVE"),
        (1.725,"VERY ACTIVE"),
        (1.9,"EXTRA ACTIVE")
    )
    activity_level=forms.ChoiceField(choices=activity_choice,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))
