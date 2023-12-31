from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Permission

from .models import ToDoUser
import logging


logger = logging.getLogger("todo")
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
                                         help_text=("Raw passwords are not stored, so there is no way to see "
                                                    "this user's password, but you can change the password "
                                                    "using <a href=\"../password/\">this form</a>."))

    class Meta:
        model = ToDoUser
        fields = ( 'password',)

    def clean_password(self):
        return self.initial["password"]

    def save(self, commit=True, request=None):
        user = super(UserChangeForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = ToDoUser
        fields = ('email',)


    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


    def save(self, commit=True, request=None):
        user = super(UserCreationForm, self).save(commit=False)
        # set the password

        user.set_password(self.cleaned_data["password1"])
        logger.info(f"saving user {user} from django admin, {commit}")
        if commit:
            user.save()
            self.save_m2m()

        return user
@admin.register(ToDoUser)
class ToDoUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('first_name','email',)

    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_superuser', 'is_staff',
                           )},),
        ('User Group', {'fields': ('groups',)},),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number',)},),
    )

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('email', 'password1', 'password2', 'groups')},),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number')},),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


    def save_form(self, request, form, change):
        """
        Method overwritten to pass request to save method.
        :param request: The request object
        :param form: The form used (Add / Change)
        :param change: if True, change is done, or add otherwise
        :return:
        """
        return form.save(commit=False, request=request)


admin.site.register(Permission)
