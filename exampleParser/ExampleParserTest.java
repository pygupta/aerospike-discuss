package com.aerospike.parser;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;
import java.util.function.Consumer;

import javax.jms.Message;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.aerospike.jms.inbound.parser.FieldEntries;

class ExampleParserTest {

	private ExampleParser exampleParser;
	@BeforeEach
	void setUp() throws Exception {
		exampleParser = new ExampleParser();
	}

	@AfterEach
	void tearDown() throws Exception {
	}

	@Test
	void test() {
		// YAML file defines (2,2,4,1,10,5)
		String messageStr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
		Message message = new MockTextMessage(messageStr);
		FieldEntries fields = exampleParser.parse(message);
		
		assertNotNull(fields);
		Iterator<Entry<String, Object>> it = fields.iterator();
		int count = 0;
		while (it.hasNext()) {
			Entry<String, Object> pair = it.next();
			assertEquals("There should only be one item in the result set", 1, ++count);
			assertEquals("key", pair.getKey());
			assertEquals("bcdjklmn", pair.getValue());
		}
	}
}
