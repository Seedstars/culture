def foo():
    # ruleid: python.custom-credit-group.disallow-cleaned_data.get
    value = cleaned_data.get('id')

    # ruleid: python.custom-credit-group.disallow-cleaned_data.get
    value = self.cleaned_data.get('id')

    # ok: python.custom-credit-group.disallow-cleaned_data.get
    value = cleaned_data['id']


class FooForm(forms.Form):
    def foo(self):
        # todoruleid: python.custom-credit-group.disallow-cleaned_data.get
        value = cleaned_data.get('id')

        # todoruleid: python.custom-credit-group.disallow-cleaned_data.get
        value = self.cleaned_data.get('id')

        # todook: python.custom-credit-group.disallow-cleaned_data.get
        value = cleaned_data['id']
