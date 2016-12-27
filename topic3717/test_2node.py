#!/usr/bin/env python
#  
from __future__ import print_function
import aerospike
from aerospike.exception import *
import sys
import time
class Program(object):
    client=None 
    start_time = time.time()
    duration = time.time() - start_time

    def __init__(self):
        #  Establish a connection to Aerospike cluster
        host1 = "127.0.0.1"  
        host2 = "127.0.0.1"
        port = 3000 
        #User AWS instance IP
        host1 = "54.172.xx.xx"  
        host2 = "55.xx.yy.zz" 
        config = {'hosts': [(host1,port), (host2,port)] }
        
        try:
            self.start_time = time.time()
            self.client = aerospike.client(config).connect()
            self.duration = time.time()-self.start_time
        except ClientError as e:
            print("ERROR: Connection to Aerospike cluster failed!")
            print("Please check the server settings and try again!")
            print("Error: {0} [{1}]".format(e.msg, e.code))
            sys.exit(1)

    @classmethod
    def main(cls, args):
        aero=Program()
        aero.work()


    def work(self):
        
        if self.client:
              print("\nINFO: Connection to Aerospike opened in %s seconds.\n"%(self.duration))
              self.start_time = time.time()
              self.client.close()
              self.duration = time.time()-self.start_time
              print("\nINFO: Connection to Aerospike cluster closed in %s seconds\n"%(self.duration))

if __name__ == '__main__':
    import sys
    Program.main(sys.argv)

