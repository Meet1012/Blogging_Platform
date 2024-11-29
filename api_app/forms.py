from django import forms


class Login_form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class Register_form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class Create_Blog(forms.Form):
    title = forms.CharField(max_length=200, label="New Title")
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))

class Edit_Blog(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    def custom(self, obj):
        if "blog_title" in obj:
            self.initial['title'] = obj["blog_title"]
            self.initial['content'] = obj["blog_content"]
            
class Admin_Page(forms.Form):
    roles = [("admin", "Admin"), ("mod", "Moderator"),("user", "User")]
    role = forms.ChoiceField(choices=roles, widget=forms.Select, label="Give Roles")