/*******************************************************************************
 * Copyright 2008-2016 by Aerospike.
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


//==========================================================
// Includes
//

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>

#include <aerospike/aerospike.h>
#include <aerospike/aerospike_key.h>
#include <aerospike/as_error.h>
#include <aerospike/as_record.h>
#include <aerospike/as_status.h>

//#include "example_utils.h"


//==========================================================
// PUT Example
//

int
main(int argc, char* argv[])
{

	as_error err;
	as_config config;
	as_config_init(&config);

  //Add you AWS node IP addresses below
  //as_config_add_host(&config, "127.0.0.1", 3000);
	as_config_add_host(&config, "54.x1.y1.z1", 3000);
	//comment line below for single node test
	as_config_add_host(&config, "54.x2.y2.z2", 3000);

	aerospike as;
	aerospike_init(&as, &config);
  clock_t start_time = clock();
	clock_t end_time = clock();

	if (aerospike_connect(&as, &err) != AEROSPIKE_OK) {
	    fprintf(stderr, "error(%d) %s at [%s:%d]", err.code, err.message, err.file, err.line);
	}
	else{
		end_time = clock();
		printf("Successfully Connected to Aerospike in %f seconds!\n", (double)(end_time - start_time) / CLOCKS_PER_SEC );
	}

	as_key key;
	as_key_init(&key, "test", "demo", "testKey2");

	as_record rec;
	as_record_inita(&rec, 2);
	as_record_set_int64(&rec, "test-bin-1", 1234);
	as_record_set_str(&rec, "test-bin-2", "test-bin-2-data");

	aerospike_key_put(&as, &err, NULL, &key, &rec);

	start_time = clock();
	if (aerospike_close(&as, &err) != AEROSPIKE_OK) {
	    fprintf(stderr, "error(%d) %s at [%s:%d]", err.code, err.message, err.file, err.line);
	}
	else{
		end_time = clock();
		printf("Closed connection to Aerospike in %f seconds!\n", (double)(end_time - start_time) / CLOCKS_PER_SEC );
	}
	aerospike_destroy(&as);
	return 0;
}
