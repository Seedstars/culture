from django.db.models import ForeignKey, ManyToManyField
_relationship_set : str = 'bar_valid_set'
class FooModel(Model):
    # ruleid: python.custom-credit-group.foreign-key-and-many2many-must-set-related-name
    invalid_1 = ForeignKey(_relationship_set)

    # ruleid: python.custom-credit-group.foreign-key-and-many2many-must-set-related-name
    invalid_2 = ManyToManyField(_relationship_set)

    # ok: python.custom-credit-group.foreign-key-and-many2many-must-set-related-name
    valid_1 = ForeignKey(_relationship_set, related_name=_relationship_set)

    # ok: python.custom-credit-group.foreign-key-and-many2many-must-set-related-name
    valid_2 = ManyToManyField(_relationship_set, related_name=_relationship_set)
