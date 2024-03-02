
for value in list_values:
    new_list_values = []

    # ruleid: python.custom-credit-group.no-iterable-updates-inside-loop
    list_values[0] = 'new_item'

    # todoruleid: python.custom-credit-group.no-iterable-updates-inside-loop
    list_values = new_list_values

    # todoruleid: python.custom-credit-group.no-iterable-updates-inside-loop
    list_values.append('new_item')

    # todoruleid: python.custom-credit-group.no-iterable-updates-inside-loop
    list_values.insert(-1, 'new_item')

    # todoruleid: python.custom-credit-group.no-iterable-updates-inside-loop
    list_values.extend(new_list_values)

    # todoruleid: python.custom-credit-group.no-iterable-updates-inside-loop
    list_values.remove('existing_item')

    # todoruleid: python.custom-credit-group.no-iterable-updates-inside-loop
    list_values.pop(-1)

    # todoruleid: python.custom-credit-group.no-iterable-updates-inside-loop
    list_values.sort()

    # todoruleid: python.custom-credit-group.no-iterable-updates-inside-loop
    list_values.reverse()
