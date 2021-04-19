import flask


#Algebra Generator

#Type 1 equation: ax+b = cx+d
#Type 2 equation: (ax+b)/(cx+d) + e = f
#Type 3: ax+b = N(cx+d) only used in displaying solution.

#Probabilities:
#pt is the probability of type 1, otherwise type 2
#pc is the probability that constants will exist
#pl for a and c1 is the probability that a and c will be 1.
#pl for c0 is the probability that c will be zero.
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
        return(((equ[5]-equ[4])*equ[3]-equ[2])/(equ[0]-(equ[3]-equ[2])*equ[1])) 


#Server stuff
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

app.run()
