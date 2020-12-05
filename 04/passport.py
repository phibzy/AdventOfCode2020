#!/usr/bin/python3

"""
  @author      : Chris Phibbs
  @created     : Friday Dec 04, 2020 16:18:19 AEDT
  @file        : passport

"""

import re, sys

# cid is optional field, so don't bother checking for it
# Will make this a dict for constant lookup time
expectedFields = {"byr": 1, "iyr": 1, "eyr": 1, "hgt": 1, "hcl": 1, "ecl": 1, "pid": 1}

def strToInput(s):
    # Split input on empty lines
    inp = s.split("\n\n")  
    return inp

def inpCheck(inp):
    validCount = 0

    # For each set of data, split into key/value pairs
    # and check them 
    for i in inp:

        # Increment counter if we have all required fields
        validCount += checkPassport(i)

    return validCount

# Return 1 if valid, 0 if not
def checkPassport(passport):
        # Delete fields as we see them from checkFields
        # if there's 0 keys left in checkFields at the end
        # of iteration, then input has all required fields
        cFields = expectedFields.copy()

        # \S matches any character that isn't whitespace
        for k, v in re.findall(r"(\S*):(\S*)", passport):
            # Part 1 spec says no duplicates so this should be safe
            if k == "cid": continue

            # For possible whacky cases where there are
            # unexpected fields
            if k not in expectedFields: return False

            del cFields[k]

            # For pt. 2
            if not checkFields(k,v): return False

        # checkFields length will be 0 if passport has all required fields
        return len(cFields) == 0

def checkFields(k,v):
    # Want to find a groovy way to do this lol
    # checks = {"byr": byr, "iyr": iyr, "eyr": eyr, "hgt": hgt, "hcl": hcl, "ecl": ecl, "pid": pid}

    # return checks[k](v) 

    # Alternative hacky way
    return globals().get(k)(v)

######### FIELD CHECK FUNCTIONS ####################

def byr(v):
    # Has to be 4 digits
    if len(v) != 4: return False

    return 1920 <= int(v) <= 2002

def iyr(v):
    # Has to be 4 digits
    if len(v) != 4: return False

    return 2010 <= int(v) <= 2020

def eyr(v):
    # Has to be 4 digits
    if len(v) != 4: return False

    return 2020 <= int(v) <= 2030

def hgt(v):
    # Two groups, the number and the unit
    num, unit = v[:-2], v[-2:]

    if unit == "cm":
        return 150 <= int(num) <= 193

    elif unit == "in":
        return 59 <= int(num) <= 76
    
    # In case of any funny business
    else:
        return False

# If we have a match object then pattern exists
def hcl(v):
    return re.match(r"^#[0-9a-f]{6}$", v) is not None

def ecl(v):
    # set of valid eye colours
    validColours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    
    # If colour isn't in set, not valid
    return v in validColours

# Regex check for 9 digit number
def pid(v):
    return re.match(r"^[0-9]{9}$", v) is not None

######################################################
    
inp = list()

# stdin.read() will read in the whole of stdin as
# one string, including newlines etc.
rawInp = sys.stdin.read()

print(inpCheck(strToInput(rawInp)))

