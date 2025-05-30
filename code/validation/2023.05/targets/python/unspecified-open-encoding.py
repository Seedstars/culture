# ruleid: python.custom-credit-group.unspecified-open-encoding
open('file.txt')

# ok: python.custom-credit-group.unspecified-open-encoding
open('file.txt', encoding='utf8')

# ok: python.custom-credit-group.unspecified-open-encoding
open('file.txt', encoding='utf8', mode='r')
