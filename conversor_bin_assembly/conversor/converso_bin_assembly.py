
#transformar inteiro em binario
def binCon(value):
	x=value
	sx=""
	while (x!=0) :
		sx=sx+str(x%2)
		x=int(x/2)
		

	return sx[::-1]


def intCon(value):
	x=value
	stvalue=str(x)[::-1]
	sx=0
	i=0

	while(i<len(str(stvalue))):
		b=int(stvalue[i])
		sx=sx+int(b*(2**i))
		i=i+1
	return sx

def instI(operation,value):
	op=value[0:6]
	rs=value[11:16]
	rt=value[6:11]
	imm=value[16:32]
	r="{} ${},{}(${})".format(operation,intCon(rt),intCon(imm),intCon(rs))
	return r

def instJ(operation,value):
  op=value[0:6]
  index=value[6:32]

  r="{} {}".format(operation,intCon(value)) 
  return r

def instR(operation,value):
  op=value[0:6]
  rs=value[6:11]
  rt=value[11:16]
  rd=value[16:21]
  shamt=value[21:26]
  funct=value[26:32]
	
  r="{} ${} ${} ${}".format(operation,intCon(rd),intCon(rs),intCon(rt))

  return r

inp=open("input.txt",'r')
inputs=inp.readlines()
lista=[];

out=open('out.txt','w')

#print(bin(comandoBin))
print("digite um valor binario para transformar em instrucao")
i=0;
for  linha in inputs:
  i+=1
  if(i>len(inputs)-1):
    break;
  y=linha
  print(y)
  print(len(inputs))

  #op_Code variable
  op_code=y[0:6]
  funct_code=y[26:32]
  address=y[6:32];
  #op_Code String
  op_codestr=""

  #op_code in integer format 
  o=intCon(op_code)
  f=intCon(funct_code)
  a=intCon(address);

  #instruction I type
  #28
  if(o==32): #1
    op_codestr="LB"
    lista.append(instI(op_codestr,y)+"\n")
   
  elif(o==33):#2
    op_codestr="LH"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==34):#3
    op_codestr="LWL"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==35):#4
    op_codestr="LW"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==36):#4
    op_codestr="LBU"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==37):#5
    op_codestr="LHU"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==38):#6
    op_codestr="LWR"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==40):#7
    op_codestr="SB"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==41):#8
    op_codestr="SH"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==42):#9
    op_codestr="SWL"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==43):#10
    op_codestr="SW"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==46):#11
    op_codestr="SWR"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==8):#12
    op_codestr="ADDI"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==9):#13
    op_codestr="ADDIU"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==10):#14
    op_codestr="SLTI"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==11):#15
    op_codestr="SLTIU"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==12):#16
    op_codestr="ADDI"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==13):#17
    op_codestr="ORI"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==14):#18
    op_codestr="XORI"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==15):#19
    op_codestr="LUI"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==1 and f==0):#20
    op_codestr="BLTZ"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==1 and f==1):#21
    op_codestr="BGEZ"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==1 and f==16):#22
    op_codestr="BLTZAL"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==1 and f==17):#23
    op_codestr="BGEZAL"
    lista.append(str(instI(op_codestr,y))+"\n")
   


  #especial
  elif(o==4):#1
    op_codestr="BEQ"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  #especial
  elif(o==5):#2
    op_codestr="BNE"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==6):
    op_codestr="BLEZ"
    lista.append(str(instI(op_codestr,y))+"\n")
   
  elif(o==7):
    op_codestr="BGTZ"
    lista.append(str(instI(op_codestr,y))+"\n")
   


  #type J 2 
  if(o==2):#1
    op_codestr="J"

    lista.append(instJ(op_codestr,address)+"\n")
   
  elif(o==3):#2
    op_codestr="JAL"
    lista.append(instJ(op_codestr,address)+"\n")
   
  #type R
  #23
  if(o==0):
    if(f==32):#1
      op_codestr="ADD"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==33):#2
      op_codestr="ADDU"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==34):#3
      op_codestr="SUB"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==35):#4
      op_codestr="SUBU"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==36):#5
      op_codestr="AND"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==37):#6
      op_codestr="OR"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==38):#7
      op_codestr="XOR"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==39):#8
      op_codestr="NOR"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==42):#9
      op_codestr="SLT"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==43):#10
      op_codestr="SLTU"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==0):#11
      op_codestr="SLL"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==2):#12
      op_codestr="SRL"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==3):#13
      op_codestr="SRA"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==16):#14
      op_codestr="MFHI"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==17):#15
      op_codestr="MTHI"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==18):#16
      op_codestr="MFLO"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==19):#17
      op_codestr="MTLO"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==24):#18
      op_codestr="MULT"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==25):#19
      op_codestr="MULTU"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==26):#20
      op_codestr="DIV"
      lista.append(instR(op_codestr,y)+"\n")
     
    elif(f==27):#21
      op_codestr="DIVU"
      lista.append(instR(op_codestr,y)+"\n")
      
    elif(f==8):#22
      op_codestr="JR"
      lista.append(instR(op_codestr,y)+"\n")

    elif(f==9):#23
      op_codestr="JALR"
      lista.append(instR(op_codestr,y)+"\n")

out.writelines(lista);
out.close();
      





