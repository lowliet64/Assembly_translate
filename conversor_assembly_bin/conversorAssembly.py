#transformar inteiro em binario
def binCon(value):
	x=value;
	sx="";
	while (x!=0) :
		sx=sx+str(x%2);
		x=int(x/2);
		

	return sx[::-1];

#deixar o op_code com 6 digitos
def op_formation(op_x):
	v=op_x;
	x="0";

	while(len(v)<6):
		v=x+v;

	return v;
#deixa os registradores com 5 digitos
def register_formation(re):
	v=re;
	x="0";

	while(len(v)<5):
		v=x+v;

	return v;
#deixa os IMM com 16 digitos
def imm_formation(imm):
	v=imm;
	x="0";
	while(len(v)<16):
		v=x+v;

	return v;
#deixa o address com 26 digitos	
def adress_formation(adress):
    v = adress
    x = "0"

    while (len(v) < 26):
        v = x + v

    return v


inp=open("input.txt",'r');
entrada=inp.readlines();
saida=[];



op={
 'LB':32,
 'LH':33,
 'LWL':34,
 'LW':35,
 'LBU':36,
 'LHU':37,
 'LWR':38,
 'SB':40,
 'SH':41,
 'SWL':42,
 'SW':43,
 'SWR':46,
 'ADDI':8,
 'ADDIU':9,
 'SLTI':10,
 'SLTIU':11,
 'ANDI':12,
 'ORI':13,
 'XORI':14,
 'LUI':15,
 'BLTZ':1,
 'BGEZ':1,
 'BLTZAL':1,
 'BGEZAL':1,
 'BEQ':4,
 'BNE':5,
 'BLEZ':6,
 'BGTS':7,


}

opJ={
	'J':2,
	'JAL':3
}

func={
    'BLTZ':0,
    'BGEZ':1,
    'BLTZAL':16,
    'BGEZAL':17,
    'ADD':32,
    'ADDU':33,
    'SUB':34,
    'SUBU':35,
    'AND':36,
    'OR':37,
    'XOR':38,
    'NOR':39,
    'SLT':42,
    'SLTU':43,
    'SLL':0,
    'SRL':2,
    'SRA':3,
    'MFHI':16,
    'MTHI':17,
    'MFLO':18,
    'MULT':24,
    'MULTU':25,
    'DIV':26,
    'DIVU':27,
    'JR':8,
    'JARL':9


}


out=open("out.txt",'w');
instrucaoT=[];


for linha in entrada:
	instrucaoNT = linha.split(" ");
	for i in range (len(instrucaoNT)):
		instrucaoNT[i]=instrucaoNT[i].replace("$","");
		instrucaoNT[i]=instrucaoNT[i].replace("(","")
		instrucaoNT[i]=instrucaoNT[i].replace(")","")
		instrucaoNT[i]=instrucaoNT[i].replace(",","")
		instrucaoNT[i]=instrucaoNT[i].replace("\n","")
		
  
		if(instrucaoNT[i]=="(" or instrucaoNT[i]==")" or instrucaoNT[i]=="$"):
			instrucaoNT[i]="";



	for i in instrucaoNT:
		if(i!=""):
			instrucaoT.append(i);





	print(instrucaoT)		


	if  instrucaoT[0] not in op and instrucaoT[0] not in func and instrucaoT[0] not in opJ :
		saida.append("Instrução não reconhecida \n");
	elif instrucaoT [0] not in op and instrucaoT[0] in func:
		#tipo R
		instrucao="";
		f=op_formation(str(binCon(int(func[instrucaoT[0]]))));
		op_code="000000";
		rd=register_formation(str(binCon(int(instrucaoT[1]))))
		rs=register_formation(str(binCon(int(instrucaoT[2]))))
		rt=register_formation(str(binCon(int(instrucaoT[3]))))
		sa="00000"

		instrucao=op_code+rd+rs+rt+sa+f;
		saida.append(instrucao+"\n");
	elif instrucaoT[0] in op:
		#tipo I
		instrucao=""
		op_code=op_formation(str(binCon(op[instrucaoT[0]])));
		rt= register_formation(str(binCon(int(instrucaoT[1]))));
		imm=imm_formation(str(binCon(int(instrucaoT[2]))));
		rs= register_formation(str(binCon(int(instrucaoT[3]))));

		instrucao=op_code+rt+rs+imm;
		print(instrucao)
		saida.append(str((instrucao))+"\n");
	
	elif instrucaoT[0] in opJ:
		instrucao=""
		op_code=op_formation(str(binCon(opJ[instrucaoT[0]])));
		adress_code=adress_formation(str(binCon(int(instrucaoT[1]))));
		instrucao=op_code+adress_code
		saida.append(instrucao+"\n");
	instrucaoT.clear();





out.writelines(saida);
out.close();