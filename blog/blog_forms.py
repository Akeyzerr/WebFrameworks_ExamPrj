# from django import forms
# from django.core.exceptions import ValidationError
#
# from .models import Recipe
#
#
# class RecipeForm(forms.ModelForm):
#     def clean_time(self):
#         time = self.cleaned_data['time']
#         if time < 0:
#             raise ValidationError(f"Time should be greater than or equal to zero. Now it's {time}")
#         return self.cleaned_data['time']
#
#     class Meta:
#         model = Recipe
#         fields = "__all__"
#
#     widgets = {
#         "time": forms.TimeInput(),
#     }
