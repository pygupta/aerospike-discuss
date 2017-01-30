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
using System.IO;

namespace AerospikeDiscuss
{
    class TopicTest
    {
        private AerospikeClient client;

        public TopicTest(AerospikeClient c)
        {
            this.client = c;
        }

        public void addRecords()
        {
            Console.WriteLine("\n********** Create Records **********\n");
            WritePolicy wPolicy = new WritePolicy();
            wPolicy.recordExistsAction = RecordExistsAction.UPDATE;
            for (int i = 0; i < 100; i++)
            {
                string myKey = "key" + i;
                Key key = new Key("test", "demo", myKey);
                Bin bin1 = new Bin(string.Empty, 0);                
                client.Put(wPolicy, key, bin1);
            }
        }
        public void updateRecords()
        {
            Console.WriteLine("\n********** Updating counter **********\n");
            WritePolicy wPolicy = new WritePolicy();
            wPolicy.recordExistsAction = RecordExistsAction.UPDATE;
            wPolicy.expiration = 1296000;
            for (int i = 0; i < 100; i++)
            {
                string myKey = "key" + i;
                Key key = new Key("test", "demo", myKey);
                Bin bin1 = new Bin(string.Empty, 1);
                client.Add(wPolicy, key, bin1);
            }
        }  
    }        
}
