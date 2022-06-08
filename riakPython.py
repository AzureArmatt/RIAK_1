import riak

myClient = riak.RiakClient(pb_port=8098, protocol='pbc')

bucket = myClient.bucket('s25333')

val = {
    'name': 'Mateusz',
    'surname': 'Rogulski',
    'GPA': 4.0,
}
key = bucket.new('Mateusz', data=val)
key.store()

fetched = bucket.get('Mateusz')
print(fetched)

fetched.data['GPA'] = 3.0
fetched.store()

fetched = bucket.get('Mateusz')
print(fetched)

fetched.delete()

fetched = bucket.get('Mateusz')