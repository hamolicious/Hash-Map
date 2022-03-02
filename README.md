# Hash Map
Was wondering how Hash Maps worked so I decided to create my own, this hash map uses MD5 hashing and a chaining, linked-list collision resolution. This will be the 2nd part to my "FromScratch" journey where I create projects that are usually implemented for you in almost every language to get a better understanding of them.

## Uses
```python
from hashmap import Hash

# initialise the hash
h = Hash()

# create some values
h['key'] = 'value'
h['foo'] = 'bar'

# change some values
h['foo'] = 'Hello World'

# get the values back
h.get('foo')
#>> 'Hello World'

# get the length of the hash
len(h)
#>> 2
```

