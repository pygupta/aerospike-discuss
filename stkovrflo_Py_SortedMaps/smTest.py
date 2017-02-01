import aerospike
from aerospike import predicates as p

config = { 'hosts': [ ("localhost", 3000), ] }
client = aerospike.client(config).connect()

# Insert the records

key = ("test", "demo", 'sm1')

print "Define MAP_UNORDERED map policy"
map_policy={'map_order':aerospike.MAP_UNORDERED}
#map_policy={'map_sort':aerospike.MAP_UNORDERED}
client.map_set_policy(key, "mymap", map_policy)
client.put(key,  {'mymap':{"ba":10, "ab":5, "ec":12, "fd":7, "ae":22, "gf":13, "fg":33, "hi":7, "ai":5}})

# Query for sorted value
print "Sorted by values, 2 - 14, map_policy unordered defined."
ret_val = client.map_get_by_value_range(key, "mymap", 2, 14, aerospike.MAP_RETURN_VALUE)
print ret_val

# Query for sorted rank
print "Sorted by rank, 0 - 3, map_policy unordered defined."
ret_val = client.map_get_by_rank_range(key, "mymap", 0, 3, aerospike.MAP_RETURN_VALUE)
print ret_val

# Query for sorted map key
print "Sorted by map keys, d - g , map_policy unordered defined."
ret_val = client.map_get_by_key_range(key, "mymap", 'd', 'g', aerospike.MAP_RETURN_VALUE)
print ret_val

#get first 3 indexes 
print "Index 0 - 5"
ret_val2 = client.map_get_by_index_range(key, "mymap", 0, 5, aerospike.MAP_RETURN_VALUE)
print ret_val2
 

print "Define MAP_KEY_VALUE_ORDERED map policy"
key = ("test", "demo", 'sm2')
#map_policy={'map_order':aerospike.MAP_KEY_VALUE_ORDERED}
map_policy={'map_sort':aerospike.MAP_KEY_VALUE_ORDERED}
client.map_set_policy(key, "mymap", map_policy)
client.put(key,  {'mymap':{"ba":10, "ab":5, "ec":12, "fd":7, "ae":22, "gf":13, "fg":33, "hi":7, "ai":5}})

# Query for sorted value
print "Sorted by values, 2 - 14,  key_value_ordered map_policy defined."
ret_val = client.map_get_by_value_range(key, "mymap", 2, 14, aerospike.MAP_RETURN_VALUE)
print ret_val

# Query for sorted rank
print "Sorted by rank, 0 - 3, map_policy key_value_ordered defined."
ret_val = client.map_get_by_rank_range(key, "mymap", 0, 3, aerospike.MAP_RETURN_VALUE)
print ret_val

# Query for sorted map key
print "Sorted by map keys, d - g , key_value_ordered map_policy defined."
ret_val = client.map_get_by_key_range(key, "mymap", 'd', 'g', aerospike.MAP_RETURN_VALUE)
print ret_val

#get first 3 indexes 
print "Index 0 - 5"
ret_val2 = client.map_get_by_index_range(key, "mymap", 0, 5, aerospike.MAP_RETURN_VALUE)
print ret_val2
 

print "Don't define any map policy"
key = ("test", "demo", 'sm3')
#map_policy={'map_order':aerospike.MAP_UNORDERED}
#map_policy={'map_sort':aerospike.MAP_UNORDERED}
#client.map_set_policy(key, "mymap", map_policy)
client.put(key,  {'mymap':{"ba":10, "ab":5, "ec":12, "fd":7, "ae":22, "gf":13, "fg":33, "hi":7, "ai":5}})

# Query for sorted value
print "Sorted by values, 2 - 14, no map_policy defined. What is the default? key_value_ordered?"
ret_val = client.map_get_by_value_range(key, "mymap", 2, 14, aerospike.MAP_RETURN_VALUE)
print ret_val

# Query for sorted rank
print "Sorted by rank, 0 - 3, map_policy not defined."
ret_val = client.map_get_by_rank_range(key, "mymap", 0, 3, aerospike.MAP_RETURN_VALUE)
print ret_val

# Query for sorted map key
print "Sorted by map keys, d - g , no map_policy defined. What is the default? key_value_ordered?"
ret_val = client.map_get_by_key_range(key, "mymap", 'd', 'g', aerospike.MAP_RETURN_VALUE)
print ret_val

#get first 3 indexes 
print "Index 0 - 5"
ret_val2 = client.map_get_by_index_range(key, "mymap", 0, 5, aerospike.MAP_RETURN_VALUE)
print ret_val2
