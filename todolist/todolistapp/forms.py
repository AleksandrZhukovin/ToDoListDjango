from django import forms


class InputProject(forms.Form):
    name = forms.CharField()


class InputTask(forms.Form):
    name = forms.CharField()
    status = forms.ChoiceField(choices=(('1', 'Done'), ('2', 'Undone')))