# ruleid: python.custom-credit-group.no-variables-in-log-messages
import uuid
user_id = uuid.uuid4()
django_rest_logger.log.error(f'Account not found for {user_id}')