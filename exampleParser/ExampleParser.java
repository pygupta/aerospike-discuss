package com.aerospike.parser;

import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

import javax.jms.JMSRuntimeException;
import javax.jms.Message;
import javax.jms.TextMessage;

import org.yaml.snakeyaml.Yaml;

import com.aerospike.jms.inbound.JmsMessageFormat;
import com.aerospike.jms.inbound.parser.FieldEntries;
import com.aerospike.jms.inbound.parser.JmsMessageParser;
import com.aerospike.jms.inbound.parser.MessageParsingException;

import kotlin.collections.CollectionsKt;

@JmsMessageFormat(name = "example")
public class ExampleParser implements JmsMessageParser {
	
	public static final String KEY_NAME = "keyDef";
	private class StringPart {
		int offset;
		int length;
		
		public StringPart(int offset, int length) {
			this.offset = offset;
			this.length = length;
		}
	}
	
	private final StringPart[] parts;
	
	public ExampleParser() {
		Yaml yaml = new Yaml();
		InputStream inputStream = this.getClass()
				.getClassLoader()
				.getResourceAsStream("config.yml");
		Map<String, Object> obj = yaml.load(inputStream);
		System.out.println(obj);
		
		// if there is a keyDef, use it as a pair of values
		Object value = obj.get(KEY_NAME);
		if (value instanceof String) {
			String fieldStr = ((String)value).trim();
			if (fieldStr.startsWith("(") && fieldStr.endsWith(")")) {
				fieldStr = fieldStr.substring(1, fieldStr.length() - 1);
			}
			String[] fieldLenPairs = fieldStr.split(",");
			if (fieldLenPairs.length % 2 != 0) {
				throw new IllegalArgumentException("Configuration file is invalid, keyDef must contain an even number of integers");
			}
			
			parts = new StringPart[fieldLenPairs.length / 2];
			for (int i = 0; i < fieldLenPairs.length; i+=2) {
				// Have to translate from 0 offset to 1 offset
				int offset = Integer.parseInt(fieldLenPairs[i])-1;
				int length = Integer.parseInt(fieldLenPairs[i+1]);
				parts[i/2] = new StringPart(offset, length);
			}
		}
		else {
			// TODO: Any other ways of parsing the data?
			throw new IllegalArgumentException("Configuration file must include a keyDef");
		}
	}
	
    @Override
    public FieldEntries parse(Message message) {
    		try {
	        if (!(message instanceof TextMessage)) {
	            throw new MessageParsingException("jms message should be of type TextMessage, not " + message.getClass().getSimpleName());
	        }
	        
	        String text = ((TextMessage)message).getText();
	        
	        StringBuffer buffer = new StringBuffer(128);
	        for (StringPart part : parts) {
	        		buffer.append(text.substring(part.offset, part.offset + part.length));
	        }
	        // Create a map
	        Map<String, String> map = new HashMap<String, String>();
	        map.put("key", buffer.toString());
	        
	        FieldEntries fieldEntries = new FieldEntries(CollectionsKt.asSequence(map.entrySet()));
	        return fieldEntries;
    		}
    		catch (Exception jmsE) {
    			if (jmsE instanceof RuntimeException) {
    				throw ((RuntimeException)jmsE);
    			}
    			else {
    				throw new JMSRuntimeException(jmsE.getMessage(), jmsE.getClass().getSimpleName(), jmsE);
    			}
    		}
    }
}
