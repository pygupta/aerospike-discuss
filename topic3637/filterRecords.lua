local function rec_to_map(rec)
   local xrec = map()
   for i, bin_name in ipairs(record.bin_names(rec)) do
       xrec[bin_name] = rec[bin_name]
   end
   return xrec
end

function check_visibility(stream, vis, linktype, id, mintime, maxtime)
   local function range_filter(rec)
      local val = rec['time']
      if val >= mintime and val <= maxtime then
         return true
      else
         return false
      end
   end
   local function idcheck(rec)
      local val = rec['id']
      if val == id then
         return true
      else
         return false
      end
   end
   local function linktypecheck(rec)
      local val = rec['link_type']
      if val == linktype then
         return true
      else
         return false
      end
   end
   local function vischeck(rec)
      local val = rec['visibility']
      if val == vis then
         return true
      else
         return false
      end
   end

   return stream:filter(range_filter):filter(idcheck):filter(linktypecheck):filter(vischeck):map(rec_to_map)
end
