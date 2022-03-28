from django import forms

from exam_project.exam_app.models import Profile, Album


# from for creating profiles
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age']

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email'}),
            'age': forms.TextInput(
                attrs={'placeholder': 'Age'}),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        albums = Album.objects.all()
        albums.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = []


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'genre', 'description', 'image', 'price']

        labels = {
            'name': 'Album Name',
            'image': 'Image URL',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(
                attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Description', 'rows': 4}),
            'image': forms.TextInput(
                attrs={'placeholder': 'Image URL'}),
            'price': forms.TextInput(
                attrs={'placeholder': 'Price'}),
        }


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artist', 'genre', 'description', 'image', 'price']

        labels = {
            'name': 'Album Name',
            'image': 'Image URL',
        }


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = ['name', 'artist', 'genre', 'description', 'image', 'price']

        labels = {
            'name': 'Album Name',
            'image': 'Image URL',
        }
