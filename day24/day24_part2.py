def parse_input():
    inputs = {}
    eq = {}
    ands = {}
    ors_extended = {}
    xors = {}
    ands_extended = {}
    with open("input.txt", "r") as f:
        x, y = f.read().split("\n\n")
        x = x.split("\n")
        for e in x:
            x1 = e.split(": ")
            inputs[x1[0]] = int(x1[1])
        y = y.split("\n")
        for e in y:
            left, right = e.split(" -> ")
            x1, op, x2 = tuple(left.split(" "))
            eq[right] = {op: (x1, x2)}
            if (x1.startswith("x") and x2.startswith("y")) or x1.startswith("y") and x2.startswith("x"):
                if op == "XOR":
                    xors[int(x1[1:])] = right
                elif op == "AND":
                    ands[int(x1[1:])] = right
            else:
                if op == "AND":
                    ands_extended[tuple(sorted((x1, x2)))] = right
                elif op == "OR":
                    ors_extended[tuple(sorted((x1, x2)))] = right
                
                    
    xors = dict(sorted(xors.items(), key=lambda item: item[0], reverse=False))
    ands = dict(sorted(ands.items(), key=lambda item: item[0], reverse=False))
    return inputs, eq, ands, xors, ands_extended, ors_extended

def op(operator, x, y):
    if operator == "XOR":
        return x^y
    elif operator == "AND":
        return x and y
    elif operator == "OR":
        return x or y

def apply_op(eq, inputs, target):
    r = eq[target]

    operator, x, y = list(r.keys())[0], list(r.values())[0][0], list(r.values())[0][1]
    if (x.startswith("x") or x.startswith("y")) and (y.startswith("x") or y.startswith("y")):
        #trace.append([target, operator, x, y])
        x = inputs[x]
        y = inputs[y]
        
    elif (x.startswith("x") or x.startswith("y")):
        x = inputs[x]
        y, _ = apply_op(eq, inputs, y)
    elif (y.startswith("x") or y.startswith("y")):
        y = inputs[y]
        x, _ = apply_op(eq, inputs, x)
    else:
        x, _ = apply_op(eq, inputs, x)
        y, _ = apply_op(eq, inputs, y)
    return op(operator, x, y), trace

inputs, eqs, ands, xors, ands_extended, ors_extended = parse_input()
xors = dict(sorted(xors.items(), key=lambda item: item[0], reverse=False))


calculated_final = {}
for k,v in xors.items():
    if k == 0:
        continue
    if k-1 in calculated_final.keys():
        bfd_and_mrk =tuple(calculated_final[k-1])
    else:
        z = list(eqs["z" + str(k-1).zfill(2)].values())[0]
        bfd_and_mrk = tuple(sorted((z[0], z[1])))
    try:
        hwt = ands_extended[bfd_and_mrk]
    except:
        print("***", k, v, bfd_and_mrk)
        continue
    sfw = ands[k-1]
    try:
        qkc = ors_extended[tuple(sorted((sfw, hwt)))]
    except:
        print("***", k, sfw, v)
        continue
    calculated = sorted((v, qkc))
    calculated_final[k] = calculated
    reality = sorted(list(eqs["z"+str(k).zfill(2)].values())[0])
    if calculated!=reality:
        print("*** problems at: ", k)
        print(calculated, reality)
    else:
        print(calculated, reality)

# observe the output:
#['bfd', 'mrk'] ['bfd', 'mrk']
#['nmb', 'qkc'] ['nmb', 'qkc']
#['cwr', 'www'] ['cwr', 'www']
#['hrk', 'sck'] ['hrk', 'sck']
#['bfg', 'hht'] ['bfg', 'hht']
#['scb', 'wkm'] ['scb', 'wkm']
#['fmv', 'sdc'] ['fmv', 'sdc']
#['qhr', 'rhc'] ['qhr', 'rhc']
#['fvg', 'trw'] ['fvg', 'trw']
#*** problems at:  11
#['gjc', 'jdm'] ['jdm', 'qjj']
#*** 12 dnj ('gjc', 'jdm')
#['mmk', 'mrw'] ['mmk', 'mrw']
#['gvp', 'jdk'] ['gvp', 'jdk']
#['jgs', 'ptj'] ['jgs', 'ptj']
#['nsf', 'vwv'] ['nsf', 'vwv']
#*** problems at:  17
#['pvh', 'rqq'] ['ffg', 'pqv']
#*** problems at:  18
#['vfq', 'z17'] ['vfq', 'wmp']
#*** 19 mpm ('vfq', 'z17')
#['drq', 'wrs'] ['drq', 'wrs']
#['hmg', 'vws'] ['hmg', 'vws']
#['gss', 'vrw'] ['gss', 'vrw']
#['gdw', 'wtc'] ['gdw', 'wtc']
#['jhj', 'psq'] ['jhj', 'psq']
#['knj', 'nvk'] ['knj', 'nvk']
#['kfq', 'qgs'] ['kfq', 'qgs']
#*** 27 vfk nrn
#['cpd', 'hvw'] ['cpd', 'hvw']
#['pjv', 'swr'] ['pjv', 'swr']
#['dgk', 'jgk'] ['dgk', 'jgk']
#['htv', 'nrj'] ['htv', 'nrj']
#['jrp', 'ncd'] ['jrp', 'ncd']
#['dqg', 'fsq'] ['dqg', 'fsq']
#['nhv', 'ptb'] ['nhv', 'ptb']
#['cpb', 'wnv'] ['cpb', 'wnv']
#['bgv', 'vcq'] ['bgv', 'vcq']
#['knp', 'pbm'] ['knp', 'pbm']
#['cwp', 'rjs'] ['cwp', 'rjs']
#*** problems at:  39
#['hkg', 'sbq'] ['x39', 'y39']
#*** 40 z39 wsw
#['gfc', 'wdd'] ['gfc', 'wdd']
#['ntc', 'wkt'] ['ntc', 'wkt']
#['ggm', 'tnh'] ['ggm', 'tnh']
#['ctm', 'dmn'] ['ctm', 'dmn']
        
# "qsb" <->"z39", "gvm" <->"z26", "wmp" <-> "z17", "qjj" <-> "gjc"
# swap those and rerun the script the problems will go away
result2 = ["qsb","z39", "gvm", "z26", "wmp", "z17", "qjj", "gjc"]
result2 = ",".join(sorted(result2))
print(result2)
    

