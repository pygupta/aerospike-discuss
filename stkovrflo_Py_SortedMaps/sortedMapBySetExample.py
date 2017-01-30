import aerospike
from aerospike import predicates as p

def print_result((key, metadata, record)):
   print(record)

config = { 'hosts': [ ("localhost", 3000), ] }
client = aerospike.client(config).connect()

# Map Index Example - you can create indexes on Map Keys or Map Values

# Create index on Map Values.
client.index_map_values_create("test", "demo", "mymap", aerospike.INDEX_NUMERIC, "map-val-idx", {})
client.index_map_keys_create("test", "demo", "mymap", aerospike.INDEX_STRING, "map-key-idx", {})

# Insert the records
key = ("test", "demo", 'km1')
client.put(key, {'name': "Map:1,2,3", "mymap":{"a":1, "b":2, "c":3} })

key = ("test", "demo", 'km2')
client.put(key, {'name': "Map:5,7,11,11", "mymap":{"a":5, "b":7, "c":11, "d":11} })

key = ("test", "demo", 'km3')
client.put(key, {'name': "Map:5,7",  "mymap":{"a":5, "b":7} })

key = ("test", "demo", 'km4')
client.put(key, {'name': "Map:5,7,11",  "mymap":{"a":5, "b":7, "c":11} })

key = ("test", "demo", 'km5')
client.put(key, {'name': "Map:5,7,10,12", "mymap":{"a":5, "b":7, "c":10, "d":12, "e":13, "f":22, "g":5, "h":7, "i":33} })



key = ("test", "demo", 'km5')
# Query for sorted value
print "Sorted by values, 2 - 14"
ret_val = client.map_get_by_value_range(key, "mymap", 2, 14, aerospike.MAP_RETURN_VALUE)
print ret_val

#get first 3 indexes 
print "Index 0 - 3"
ret_val2 = client.map_get_by_index_range(key, "mymap", 0, 3, aerospike.MAP_RETURN_VALUE)
print ret_val2
 
