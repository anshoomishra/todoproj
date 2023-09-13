from django.forms import ModelForm
from .models import Task
from django import forms
from django.utils.timezone import now
from django.core.exceptions import ValidationError

import datetime
class FutureDateInput(forms.DateInput):
    input_type = 'date'

    def get_context(self, name, value, attrs):
        attrs.setdefault('min', now().strftime('%Y-%m-%d'))
        return super().get_context(name, value, attrs)
class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','priority','due_date']

        widgets = {
            'due_date': FutureDateInput(),

        }

    def __init__(self, *args, **kwargs):
        super(TaskCreateForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'


        self.fields['priority'].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        due_date = cleaned_data.get("due_date")
        print("due date",due_date)
        format = '%H:%M:%S'

        if (due_date < now()):
            raise ValidationError(
                "You can only book for future.", code='only book for future'
            )
        return cleaned_data
