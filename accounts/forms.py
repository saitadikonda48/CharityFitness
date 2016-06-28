from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import messages
from .models import MyUser, UserProfile, Message


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        if len(password1) <= 4:
            raise forms.ValidationError("Password is too short")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            exists = MyUser.objects.get(username=username)
            raise forms.ValidationError("This username is taken")
        except MyUser.DoesNotExist:
            return username
        except:
            raise forms.ValidationError("Username is already taken.")


    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            exists = MyUser.objects.get(email=email)
            messages.warning(request, "Email is already taken.")
            raise forms.ValidationError("This email is taken")
        except MyUser.DoesNotExist:
            return email
        except:
            raise forms.ValidationError("Email is already taken.")




class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'full_name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'username', 'full_name', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    username = forms.CharField(label='', 
                    widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', 
                    widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserProfileChangeForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('full_name','age','height','startWeight','startDate','goalWeight','goalDate','hobbies')
        
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter New Name'}),
            'age': forms.TextInput(attrs={'placeholder': 'Enter New Age'}),
            'height': forms.TextInput(attrs={'placeholder': 'Enter New Height'}),
            'startDate': forms.TextInput(attrs={'placeholder': 'Enter Start Date'}),
            'startWeight': forms.TextInput(attrs={'placeholder': 'Enter Start Weight'}),
            'goalDate': forms.TextInput(attrs={'placeholder': 'Enter Goal Date'}),
            'goalWeight': forms.TextInput(attrs={'placeholder': 'Enter Goal Weight'}),
            'hobbies': forms.Textarea(attrs={'placeholder': 'Enter personal hobbies here'}),
        }
        labels = {
            'height':('Height (cm)'),
            'startWeight':('Start Weight (kg)'),
            'startDate':('Start Date (YYYY-MM-DD)'),
            'goalWeight':('Goal Weight (kg)'),
            'goalDate':('Goal Date (YYYY-MM-DD)'),
            'hobbies':('Activities'),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('email', 'name', 'message')
        
