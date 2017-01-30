
local function rec_to_map(rec)
   local xrec = map()
   for i, bin_name in ipairs(record.bin_names(rec)) do
       xrec[bin_name] = rec[bin_name]
   end
   return xrec
end

function str_equal(stream, key, email)
   local function email_filter(rec)
      local val = rec[key]
      if type(val) ~= 'string' then
         return false
      end
      if val == email then
         return true
      else
         return false
      end
   end
   return stream:filter(email_filter):map(rec_to_map)
end
