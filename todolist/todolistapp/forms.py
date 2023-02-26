from django import forms


class AddForm(forms.Form):
    btn = forms.CharField()


class DeleteForm(forms.Form):
    btn = forms.CharField()


class AddProjectForm(forms.Form):
    project_name = forms.CharField()
    add_task = forms.CharField()
    status = forms.ChoiceField(choices=(('1','Done'), ('2','Undone')))
