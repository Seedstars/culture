import uuid
user_id = uuid.uuid4()
name = 'Jogn'
username = ''
detail = {
    'username': '',
    'name': 'Jogn',
    'user_id': user_id
}

# ruleid: python.custom-credit-group.no-variables-in-log-messages
django_rest_logger.log.error(f'Account not found for {user_id}')

# ruleid: python.custom-credit-group.no-variables-in-log-messages
django_rest_logger.log.error(
    f'Account not found for {user_id}'
    f'Maybe you misspelt your name {name}'
    f'Or your username {username} was missing'
    f'Or, just check this detail: {detail}'
)

# ok: python.custom-credit-group.no-variables-in-log-messages
django_rest_logger.log.error('Account not found for', details={'user_id':str(user_id)})