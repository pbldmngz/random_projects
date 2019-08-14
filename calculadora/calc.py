import re
op = ["/", "*", "+"] 
r_string = ""
def parenthesis_slayer(): 
    global r_string
    end = r_string.find(")") 
    cont = r_string[0:end]
    init = cont.rfind("(") + 1 
    cont = cont[init:]
    cont = calc_mod(cont)
    r_string = r_string[0:init-1] + str(cont) + r_string[end+1:]
    r_string = standarize(r_string)
    
def calc_mod(string):
    sym = []
    string = list(string)
    a_aux = 0
    
    control = False
    if string[0] == "-": control = True
    
    while a_aux < len(string):
        if "-" in string[a_aux]: 
            string.insert(a_aux, " ")
            a_aux += 1
        a_aux += 1

    for iy, i in enumerate(string): 
        if i in "*/+":
            sym.append(i)
        if i == "-":
            sym.append(" ")
            if iy > 0 and string[iy-2] in "*/":
                del sym[len(sym)-1]
    if string[0] == "+": 
        del string[0]
        del sym[0]
    string = "".join(string)
    string = re.split("[*/+ ]", "".join(string))

    if len(sym) == 0: return float("".join(string))
    if control: del sym[0]
    
    i_aux = 0
    while i_aux < len(string):
        if string[i_aux] == "": 
            del string[i_aux]
            i_aux -= 1
        i_aux += 1

    string = list(map(lambda x: float(x), string))

    #print("STRING: ", string)
    #print("SYM: ", sym)
    try:
        
        op = ["/", "*", "+"]
        if op[0] in sym:
            while op[0] in sym:
                string[sym.index(op[0])] = string[sym.index(op[0])] / string[sym.index(op[0])+1]
                del string[sym.index(op[0])+1]
                del sym[sym.index(op[0])]
        if op[1] in sym:
            while op[1] in sym:
                string[sym.index(op[1])] = string[sym.index(op[1])] * string[sym.index(op[1])+1]
                del string[sym.index(op[1])+1]
                del sym[sym.index(op[1])]
        if op[2] in sym:
            while op[2] in sym:
                string[sym.index(op[2])] = string[sym.index(op[2])] + string[sym.index(op[2])+1]
                del string[sym.index(op[2])+1]
                del sym[sym.index(op[2])]
                    
    except: pass
    val = 0
    for v in string:
        val += v
    
    return val

def standarize(s):
    s = s.replace(' ', '')
    while "--" in s:
        s = s.replace('--', '+')
    while "++" in s:
        s = s.replace('++', '+')
    while "+-" in s:
        s = s.replace('+-', '-')
    while "/+" in s:
        s = s.replace('/+', '/')
    while "*+" in s:
        s = s.replace('*+', '*')
    return s

def calc(s):
    global r_string
    r_string = standarize(s)
    clear = False if "(" in r_string else True
    while not clear:
        parenthesis_slayer()
        if not "(" in r_string: clear = True
    return calc_mod(r_string)