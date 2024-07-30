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
    local nominative_plural = ""

    if isVowel(string.sub(nominative_singular, -1, -1)) then
        accusative_singular = nominative_singular .. "m"
        accusative_plural = nominative_singular .. "s"
        nominative_plural = nominative_singular
    else
        local i = -2
        while not isVowel(string.sub(nominative_singular, i, i)) and i > MAX_WHILE_ITERATION do
            i = i - 1
            if i <= MAX_WHILE_ITERATION then
                print("Error: While loop failed")
            end
        end
        if i == MAX_WHILE_ITERATION then
            accusative_singular = "error"
            accusative_plural = "error"
            nominative_plural = "error"
        else
            accusative_singular = nominative_singular .. getVowel(string.sub(nominative_singular,i,i)) .. "m"
            accusative_plural = nominative_singular .. getVowel(string.sub(nominative_singular,i,i)) .. "s"
            nominative_plural = nominative_singular
        end
    end


    print(nominative_singular .. " " .. accusative_singular .. " " .. nominative_plural .. " " .. accusative_plural)
    end