local utf8 = require('utf8')

-- fix string.sub for non ascii char, from http://lua-users.org/lists/lua-l/2014-04/msg00590.html
function utf8.sub(s,i,j)
   i = i or 1
   j = j or -1
   if i<1 or j<1 then
      local n = utf8.len(s)
      if not n then return nil end
      if i<0 then i = n+1+i end
      if j<0 then j = n+1+j end
      if i<0 then i = 1 elseif i>n then i = n end
      if j<0 then j = 1 elseif j>n then j = n end
   end
   if j<i then return "" end
   i = utf8.offset(s,i)
   j = utf8.offset(s,j+1)
   if i and j then return s:sub(i,j-1)
      elseif i then return s:sub(i)
      else return ""
   end
end

local MAX_WHILE_ITERATION = -100

local vowelList = {
                      ["a"] = true,
                      ["e"] = true,
                      ["é"] = true,
                      ["ë"] = true,
                      ["i"] = true,
                      ["o"] = true,
                      ["ò"] = true,
                      ["u"] = true,
                      ["ü"] = true,
                      ["ā"] = true,
                      ["ō"] = true,
                      ["ū"] = true,

                      ["A"] = true,
                      ["E"] = true,
                      ["É"] = true,
                      ["Ë"] = true,
                      ["I"] = true,
                      ["O"] = true,
                      ["Ò"] = true,
                      ["U"] = true,
                      ["Ü"] = true,
                      ["Ā"] = true,
                      ["Ō"] = true,
                      ["Ū"] = true
                  }
local vowelGet = {
                    ["a"] = "a",
                    ["e"] = "e",
                    ["é"] = "e",
                    ["ë"] = "e",
                    ["i"] = "e",
                    ["o"] = "u",
                    ["ò"] = "u",
                    ["u"] = "u",
                    ["ü"] = "u",
                    ["ā"] = "a",
                    ["ō"] = "u",
                    ["ū"] = "u",
                
                    ["A"] = "a",
                    ["E"] = "e",
                    ["É"] = "e",
                    ["Ë"] = "e",
                    ["I"] = "e",
                    ["O"] = "u",
                    ["Ò"] = "u",
                    ["U"] = "u",
                    ["Ü"] = "u",
                    ["Ā"] = "a",
                    ["Ō"] = "u",
                    ["Ū"] = "u"
                }

function isVowel(vowel) return vowelList[vowel] end
function getVowel(vowel) return vowelGet[vowel] end

function main(nominative_singular)
    local accusative_singular = ""
    local accusative_plural = ""

    if isVowel(utf8.sub(nominative_singular, -1, -1)) then
        accusative_singular = nominative_singular .. "m"
        accusative_plural = nominative_singular .. "s"
    else
        local i = -2
        while not isVowel(utf8.sub(nominative_singular, i, i)) and i > MAX_WHILE_ITERATION do
            i = i - 1
            if i <= MAX_WHILE_ITERATION then
                print("Error: While loop failed for " .. nominative_singular)
            end
        end
        if i == MAX_WHILE_ITERATION then
            accusative_singular = "error"
            accusative_plural = "error"
        else
            accusative_singular = nominative_singular .. getVowel(utf8.sub(nominative_singular,i,i)) .. "m"
            accusative_plural = nominative_singular .. getVowel(utf8.sub(nominative_singular,i,i)) .. "s"
        end
    end


    return  accusative_singular .. " " ..  accusative_plural
    end