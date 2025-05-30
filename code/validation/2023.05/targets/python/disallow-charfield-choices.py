class TestModel(Model):
    # ruleid: python.custom-credit-group.disallow-charfield-choices
    invalid_1 = rest_framework.fields.CharField(choices=['a', 'b'])

    # ruleid: python.custom-credit-group.disallow-charfield-choices
    invalid_2 = rest_framework.serializers.CharField(choices=['a', 'b'])

    # ok: python.custom-credit-group.disallow-charfield-choices
    valid = rest_framework.serializers.IntegerField(choices=['a', 'b'])
