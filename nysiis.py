from typing import List, Callable
import string

# vowel array defined outside of function as not to recreate when used in loops
__vowels : List[str ]= ["A","E","I","O","U"]

# Python should have this functionality built in, replacing at an index
def __replaceAt(input : str, index : int, replace : str = "") -> str :
    return input[:index] + replace + input[(len(replace) or 1) + index:]


# NYSIIS implementation https://en.wikipedia.org/wiki/New_York_State_Identification_and_Intelligence_System
def nysiis (input : str) -> str | None:

    # fail fast if there isn't an input value to code (code defensively)
    if (input is None or not input) :
        return None
    
    # strip leading and trailing whitespace
    input = input.strip()

    # make input uppercase (wiki algorithm doen't mention this as first step)
    input = input.upper()

    # Step 1.
    if input.startswith("MAC") :
        input = "MCC" + input.removeprefix("MAC")
    elif input.startswith("KN") :
        input = "NN" + input.removeprefix("KN")
    elif input.startswith("K") :
        input = "C" + input.removeprefix("K")
    elif input.startswith("PH") :
        input = "FF" + input.removeprefix("PH")
    elif input.startswith("PF") :
        input = "FF" + input.removeprefix("PF")
    elif input.startswith("SCH") :
        input = "SSS" + input.removeprefix("SCH")

    # Step 2.
    if input.endswith("EE") :
        input = input.removesuffix("EE") + "Y"
    elif input.endswith("IE") :
        input = input.removesuffix("IE") + "Y"
    for item in ["DT","RT","RD","NT","ND"] :
        if input.endswith(item) :
            input = input.removesuffix(item) + "D"

    # Steps 3-4.
    idx : int = 1

    while idx < len(input) :
 
        # Step 5. (1)
        # only process letters, skip all other characters including spaces
        if input[idx] not in string.ascii_letters : 
            input = __replaceAt(input,idx)
            # keeps current index and restarts
            continue

        # Step 5. (2)
        if input[idx] in __vowels :
            if input[idx:idx+2] == "EV" :
                input = __replaceAt(input,idx,"EV")
            else :
                input = __replaceAt(input,idx,"A")

        # Step 5. (3)
        elif input[idx] == "Q" :
            input = __replaceAt(input,idx,"G")
        elif input[idx] == "Z" :
            input = __replaceAt(input,idx,"S")
        elif input[idx] == "M" :
            input = __replaceAt(input,idx,"N")

        # Step 5. (4)
        elif input[idx:idx+2] == "KN" :
            input = __replaceAt(input,idx,"N")
        elif input[idx] ==  "K" :
            input = __replaceAt(input,idx,"C")

        # Step 5. (5)
        elif input[idx:idx+2] == "PH" :
            input = __replaceAt(input,idx,"FF")

        # Step 5. (6)
        elif input[idx] == "H" and (input[idx - 1] not in __vowels or input[idx:idx+1] not in __vowels) :
            input = __replaceAt(input,idx,input[idx - 1])

        # Step 5. (7)
        elif input[idx] == "W" and input[idx - 1]  in __vowels :
            input = __replaceAt(input,idx,input[idx - 1])

        # Step 6.
        if input[idx] == input[idx - 1] :
            input = __replaceAt(input,idx,"")
            continue
            
        idx += 1

    # Step 7.
    if input.endswith("S") :
        input = input.removesuffix("S")
    
    # Step 8.
    if input.endswith("AY") :
        input = __replaceAt(input,idx,"AY") + "Y"

    # Step 9.
    if input.endswith("A") :
        input = input.removesuffix("A")

    return input[0:6]
