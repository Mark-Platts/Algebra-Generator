import flask
import random
import json





#Algebra stuff
'''
Type 1 equation: ax+b = cx+d
Type 2 equation: (ax+b)/(cx+d) + e = f
Type 3: ax+b = N(cx+d) only used in displaying solution.

Probabilities:
pt is the probability of type 1, otherwise type 2
pc is the probability that constants will exist
pl for a and c1 is the probability that a and c will be 1.
pl for c0 is the probability that c will be zero.
'''

pt = 1

pc = [0.5,0.5,0.5,0.5]

pl = [0.5,0.5,0.5,0.5]

equ_type = 2

ptl = [1,1,0.5,0.5,0]

pcl = [[0.2,0.5,0,0],
       [0.2,0.2,0,0],
       [0.5,1,0,0.5],
       [0.5,0.5,0.5,0.5],
       [1,1,1,1]]

pll = [[0,0.5,1,0],
       [0,0.1,0.2,0.5],
       [0.5,0.5,1,0],
       [0.5,0.5,0.5,0.5],
       [0.2,0.2,0.2,0.2]]

eql = [1,1,0.5,0.3,0]

#generate a number between -b and -a or a and b,
def randint_nz(a,b):
    t = random.randint(a,b)
    if random.random() >= 0.5:
        return(t)
    else:
        return(-t)

#generates a set of values to build equation with
#form: f = [a,c,b,d,e,f]
def generate_values(equ_type,pt,pc,pl):
    f = []
    if equ_type == 1:
        if random.random() < pl[1]:
            f.append(1) #set a = 1
        else:
            f.append(randint_nz(1,5))
        if random.random() < pl[2]: #set c = 0
            f.append(0)
        elif random.random() < pl[3] and f[0] != 1: #set c = 1
            f.append(1)
        else: #set c = random value that isn't equal to a
            T = 1
            while T == 1:
                t = random.randint(-5,5)
                if t != f[0]:
                    f.append(t)
                    T = 0
        for i in pc: #for constants test if 0 or set to random times (a-c)
            if random.random() < i:
                f.append((f[0]-f[1])*randint_nz(1,10))
            else:
                f.append(0)
        if f[0] == 1 and f[2] == 0:
            f[2] = (f[0]-f[1])*randint_nz(1,10)
    if equ_type == 2:
        if random.random() < pl[2]:
            c = 0 #set c = 0
        elif random.random() < pl[3]:
            c = 1 #set c = 1
        else:
            c = randint_nz(2,6)
        if random.random() < pc[3]:
            fc = random.randint(-10,10)
        else:
            fc = 0
        if random.random() < pc[2]:
            e = random.randint(-10,10)
        else:
            e = 0
        if fc - e == 0:
            if random.random() < pl[1]: #set a = 1
                f.append(1)
            else: #set a = random value
                f.append(randint_nz(2,6))
            f.append(c)
            if random.random() < pc[0] or f[0] == 0:
                f.append(f[0]*randint_nz(1,10))
            else:
                f.append(0)
            if random.random() < pc[1] or c == 0:
                f.append(randint_nz(1,10))
            else:
                f.append(0)
            f.append(e)
            f.append(fc)
        else:
            if c == 0:
                if random.random() < pl[1]: #set a = 1
                    f.append(1)
                else: #set a = random value
                    f.append(randint_nz(1,5))
                f.append(c)
                if random.random() < pc[0] or f[0] == 0:
                    f.append(f[0]*randint_nz(1,10))
                else:
                    f.append(0)
                if random.random() < pc[1] or c == 0:
                    f.append(f[0]*randint_nz(1,10))
                else:
                    f.append(0)
                f.append(e)
                f.append(fc)
            else:
                if random.random() < pl[0]: #set a = 0
                    f.append(0)
                elif random.random() < pl[1]: #set a = 1
                    f.append(1)
                else: #set a = random value that doesn't delete the denominator
                    T = 1
                    while T == 1:
                        t = random.randint(-5,5)
                        test = t - (fc - e)*c
                        if test != 0:
                            f.append(t)
                            T = 0
                f.append(c)
                if random.random() < pc[0] or f[0] == 0:
                    f.append((f[0] - (fc - e)*c)*randint_nz(1,10))
                else:
                    f.append(0)
                if random.random() < pc[1] or c == 0:
                    f.append((f[0] - (fc - e)*c)*randint_nz(1,10))
                else:
                    f.append(0)
                f.append(e)
                f.append(fc)
    return(f)

def get_equ_ans(equ, equ_type):
    if equ_type == 1:
        return((equ[3]-equ[2])/(equ[0]-equ[1]))
    if equ_type == 2:
        return(((equ[5]-equ[4])*equ[3]-equ[2])/(equ[0]-(equ[3]-equ[2])*equ[1])) #come back to!!!

def disp_equ(equ,equ_type):
    if equ_type == 1 or equ_type == 3:
        f = ""
        if equ[0] == 1:
            f += "x"
        elif equ[0] == -1:
            f += "-x"
        elif equ[0] != 0:
            f += str(equ[0])+"x"
        if equ[2] == 0:
            f += " = "
        elif equ[2] > 0 and equ[0] != 0:
            f += " + "+str(equ[2])+" = "
        elif equ[2] < 0 and equ[0] != 0:
            f += " - "+str(-equ[2])+" = "
        elif equ[2] > 0 and equ[0] == 0:
            f += str(equ[2])+" = "
        elif equ[2] < 0 and equ[0] == 0:
            f += "-"+str(-equ[2])+" = "
        if equ_type == 3:
            f += str(equ[5])+"("
        if equ[1] == 1:
            f += "x"
        elif equ[1] == -1:
            f += "-x"
        elif equ[1] != 1 and equ[1] != 0:
            f += str(equ[1])+"x"
        if equ[1] != 0 and equ[3] > 0:
            f += " + "+str(equ[3])
        elif equ[1] != 0 and equ[3] < 0:
            f += " - "+str(-equ[3])
        elif equ[3] > 0 and equ[1] == 0:
            f += str(equ[3])
        elif equ[3] < 0 and equ[1] == 0:
            f += "-"+str(-equ[3])
        elif equ[3] == 0 and equ[1] == 0:
            f += "0"
        if equ_type == 3:
            f += ")"
        return(f)
    if equ_type == 2:
        num = ""
        if equ[0] == 1:
            num += "x"
        elif equ[0] == -1:
            num += "-x"
        elif equ[0] != 1 and equ[0] != 0:
            num += str(equ[0])+"x"
        if equ[0] != 0 and equ[2] > 0:
            num += " + "+str(equ[2])
        elif equ[0] != 0 and equ[2] < 0:
            num += " - "+str(-equ[2])
        elif equ[2] > 0 and equ[0] == 0:
            num += str(equ[2])
        elif equ[2] < 0 and equ[0] == 0:
            num += "-"+str(-equ[2])
        elif equ[2] == 0 and equ[0] == 0:
            num += "0"
        den = ""
        if equ[1] == 1:
            den += "x"
        elif equ[1] == -1:
            den += "-x"
        elif equ[1] != 1 and equ[1] != 0:
            den += str(equ[1])+"x"
        if equ[3] != 0 and equ[1] != 0 and equ[3] > 0:
            den += " + "+str(equ[3])
        elif equ[3] != 0 and equ[1] != 0 and equ[3] < 0:
            den += " - "+str(-equ[3])
        elif equ[3] > 0 and equ[1] == 0:
            den += str(equ[3])
        elif equ[3] < 0 and equ[1] == 0:
            den += "-"+str(-equ[3])
        elif equ[3] == 0 and equ[1] == 0:
            den += "0"
        fraclen = 0
        if len(num) >= len(den):
            fraclen = len(num)+2
        else:
            fraclen = len(den)+2
        nummar = int((fraclen - len(num))/2)
        denmar = int((fraclen - len(den))/2)
        f = ""
        f += nummar*" " + num + nummar*" " + "\n"
        f += fraclen*"\u2500"
        if equ[4] > 0:
            f += " + "+str(equ[4])
        elif equ[4] < 0:
            f += " - "+str(-equ[4])
        f += " = "+str(equ[5])+"\n"
        f += denmar*" " + den + denmar*" "
        return(f)
        

def arr_int(f):
    for i in range(len(f)):
        f[i] = int(f[i])
    return(f)

def show_sol_1(equ):
    tequ = []
    for i in range(len(equ)):
        tequ.append(equ[i])
    f = ""
    f += disp_equ(tequ,1)+"\n\n"
    if tequ[2] != 0:
        f += "Take "+str(tequ[2])+" to the right hand side.\n"
        tequ[3] -= tequ[2]
        tequ[2] = 0
        arr_int(tequ)
        f += disp_equ(tequ,1)+"\n\n"
    if tequ[1] != 0:
        f += "Take "+str(tequ[1])+"x to the left hand side.\n"
        tequ[0] -= tequ[1]
        tequ[1] = 0
        arr_int(tequ)
        f += disp_equ(tequ,1)+"\n\n"
    if tequ[0] != 1:
        f += "Divide by "+str(tequ[0])+".\n"
        tequ[3] /= tequ[0]
        tequ[0] = 1
        arr_int(tequ)
        f += disp_equ(tequ,1)+"\n\n"
    f += "Done!"
    return(f)

def show_sol_2(equ):
    tequ = []
    for i in range(len(equ)):
        tequ.append(equ[i])
    f = ""
    f += disp_equ(tequ,2)+"\n\n"
    if tequ[4] != 0:
        f += "Take "+str(tequ[4])+" to the right hand side.\n"
        tequ[5] -= tequ[4]
        tequ[4] = 0
        arr_int(tequ)
        f += disp_equ(tequ,2)+"\n\n"
    f += "Multiply both sides by the denominator.\n"
    f += disp_equ(tequ,3)+"\n\n"
    f += "Multiply out the brackets. \n"
    tequ[1] *= tequ[5]
    tequ[3] *= tequ[5]
    if tequ[0] == 0:
        f += disp_equ(tequ,1)+"\n\n"
        f += "Switch the sides. \n"
        b = tequ[2]
        c = tequ[1]
        d = tequ[3]
        tequ[0] = c
        tequ[1] = 0
        tequ[2] = d
        tequ[3] = b
    f += show_sol_1(tequ)
    return(f)

#Takes level and returns an object with all equ info in
def generateEquationSet(level):
    equationSet = {}
    level -= 1
    pt = ptl[level]
    pc = pcl[level]
    pl = pll[level]
    pequ = eql[level]
    if random.random() < pequ:
        equ_type = 1
    else:
        equ_type = 2
    equ = []
    ans = 0
    while True:
        equ = generate_values(equ_type,pt,pc,pl)
        ans = str(int(get_equ_ans(equ,equ_type)))
        if ans != '0':
            break
    equationSet['values'] = equ
    equationSet['answer'] = ans
    if equ_type == 1:
        equationSet['solution'] = show_sol_1(equ)
    else:
        equationSet['solution'] = show_sol_2(equ)
    final = json.dumps(equationSet)
    return final

#Server stuff
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/<int:level>', methods=['GET'])
def home(level):
    return generateEquationSet(level)

app.run()
    
