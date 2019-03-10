#script para simular assembly lendo arquivo 
#transforma um binário em inteiro
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
#transformar inteiro em binario
def binCon(value):
	x=value
	sx=""
	while (x!=0) :
		sx=sx+str(x%2)
		x=int(x/2)
		

	return sx[::-1]

#deixa os registradores com 32 digitos
def register_formation(re):
	v=re;
	x="0";

	while(len(v)<32):
		v=x+v;

	return v;

#função para inicializar arquivo dos registradores 
def init(arq):
	regs=[];
	for i in range (32):
	

		regs.append("{} {}\n".format(i,"00000000000000000000000000000010"));


	arq.writelines(regs);
	arq.close();
	return regs;

#função para limpar a formatação
def clearFormatation(comando):

	comando=comando.replace("$","");
	comando=comando.replace(",","");
	comando=comando.replace("(","");
	comando=comando.replace(")","");
	comando=comando.replace("\n","");

	return comando;





#arquivo com comandos em assembly para executar 
entrada=open('input.txt','r');
#arquivo aonde ficam os registradores
saida=open('reg.txt','w');

linhasE=entrada.readlines();
#Lista com registradores 

#inicializando o arquivo de registradores
regs=init(saida);



for i in range (len(linhasE)):
	#limpa a formatação da instrução para apenas números
	comando=clearFormatation(linhasE[i]);
	
	#separa a instrução 
	comandoL=comando.split();

	if(comandoL[0]=="ADD" or comandoL[0]=="ADDU" ):
		print("ADD");
		rd=int(comandoL[1]);
		rs=int(comandoL[2]);
		rt=int(comandoL[3]);
		#pegando os valores dos registradores
		regS = regs[rs].split();
		regT = regs[rt].split();
		add  = intCon(regS[1])+intCon(regS[1]);
		regs[rd]="{} {}\n".format(rd,register_formation(binCon(add)));
	elif(comandoL[0]=="SUB" or comandoL[0]=="SUBU"):
		
		rd=int(comandoL[1]);
		rs=int(comandoL[2]);
		rt=int(comandoL[3]);
		#pegando os valores dos registradores
		regS = regs[rs].split();
		regT = regs[rt].split();
		add  = intCon(regS[1])-intCon(regS[1]);
		regs[rd]="{} {}\n".format(rd,register_formation(binCon(add)));

	elif(comandoL[0]=="AND"):

		rd=int(comandoL[1]);
		rs=int(comandoL[2]);
		rt=int(comandoL[3]);
		#pegando os valores dos registradores
		regS = regs[rs].split();
		regT = regs[rt].split();
		add  = intCon(regS[1]) & intCon(regS[1]);
		regs[rd]="{} {}\n".format(rd,register_formation(binCon(add)));

	elif(comandoL[0]=="OR"):
		rd=int(comandoL[1]);
		rs=int(comandoL[2]);
		rt=int(comandoL[3]);
		#pegando os valores dos registradores
		regS = regs[rs].split();
		regT = regs[rt].split();
		add  = intCon(regS[1]) | intCon(regS[1]);
		regs[rd]="{} {}\n".format(rd,register_formation(binCon(add)));
	elif(comando[0]=="XOR"):
		rd=int(comandoL[1]);
		rs=int(comandoL[2]);
		rt=int(comandoL[3]);
		#pegando os valores dos registradores
		regS = regs[rs].split();
		regT = regs[rt].split();
		add  = intCon(regS[1]) ^ intCon(regS[1]);
		regs[rd]="{} {}\n".format(rd,register_formation(binCon(add)));
	elif(comandoL[0]=="NOR"):
		rd=int(comandoL[1]);
		rs=int(comandoL[2]);
		rt=int(comandoL[3]);
		#pegando os valores dos registradores
		regS = regs[rs].split();
		regT = regs[rt].split();
		add  = ~(intCon(regS[1]) ^ intCon(regS[1]));
		regs[rd]="{} {}\n".format(rd,register_formation(binCon(add)));






		

saida=open("reg.txt",'w');
saida.writelines(regs);



	




