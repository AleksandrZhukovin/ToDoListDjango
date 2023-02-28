from django import forms


class InputProject(forms.Form):
    name = forms.CharField()


class InputTask(forms.Form):
    name = forms.CharField()
    priority = forms.IntegerField()
    status = forms.ChoiceField(choices=(('Undone', 'Undone'), ('Done', 'Done')))
    deadline = forms.DateField(required=False)


class EditProject(forms.Form):
    name = forms.CharField(initial='proj')
    task = forms.CharField(initial='t')


