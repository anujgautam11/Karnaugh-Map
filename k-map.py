  
#!/usr/local/bin/python3


# Quine McCluskey algorithm for minimizing logical expressions with K-map grouping 
# Author: Anuj Gautam

# from tkinter import *
import tkinter as tk


def minFunc(numVar, stringIn):
	num= int(numVar)
	x= stringIn
	"""
    This python function takes function of maximum of 4 variables
    as input and gives the corresponding minimized function(s)
    as the output (minimized using the K-Map methodology),
    considering the case of Don’t Care conditions.
	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.
	"""
	l= []
	i=0
	while(x[i]!='d'):
		if(x[i].isdigit()==True):                         # taking the values from the input, and storing it in a list
			if(x[i+1].isdigit()==False):
				l.append(x[i])
				i+=1
			else:
				l.append(x[i]+x[i+1])
				i+=2
		else:
			i+=1
		y=i
	ess=list(l)                                             #storing essential prime implicant in a seprate list for further use
	if(x[y+1]!='-'):
		while(x[y]!=')'):
			if(x[y].isdigit()==True):
				if(x[y+1].isdigit()==False):                #storing the dont care condition giving in the input
					l.append(x[y])
					y+=1
				else:
					l.append(x[y]+x[y+1])
					y+=2
			else:
				y+=1
	if(num==4):
		for i in range(len(l)):								#converting to binary for 4 variables
			l[i] = format(int(l[i]), '04b')
	elif(num==3):
		for i in range(len(l)):								#converting to binary for 3 variables
			l[i] = format(int(l[i]), '03b')
	elif(num==2):
		for i in range(len(l)):								#converting to binary for 2 variables
			l[i] = format(int(l[i]), '02b')

	a,b,c,d,e,f,g,h,p,q,w,r,t,y,m,n,o,z,u,v = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]  	#creating list to be stored
	l.sort()
	count = 0
	t=0

	#  Quine-McCluskey and Petrick methods - 

	for i in range(len(l)):
			for j in range(num):				#Storing the digit speratly on the basis of much many 1's they contain
				if(l[i][j]=='1'):
					count+=1
			if(count==0):
				a.append(l[i])
			if(count==1):						#appending into one of the list created above for seperation
				b.append(l[i])
			if(count==2):
				c.append(l[i])
			if(count==3):
				d.append(l[i])
			if(count==4):
				e.append(l[i])
			count=0

	def step1(a,b,f):  									# Proceding tp step 1 comparing a and b then follows on uptil all thrr couples are compared 
		count=0
		for i in range(len(a)):
			for k in range(len(b)): 					#loops
				for j in range(num):
					if(a[i][j]!=b[k][j]):
						count+=1
				if(count==1):
					for j in range(num):
						if(a[i][j]!=b[k][j]):
							f.append(str(str(a[i][:j])+'x'+str(a[i][j+1:])+',('+str(int(a[i],2))+','+str(int(b[k],2))+')')) 	#slicing and appending
				count=0
		return(f)

	f=step1(a,b,f)					#calling the function and storing what it returns
	g=step1(b,c,g)
	h=step1(c,d,h)
	p=step1(d,e,p)

	def step2(f,g,q):
		count=0
		for i in range(len(f)): 		#same as step 1 , step 2 does the same on the output of step 1 and give us a compariable impicants
			for k in range(len(g)):
				for j in range(num):
					if(f[i][j]!=g[k][j]):			#loops
						count+=1
				if(count==1):
					for j in range(num):
						if(f[i][j]!=g[k][j]):
							q.append(str(str(f[i][:j])+'x'+str(f[i][j+1:-1])+','+ str(g[k][num+2:])))   #slicing and appending
				count=0
		return(q)

	q = step2(f,g,q)                  #calling the function and storing what it returns
	w = step2(g,h,w)
	r = step2(h,p,r)

	def step3(f,g,q):
		count=0
		for i in range(len(f)):			#same as step 2 , step 3 does the same on the output of step 2 and give us a compariable impicants
			for k in range(len(g)):
				for j in range(num):
					if(f[i][j]!=g[k][j]):
						count+=1				#loops
				if(count==1):
					for j in range(num):
						if(f[i][j]!=g[k][j]):
							q.append(str(str(f[i][:j])+'x'+str(f[i][j+1:-1])+ ',' +str(g[k][6:]))) 				#slicing and appending
				count=0
		return(q)
	m = step3(q,w,m)			#calling the function and storing what it returns
	n = step3(w,r,n)

	def step4(f,g,p):
		count=0
		for i in range(len(f)):				#same as step 3 , step 4 does the same on the output of step 3 and give us a compariable impicants
			for k in range(len(g)):
				for j in range(num):
					if(f[i][j]=='x'):			#loops
						if(g[k][j]=='x'):
							count+=1
				if(count==2):
					for j in range(num):
						if(f[i][j]!=g[k][j]):
							p.append(str(str(f[i][:j])+'x'+str(f[i][j+1:-1])+ str(g[k][-4:])))  #slicing and appending
				count=0
		return(p)				#return 
	o = step4(m,n,o)			#fuction calling

	z=list(o)
	if(len(z)==0):
		z=list(m)
		z.extend(n)	 			# getting the last unempty ist so that we can have the prime implicants stored in a particular list
	if(len(z)==0):
		z=list(q)
		z.extend(w)
		z.extend(r)
	if(len(z)==0):
		z=list(f)
		z.extend(g)
		z.extend(h)
		z.extend(p)
	if(len(z)==0):
		z=list(a)
		z.extend(b)
		z.extend(c)
		z.extend(d)
		z.extend(e)

	def concatinate(q):							#concatinating the list of unneccesary repeatation of the implicants
		for i in range(len(q)):
			for k in range(1+i,len(q)):
				if(q[i][:num]==q[k][:num]):
					q[k] = ''
		while '' in q:
			q.remove('')
		return(q)					#return

	z = concatinate(z)  

	if ")" in z[0]:			#function call
		def left(q):											#getting whats left in quine method of table and storing it in another list
			for i in range(len(q)):
				j=num+1
				while(q[i][j]!=')'):
					if(q[i][j].isdigit()==True):
						if(q[i][j+1].isdigit()==False):
							u.append(q[i][j])
							j+=1
						else:
							u.append(q[i][j]+q[i][j+1])
							j+=2
					else:
						j+=1
			return(u)						#return
		u=left(z)								#fucntion call

		def simple(u):												#removing repeated entries
			for i in range (len(u)):
				for k in range(i+1,len(u)):
					if(u[i]==u[k]):
						u[k]=''
			while '' in u:
				u.remove('')
			return(u)			#return
		u=simple(u)					#function call


	# Further code deals with the dont care conditions and isnt neccssary if you want to simplify it further it adds up to beauty.

		def dcare(f,u,v):
			count=0
			for i in range(len(f)):
				j=5													#to find out whats left, for loop run all over
				while(f[i][j]!=')'):
					if(f[i][j].isdigit()==True):
						if(f[i][j+1].isdigit()==False):
							if(f[i][j] not in u):
								count+=1							#loops
								u.append(f[i][j])
							j+=1
						else:
							if(f[i][j]+f[i][j+1] not in u):
								count+=1
								u.append(f[i][j]+f[i][j+1])
							j+=2
					else:												#else condition
						j+=1
				if(count>=1):
					v.append(f[i])
				count=0
			return(v,u)

		def acare(a,b,c,d,e,v):
			if(len(a)==0 and len(c)==0):
				v.extend(b)															#checking the left over in the very first seperation table
			if(len(b)==0 and len(d)==0):
				v.extend(c)
			if(len(c)==0 and len(e)==0):
				v.extend(d)
			if(len(d)==0):
				v.extend(e)
			for i in range(len(v)):
				v[i]=str(int(v[i],2))							#converting to decimal in returning the value
			return(v)
		v=acare(a,b,c,d,e,v)
		v,u=dcare(n,u,v)
		v,u=dcare(m,u,v)
		v,u=dcare(r,u,v)					#checking each step of the quine table for left over elements
		v,u=dcare(w,u,v)
		v,u=dcare(q,u,v)
		v,u=dcare(p,u,v)
		v,u=dcare(h,u,v)
		v,u=dcare(g,u,v)
		v,u=dcare(f,u,v)
		v=concatinate(v)

		z.extend(v)	
					#storing all implicants including dont care in the same list
		def order(z):
			for i in range(len(z)):
				count=0
				count1=0
				for j in range(num):
					if(z[i][j]=='x'):
						count1+=1
				a=num+1
				while(z[i][a]!=')'):
					if(z[i][a].isdigit()==True):
						if(z[i][a+1].isdigit()==False):
							if z[i][a] in ess:
								count+=1
							a+=1
						else:
							if((z[i][a]+z[i][a+1]) in ess):
								count+=1
							a+=2
					else:
						a+=1
				if(count==(2*count1)):
					temp = z[0]
					z[0]=z[i]
					z.pop(i)
					z.insert(1,temp)
			return(z)
		z=order(z)

		def imp(z):
			prime=[]
			for i in range(len(z)):
				count=0
				j=num+1
				while(z[i][j]!=')'):
					if(z[i][j].isdigit()==True):
						if(z[i][j+1].isdigit()==False):
							if z[i][j] in ess:
								count+=1
								ess.remove(z[i][j])
							j+=1
						else:
							if((z[i][j]+z[i][j+1]) in ess):
								count+=1
								ess.remove((z[i][j]+z[i][j+1]))
							j+=2
					else:
						j+=1
				if(count>=1):
					prime.append(z[i])
			return(prime)
		z=imp(z)
        

	# Expresing the prime implicants in the form of 4 variables
	def exp(z):
		if(num==4):
			dir = {0:'abcd',1:'abcD',2:'abCd',3:'abCD',4:'aBcd',5:'aBcD',6:'aBCd',7:'aBCD',8:'Abcd',9:'AbcD',10:'AbCd',11:'AbCD',12:'ABcd',13:'ABcD',14:'ABCd',15:'ABCD'}
		elif(num==3):
			dir = {0:'abc',1:'abC',2: 'aBc',3:'aBC',4:'Abc',5:'AbC',6:'ABc',7:'ABC'}		#Dictionary
		elif(num==2):
			dir = {0:'ab',1:'aB',2: 'Ab',3:'AB'}
		f=''
		if ')' in z[0]:
			for i in range(len(z)):
				s=[]								#loops
				j=num+1
				while(z[i][j]!=')'):
					if(z[i][j].isdigit()==True):
						if(z[i][j+1].isdigit()==False):
							s.append(dir[int(z[i][j])])				#string appending
							j+=1
						else:
							s.append(dir[int(z[i][j]+z[i][j+1])])
							j+=2
					else:
						j+=1
				for j in range(num):
					count=0
					for k in range(0,len(s)-1):
						if(s[k][j]==s[k+1][j]):				#adding up the variable to create expression 
							count+=1
					if(count==(len(s)-1)):
						if(s[k][j]=='a'):
							f=f+'A\''
						elif(s[k][j]=='b'):
							f=f+'B\''
						elif(s[k][j]=='c'):
							f=f+'C\''
						elif(s[k][j]=='d'):
							f=f+'D\''
						else:
							f=f+s[k][j]
				if(i!=(len(z)-1)):
					f=f+'+'		
		else:
			s=[]
			decimal =0
			for i in range(len(z)):
				for digit in z[i]:
					decimal = decimal*2 + int(digit)	
				z[i]=decimal
				decimal=0
			for i in range(len(z)):
				s.append(dir[(z[i])])
			for i in range(len(s)):
				for j in range(len(s[i])):
					if(s[i][j]=='a'):
							f=f+'A\''
					elif(s[i][j]=='b'):
						f=f+'B\''
					elif(s[i][j]=='c'):
						f=f+'C\''
					elif(s[i][j]=='d'):
						f=f+'D\''
					else:
						f=f+s[i][j]
				if(i!=(len(z)-1)):
					f=f+'+'					#SOP operator
		return(f)
	stringOut=exp(z)		#storing
	return (stringOut, z)    	#returning the K map value back


def solve_kmap(n, e):
    if len(e[1])==0:
        mtdt = "(" + ''.join([str(elem) for elem in e[0]]) + ")" + "d-"
    else:
        mtdt = "(" + ''.join([str(elem) for elem in e[0]]) + ")" + "d(" + ''.join([str(elem) for elem in e[1]]) + ")"


    mt = [int(i) for i in e[0].strip().split()]
    dc = [int(i) for i in e[1].strip().split()]

    mt.sort()
    minterms = mt+dc
    minterms.sort()
    size = len(bin(minterms[-1]))-2
    groups,all_pi = {},set()
    
    values = [0]*n**2
    for i in range(len(values)):
        if i in mt:
            values[i]=1
        elif i in dc:
            values[i]='x'
    
    if Solve == True:
        Y, y = minFunc(str(n), mtdt)
        print("Result: ", Y, y)

        ## Groups
        global g
        g = []
        if type(y[0])!=int:
            for text in y:
                print(text)
                text = text[text.index('(')+len('(' ): text.index(')')]
                g.append( [int(i) for i in text.strip().split(',')] )

            group.set('  '.join([str(elem) for elem in g]))
        else:
            group.set([])
        
    create_kmap(values, g)
    return Y
        

def create_kmap(values, g):
	if len(values) == 16:
		k_grid = list([ [0,0], [0,1], [0,3], [0,2], [1,0], [1,1], [1,3], [1,2], [3,0], [3,1], [3,3], [3,2], [2,0], [2,1], [2,3], [2,2] ])
	if len(values) == 9:
		k_grid = list([ [0,0], [0,1], [1,0], [1,1], [1,0], [3,0], [3,1], [2,0], [2,1] ])
	if len(values) == 4:
		k_grid = list([ [0,0], [0,1], [1,0], [1,1] ])

	for i in range(len(values)):
		m = "m" + str(i)
		value = values[i]
		exec( m + "= addTextLabel(mapframe, i, k_grid[i], value, g)")


## GUI
def addTextLabel(root, n, k_grid, value, g):
    var_m = eval("m"+str(n))

    label_color = "wheat4"
    lh = 4
    lw = 6
    if str(value) == "1" or str(value) == "x" :
        relief = "sunken"
    else:
        relief = "raised"

    var_m = tk.StringVar()
    var_m.set(str(value))
    label = "label"+str(n) 
    
    exec( label + "= tk.Label(root,textvariable = var_m,width = lw,height = lh,background = label_color, highlightbackground=\"black\", highlightcolor=\"black\", highlightthickness=1, borderwidth=2, relief=relief)")
    exec( label +".grid(column = k_grid[1] ,row = k_grid[0])")

    if len(g)>0:
        flag = 0
        for i in range(len(g)):
            if n in g[i]:
                flag += 1
                if flag == 1:
                    if i == 0:
                        label_color = "red"
                    if i == 1:
                        label_color = "blue"
                    if i == 2:
                        label_color = "yellow"
                    if i == 3:
                        label_color = "pink"  
                    if i == 4:
                        label_color = "orange" 
                    if i == 5:
                        label_color = "violet" 
                    if i == 6:
                        label_color = "cyan"  
                elif flag>1:
                    label_color = "grey16" 
                    # lh, lw = 4, 6
                    # if (n + 1) in g[i]:
                    #     lh = 4
                    # if (n + 4) in g[i]:
                    #     lh = 4
                    # if len(g[1]) == 2:
                    #     if (n + 1) in g[i]:
                    #         lw = -6
                    #     if (n + 2) in g[i]:
                    #         lw = -6
                    #     if (n + 8) in g[i]:
                    #         lh = 4
        exec( label + "= tk.Label(root,textvariable = var_m,width = lw,height = lh,background = label_color, highlightbackground=\"black\", highlightcolor=\"black\", highlightthickness=1, borderwidth=2, relief=relief)")
        exec( label +".grid(column = k_grid[1] ,row = k_grid[0])")

    return var_m


def fetch(entries):
    e = []
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()   
        print('%s: "%s"' % (field, text)) 
        e.append(text)
    return e

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=20, text=field, anchor='w')
        ent = tk.Entry(row, width =20)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries


def activate_fetch():        
    global e
    global Solve
    Solve = True
    n = 4                   ## default 4 variables
    e = fetch(ents)
    if e[2] != "":
        n = int(e[2])
    Y = solve_kmap(n, e)
    la.set(Y)           ## Set output on Screen
    return Y





if __name__ == '__main__':
	global Y
	tvar = tk.StringVar
	tvar = ""
	m0 = None
	m1 = None
	m2 = None
	m3 = None
	m4 = None
	m5 = None
	m6 = None
	m7 = None
	m8 = None
	m9 = None
	m10 = None
	m11 = None
	m12= None
	m13 = None
	m14 = None
	m15 = None

	global e
	e=0
	global Solve
	Solve = False    

	def start_gui():
		global root
		root = tk.Tk()
		# MAXW = 750
		# MAXH = 400
		MAXW = 1000
		MAXH = 500
		root.maxsize(MAXW,MAXH)
		root.minsize(MAXW,MAXH)

		root.title("Karnaugh Map Minimiser")
		root.tk_setPalette( "steelblue4")

		setframe = tk.LabelFrame(root, text = "Input", background='skyblue4', borderwidth=5, padx=5, pady=5)
		setframe.grid(row = 0,column = 1)
		selectionframe = tk.Frame(root)
		selectionframe.grid(row = 0,column = 2)
		sol_frame = tk.LabelFrame(root, text= "Result:", background='skyblue4', borderwidth=5, padx=7, pady=7, width = 500)
		sol_frame.grid(row = 1 ,column = 3 )
		# result_label = tk.Label(sol_frame)
		# result_label.grid()

		global la
		la = tk.StringVar()
		la.set("Karnaugh Minimization")


		sol_text = tk.Entry(sol_frame,bg = "goldenrod", fg = 'black', textvariable=la, relief="ridge")
		sol_text.config(width = 25)
		sol_text.grid()

		root.tk_focusFollowsMouse()

		global mapframe
		mapframe = tk.LabelFrame(root,text="K-map", borderwidth=5, relief="ridge")
		mapframe.grid(row = 1,column = 1)

		groupframe = tk.LabelFrame(root,text="Groups", background='skyblue4', borderwidth=5, relief="ridge")
		groupframe.grid(row = 1,column = 0)

		global group
		global g
		g = []
		group = tk.StringVar()
		group.set(g)
		groups = tk.Entry(groupframe, bg = "goldenrod", fg = 'black', textvariable=group, width=25)
		groups.pack()
		# groups.config(width = 25)
		# groups.grid()

		global fields
		global ents
		fields = 'Enter the minterms', 'Enter the don\'t cares(If any)', 'Number of variables'
		ents = makeform(setframe, fields) 

		Sol = tk.Button(selectionframe,bg="black", text = "Solve", fg = "white", command = activate_fetch)
		Sol.grid(row = 0 , column = 2)

		Reset = tk.Button(selectionframe, text = "Reset", command = refresh)
		Reset.grid(row = 1 , column = 2)

		Quit = tk.Button(selectionframe, text = "Quit", command = root.destroy)
		Quit.grid(row = 2 , column = 2)

		root.mainloop()

	def refresh():
		root.destroy()
		start_gui()

	start_gui()
