from django.views.generic.edit import FormView
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class ImportBookView(FormView):
    template_name = "admin/book_manager/book/import.html"
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        print("dipudeey")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
