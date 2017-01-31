import aerospike
from aerospike import predicates as p

def print_result((key, metadata, record)):
   print(record)

config = { 'hosts': [ ("localhost", 3000), ] }
client = aerospike.client(config).connect()

# Map Index Example - you can create indexes on Map Keys or Map Values

print "Not creating any MAP SIs"
# Create index on Map Values.
#client.index_map_values_create("test", "demo", "mymap", aerospike.INDEX_NUMERIC, "map-val-idx", {})
#client.index_map_keys_create("test", "demo", "mymap", aerospike.INDEX_STRING, "map-key-idx", {})

# Insert the records
print 'Test Repeated Key map: {"a":1, "b":5, "a":3,"a":1, "b":2, "c":3} }'
key = ("test", "demo", 'km1')
client.put(key, {'name': "Map:1,2,3", "mymap":{"a":1, "b":5, "a":3,"a":1, "b":2, "c":3} })
ret_val2 = client.map_get_by_index_range(key, "mymap", 0, 3, aerospike.MAP_RETURN_VALUE)
print ret_val2

key = ("test", "demo", 'km2')
client.put(key, {'name': "Map:5,7,11,11", "mymap":{"a":5, "b":7, "c":11, "d":11} })

key = ("test", "demo", 'km3')
client.put(key, {'name': "Map:5,7",  "mymap":{"a":5, "b":7} })

key = ("test", "demo", 'km4')
client.put(key, {'name': "Map:5,7,11",  "mymap":{"a":5, "b":7, "c":11} })

print "\nTest Record (diff keys, same data) for map_order tests is:"
print ' "mymap":{"b":5, "d":7, "a":10, "c":12, "f":13, "e":22, "i":5, "h":7, "g":33} '

print "Define MAP_UNORDERED map policy"
key = ("test", "demo", 'km5')
#map_policy={'map_order':aerospike.MAP_UNORDERED}
map_policy={'map_sort':aerospike.MAP_UNORDERED}
client.map_set_policy(key, "mymap", map_policy)
client.put(key, {'name': "Map:5,7,10,12", "mymap":{"b":5, "d":7, "a":10, "c":12, "f":13, "e":22, "i":5, "h":7, "g":33} })

# Query for sorted value
print "Sorted by values, 2 - 14, map_policy unordered defined."
ret_val = client.map_get_by_value_range(key, "mymap", 2, 14, aerospike.MAP_RETURN_VALUE)
print ret_val

# Query for sorted map key
print "Sorted by map keys, d - g , map_policy unordered defined."
ret_val = client.map_get_by_key_range(key, "mymap", 'd', 'g', aerospike.MAP_RETURN_VALUE)
print ret_val

#get first 3 indexes 
print "Index 0 - 3"
ret_val2 = client.map_get_by_index_range(key, "mymap", 0, 3, aerospike.MAP_RETURN_VALUE)
print ret_val2
 

print "Define MAP_KEY_VALUE_ORDERED map policy"
key = ("test", "demo", 'km6')
#map_policy={'map_order':aerospike.MAP_KEY_VALUE_ORDERED}
map_policy={'map_sort':aerospike.MAP_KEY_VALUE_ORDERED}
client.map_set_policy(key, "mymap", map_policy)
client.put(key, {'name': "Map:5,7,10,12", "mymap":{"b":5, "d":7, "a":10, "c":12, "f":13, "e":22, "i":5, "h":7, "g":33} })

# Query for sorted value
print "Sorted by values, 2 - 14,  key_value_ordered map_policy defined."
ret_val = client.map_get_by_value_range(key, "mymap", 2, 14, aerospike.MAP_RETURN_VALUE)
print ret_val

# Query for sorted map key
print "Sorted by map keys, d - g , key_value_ordered map_policy defined."
ret_val = client.map_get_by_key_range(key, "mymap", 'd', 'g', aerospike.MAP_RETURN_VALUE)
print ret_val

#get first 3 indexes 
print "Index 0 - 3"
ret_val2 = client.map_get_by_index_range(key, "mymap", 0, 3, aerospike.MAP_RETURN_VALUE)
print ret_val2
 

print "Don't define any map policy"
key = ("test", "demo", 'km7')
#map_policy={'map_order':aerospike.MAP_UNORDERED}
#map_policy={'map_sort':aerospike.MAP_UNORDERED}
#client.map_set_policy(key, "mymap", map_policy)
client.put(key, {'name': "Map:5,7,10,12", "mymap":{"b":5, "d":7, "a":10, "c":12, "f":13, "e":22, "i":5, "h":7, "g":33} })

# Query for sorted value
print "Sorted by values, 2 - 14, no map_policy defined. What is the default? key_value_ordered?"
ret_val = client.map_get_by_value_range(key, "mymap", 2, 14, aerospike.MAP_RETURN_VALUE)
print ret_val

# Query for sorted map key
print "Sorted by map keys, d - g , no map_policy defined. What is the default? key_value_ordered?"
ret_val = client.map_get_by_key_range(key, "mymap", 'd', 'g', aerospike.MAP_RETURN_VALUE)
print ret_val

#get first 3 indexes 
print "Index 0 - 3"
ret_val2 = client.map_get_by_index_range(key, "mymap", 0, 3, aerospike.MAP_RETURN_VALUE)
print ret_val2
