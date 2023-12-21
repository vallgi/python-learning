language='c#'
if language == 'python':
    print('languageis python')
elif language == 'java':
    print('language is java')

else:
    print('No mismatch')

    user = 'Admin'
    logged_in =True
    if user == 'Admin'and logged_in:
        print ('Admin page')
    else:
        print('bad creds')
    if not logged_in:
        print('please log in')
    else:
        print('welcome')