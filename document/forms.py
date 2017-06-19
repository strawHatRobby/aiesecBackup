from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title','description', 'document', )
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(DocumentForm, self).__init__(*args, **kwargs)
