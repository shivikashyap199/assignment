def suppress_exception(exception=None, result=None):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError as key_error:
                if exception is None or exception == KeyError:
                    return result if result is not None else False
                else:
                    raise key_error
            except Exception as e:
                if exception is None:
                    return False
                else:
                    raise e

        return inner

    return decorator

@suppress_exception(exception=KeyError, result=False)
def authenticate(user, password):
    print(f'authenticating {user}')
    return Users[user] == password


Users = {"user1": "password1", "user2": "password2"}
print(authenticate("user1", "password1"))  
print(authenticate("user3", "password3"))  