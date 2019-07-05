from betterreads import client

key = 'UnJEUENuYcvAB9ZAWrD7Q'

secret = 'RgEtOdnNHFxnkumatFOLgzPnfMeN0dQEJ8DbjLV4'

gc = client.GoodreadsClient(key,secret)

author = gc.author(2618)
type(author)
print(author)
