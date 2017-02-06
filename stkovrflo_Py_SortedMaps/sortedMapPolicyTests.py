import aerospike
import time
from aerospike import predicates as p

def print_result((key, metadata, record)):
   print(record)

config = { 'hosts': [ ("localhost", 3000), ] }
client = aerospike.client(config).connect()

print "Regardless of map_policy, all API calls will work, difference is PERFORMANCE."
print "But to really test this, need much larger map bin than the example below."

print "Define MAP_UNORDERED map policy"
key = ("test", "demo", 'k1')
map_policy={'map_order':aerospike.MAP_UNORDERED}
#map_policy={'map_sort':aerospike.MAP_UNORDERED}
client.map_set_policy(key, "mymap1", map_policy)
client.put(key, {'name': "testRecord", "mymap1":{"b":5, "d":7, "a":10, "c":12, "f":13, "e":22, "i":5, "h":7, "g":33} })

# Query for sorted value
print "Sorted by values, 2 - 14, map_policy unordered defined."
start_time = time.time()
ret_val = client.map_get_by_value_range(key, "mymap1", 2, 14, aerospike.MAP_RETURN_VALUE)
duration = time.time() - start_time
print "UNORDERED duration = " 
print duration
print ret_val

print "Define MAP_KEY_VALUE_ORDERED map policy"
key = ("test", "demo", 'k2')
map_policy={'map_order':aerospike.MAP_KEY_VALUE_ORDERED}
client.map_set_policy(key, "mymap2", map_policy)
client.put(key, {'name': "testRecord", "mymap2":{"b":5, "d":7, "a":10, "c":12, "f":13, "e":22, "i":5, "h":7, "g":33} })

# Query for sorted value
print "Sorted by values, 2 - 14,  key_value_ordered map_policy defined."
start_time = time.time()
ret_val = client.map_get_by_value_range(key, "mymap2", 2, 14, aerospike.MAP_RETURN_VALUE)
duration2 = time.time() - start_time
print "KEY_VALUE_ORDERED duration = "
print duration2
print ret_val
 

print "Don't define any map policy"
key = ("test", "demo", 'k3')
client.put(key, {'name': "testRecord", "mymap3":{"b":5, "d":7, "a":10, "c":12, "f":13, "e":22, "i":5, "h":7, "g":33} })

# Query for sorted value
print "Sorted by values, 2 - 14, no map_policy defined."
start_time = time.time()
ret_val = client.map_get_by_value_range(key, "mymap3", 2, 14, aerospike.MAP_RETURN_VALUE)
duration3 = time.time() - start_time
print "DEFAULT POLICY - no policy defined, duration = " 
print duration3
print ret_val

