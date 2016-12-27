/*******************************************************************************
 * Copyright 2012-2014 by Aerospike.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 * IN THE SOFTWARE.
 ******************************************************************************/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Aerospike.Client;

namespace AerospikeDiscuss
{
    class Program
    {

        static void Main(string[] args)
        {
            
            AerospikeClient client = null;
            try
            {
                Console.WriteLine("INFO: Connecting to Aerospike cluster...");

                // Connecting to Aerospike cluster

                // Specify IP of one of the nodes in the cluster
                // Note: Assign your AWS Instance Public IP address to asServerIP
                string asServerIP = "54.236.253.20";
                // Specity Port that the node is listening on
                int asServerPort = 3000;
                // Establish connection
                
                client = new AerospikeClient(asServerIP, asServerPort);

                // Check to see if the cluster connection succeeded
                
                if (client!= null && client.Connected)
                {
                    Console.WriteLine("INFO: Connection to Aerospike cluster succeeded!\n");

                    // Create instance of TopicTest
                    TopicTest tt = new TopicTest(client);
                   
                    // Present options
                    Console.WriteLine("What would you like to do:");
                    Console.WriteLine("1> Add test records.");
                    Console.WriteLine("2> Increment counter - Update test records.");
                    Console.WriteLine("0> Exit");
                    Console.Write("\nSelect 0-2 and hit enter:");
                    byte feature = byte.Parse(Console.ReadLine());

                    if (feature != 0)
                    {
                        switch (feature)
                        {
                            case 1:
                                Console.WriteLine("\n********** Your Selection: Add records **********\n");
                                tt.addRecords();                                
                                break;
                            case 2:
                                Console.WriteLine("\n********** Your Selection: Increment counter - Update test records. **********\n");
                                tt.updateRecords();
                                break;                            
                            default:
                                Console.WriteLine("\n********** Invalid Selection **********\n");
                                break;
                        }
                    }
                }
                else
                {
                    Console.Write("ERROR: Connection to Aerospike cluster failed! Please check IP & Port settings and try again!");
                    Console.ReadLine();
                }
            }
            catch (AerospikeException e)
            {
                Console.WriteLine("AerospikeException - Message: " + e.Message);
                Console.WriteLine("AerospikeException - StackTrace: " + e.StackTrace);
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception - Message: " + e.Message);
                Console.WriteLine("Exception - StackTrace: " + e.StackTrace);
            }
            finally
            {
                if (client != null && client.Connected)
                {
                    // Close Aerospike server connection
                   
                    client.Close();
                }
                Console.Write("\n\nINFO: Press any key to exit...");
                Console.ReadLine();
            }
            
        } //main

    }
}
