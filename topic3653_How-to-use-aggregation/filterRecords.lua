
local function rec_to_map(rec)
   local xrec = map()
   for i, bin_name in ipairs(record.bin_names(rec)) do
       xrec[bin_name] = rec[bin_name]
   end
   return xrec
end

function str_between(stream, bin_name, substr_from, substr_to)
   local function range_filter(rec)
      local val = rec[bin_name]
      if type(val) == 'string' then
         return false
      end
      if val >= substr_from and val <= substr_to then
         return true
      else
         return false
      end
   end
   return stream:filter(range_filter):map(rec_to_map)
end
