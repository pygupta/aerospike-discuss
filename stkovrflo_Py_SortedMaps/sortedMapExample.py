import aerospike
from aerospike import predicates as p

def print_result((key, metadata, record)):
   print(record)

config = { 'hosts': [ ("localhost", 3000), ] }
client = aerospike.client(config).connect()

map_policy={'map_order':aerospike.MAP_KEY_VALUE_ORDERED}

# Insert the records
key = ("test", "demo", 'km1')
client.map_set_policy(key, "mymap", map_policy)
client.map_put(key,  "mymap", '0', 13)
client.map_put(key,  "mymap", '1', 3)
client.map_put(key,  "mymap", '2', 7)
client.map_put(key,  "mymap", '3', 2)
client.map_put(key,  "mymap", '4', 12)
client.map_put(key,  "mymap", '5', 33)
client.map_put(key,  "mymap", '6', 1)
client.map_put(key,  "mymap", '7', 12)
client.map_put(key,  "mymap", '8', 22)


# Query for sorted value
print "Sorted by values, 2 - 14"
ret_val = client.map_get_by_value_range(key, "mymap", 2, 14, aerospike.MAP_RETURN_VALUE)
print ret_val

#get first 3 indexes 
print "Index 0 - 3"
ret_val2 = client.map_get_by_index_range(key, "mymap", 0, 3, aerospike.MAP_RETURN_VALUE)
print ret_val2
 
