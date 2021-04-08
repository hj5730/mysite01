
mydict = {
    'no': 1,
    'name': '김현지'
}

# email = mydict['email']
email = mydict.get('email')
print(email)

page = int(request.GET.setDefault('p', '1'))