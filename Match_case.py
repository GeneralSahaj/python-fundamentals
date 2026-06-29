# Match Case statement (switch) : An alternative to using many elif statements.
#                                 Execute some code if a value matches a case.
#                                 Benefits: Clearer and syntax is more readable.

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"