inp = input('file input? ')
gig = inp.lower()
# sany = gig.split('.')

if 'jpeg' in gig:
    print('image/jpeg')
elif 'jpg' in gig:
    print('image/jpeg')
elif 'gif' in gig:
    print('image/gif')
elif 'png' in gig:
    print('image/png')
elif 'pdf' in gig:
    print('application/pdf')
elif 'txt' in gig:
    print('text/plain')
elif 'zip' in gig:
    print('application/zip')
else:
    print('application/octet-stream')