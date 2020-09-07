# coding: utf-8
#programa filtra os minerais por características físicas em comum e exibe em uma lista. retorna foto e informações gerais quando selecionado na lista.
#no menu arquivo a opção salvar, salva a lista de minerais filtrados em arquivo de texto e no diretório que desejar.
#a opção adicionar mineral possibilita incrementar o banco de dados. se o mineral já estiver no bancos de dados, o programa informa a existência e nada acontece. 
from tkinter import *
from PIL import Image
import os
root=Tk()
titulo=Label(root, text="Lab. de Mineralogia - Geologia/UFRJ", font="arial 20 bold", foreground="blue")
titulo.pack(side=TOP)
dica=Label(root, text="Clique em Filtrar para exibir uma lista de minerais. Clique no nome do mineral para ver detalhes. Para adicionar mais minerais, ir no menu Arquivo -> adicionar mineral")
dica.pack(side=TOP)
class Checkbuttons:
    def __init__(self,root):
        self.root=root
        frame_pfisicas=Frame(self.root)
        frame_pfisicas.pack(side=TOP)
        
        frame_dureza=Frame(frame_pfisicas)
        frame_dureza.pack(side=LEFT, anchor="nw", fill=X)
        titulo_dureza=Label(frame_dureza, text="Dureza:")
        titulo_dureza.pack(side=TOP, anchor="w")
        self.dureza=StringVar()
        self.dureza.set("todos.txt")
        Checkbutton(frame_dureza, text="0 a 2.5", variable=self.dureza, onvalue="dureza_0a2.5.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_dureza, text="3 a 4.5", variable=self.dureza, onvalue="dureza_3a4.5.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_dureza, text="5 a 6.5", variable=self.dureza, onvalue="dureza_5a6.5.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_dureza, text="7 a 8.5", variable=self.dureza, onvalue="dureza_7a8.5.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_dureza, text="9 a 10", variable=self.dureza, onvalue="dureza_9a10.txt", offvalue="todos.txt").pack(anchor="w")

        frame_habito=Frame(frame_pfisicas)
        frame_habito.pack(side=LEFT, anchor="nw", fill=X)
        titulo_habito=Label(frame_habito, text="Hábito:")
        titulo_habito.pack(side=TOP, anchor="w")
        self.habito=StringVar()
        self.habito.set("todos.txt")
        Checkbutton(frame_habito, text="Maciço", variable=self.habito, onvalue="macico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_habito, text="Tabular", variable=self.habito, onvalue="tabular.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_habito, text="Laminar", variable=self.habito, onvalue="laminar.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_habito, text="Prismático", variable=self.habito, onvalue="prismatico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_habito, text="Granular", variable=self.habito, onvalue="granular.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_habito, text="Acicular", variable=self.habito, onvalue="acicular.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_habito, text="Cúbico", variable=self.habito, onvalue="cubico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_habito, text="fibroso", variable=self.habito, onvalue="fibroso.txt", offvalue="todos.txt").pack(anchor="w")

        frame_clivagem=Frame(frame_pfisicas)
        frame_clivagem.pack(side=LEFT, anchor="nw", fill=X)
        titulo_clivagem=Label(frame_clivagem, text="Clivagem:")
        titulo_clivagem.pack(side=TOP, anchor="w")
        self.clivagem=StringVar()
        self.clivagem.set("todos.txt")
        Checkbutton(frame_clivagem, text="Perfeita", variable=self.clivagem, onvalue="clivagem_perfeita.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_clivagem, text="Boa", variable=self.clivagem, onvalue="clivagem_boa.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_clivagem, text="Ruim", variable=self.clivagem, onvalue="clivagem_ruim.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_clivagem, text="Inexistente", variable=self.clivagem, onvalue="clivagem_inexistente.txt", offvalue="todos.txt").pack(anchor="w")

        frame_fratura=Frame(frame_pfisicas)
        frame_fratura.pack(side=LEFT, anchor="nw", fill=X)
        titulo_fratura=Label(frame_fratura, text="Fratura:")
        titulo_fratura.pack(side=TOP, anchor="w")
        self.fratura=StringVar()
        self.fratura.set("todos.txt")
        Checkbutton(frame_fratura, text="Conchoidal", variable=self.fratura, onvalue="fratura_conchoidal.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_fratura, text="Fibrosa", variable=self.fratura, onvalue="fratura_fibrosa.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_fratura, text="Irregular", variable=self.fratura, onvalue="fratura_irregular.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_fratura, text="Serrilhada", variable=self.fratura, onvalue="fratura_serrilhada.txt", offvalue="todos.txt").pack(anchor="w")

        frame_tenacidade=Frame(frame_pfisicas)
        frame_tenacidade.pack(side=LEFT, anchor="nw", fill=X)
        titulo_tenacidade=Label(frame_tenacidade, text="Tenacidade:")
        titulo_tenacidade.pack(side=TOP, anchor="w")
        self.tenacidade=StringVar()
        self.tenacidade.set("todos.txt")
        Checkbutton(frame_tenacidade, text="Quebradiço", variable=self.tenacidade, onvalue="quebradico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_tenacidade, text="Maleável", variable=self.tenacidade, onvalue="maleavel.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_tenacidade, text="Flexível", variable=self.tenacidade, onvalue="flexivel.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_tenacidade, text="Séctil", variable=self.tenacidade, onvalue="sectil.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_tenacidade, text="Dúctil", variable=self.tenacidade, onvalue="ductil.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_tenacidade, text="Elástico", variable=self.tenacidade, onvalue="elastico.txt", offvalue="todos.txt").pack(anchor="w")

        frame_brilho=Frame(frame_pfisicas)
        frame_brilho.pack(side=LEFT, anchor="nw", fill=X)
        titulo_brilho=Label(frame_brilho, text="Brilho:")
        titulo_brilho.pack(side=TOP, anchor="w")
        self.brilho=StringVar()
        self.brilho.set("todos.txt")
        Checkbutton(frame_brilho, text="Metálico", variable=self.brilho, onvalue="metalico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_brilho, text="Submetálico", variable=self.brilho, onvalue="submetalico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_brilho, text="Vítreo", variable=self.brilho, onvalue="vitreo.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_brilho, text="Resinoso", variable=self.brilho, onvalue="resinoso.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_brilho, text="Adamantino", variable=self.brilho, onvalue="adamantino.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_brilho, text="Nacarado", variable=self.brilho, onvalue="nacarado.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_brilho, text="Gorduroso", variable=self.brilho, onvalue="gorduroso.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_brilho, text="Sedoso", variable=self.brilho, onvalue="sedoso.txt", offvalue="todos.txt").pack(anchor="w")

        frame_cor=Frame(frame_pfisicas)
        frame_cor.pack(side=LEFT, anchor="nw", fill=X)
        titulo_cor=Label(frame_cor, text="Cor:")
        titulo_cor.pack(side=TOP, anchor="w")
        self.cor=StringVar()
        self.cor.set("todos.txt")
        Checkbutton(frame_cor, text="Preto", variable=self.cor, onvalue="preto.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_cor, text="Azul", variable=self.cor, onvalue="azul.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_cor, text="Verde", variable=self.cor, onvalue="verde.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_cor, text="Amarelo", variable=self.cor, onvalue="amarelo.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_cor, text="Vermelho", variable=self.cor, onvalue="vermelho.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_cor, text="Branco", variable=self.cor, onvalue="branco.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_cor, text="Cinza", variable=self.cor, onvalue="cinza.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_cor, text="Incolor", variable=self.cor, onvalue="incolor.txt", offvalue="todos.txt").pack(anchor="w")

        frame_diafaneidade=Frame(frame_pfisicas)
        frame_diafaneidade.pack(side=LEFT, anchor="nw", fill=X)
        titulo_diafaneidade=Label(frame_diafaneidade, text="Diafaneidade:")
        titulo_diafaneidade.pack(side=TOP, anchor="w")
        self.diafaneidade=StringVar()
        self.diafaneidade.set("todos.txt")
        Checkbutton(frame_diafaneidade, text="Transparente", variable=self.diafaneidade, onvalue="transparente.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_diafaneidade, text="Translúcido", variable=self.diafaneidade, onvalue="translucido.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_diafaneidade, text="Opaco", variable=self.diafaneidade, onvalue="opaco.txt", offvalue="todos.txt").pack(anchor="w")

        frame_traco=Frame(frame_pfisicas)
        frame_traco.pack(side=LEFT, anchor="nw", fill=X)
        titulo_traco=Label(frame_traco, text="Traço:")
        titulo_traco.pack(side=TOP, anchor="w")
        self.traco=StringVar()
        self.traco.set("todos.txt")
        Checkbutton(frame_traco, text="Preto", variable=self.traco, onvalue="traco_preto.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_traco, text="Castanho", variable=self.traco, onvalue="traco_castanho.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_traco, text="Amarelo", variable=self.traco, onvalue="traco_amarelo.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_traco, text="Cinza", variable=self.traco, onvalue="traco_cinza.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_traco, text="Vermelho", variable=self.traco, onvalue="traco_vermelho.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_traco, text="Azul", variable=self.traco, onvalue="traco_azul.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_traco, text="Verde", variable=self.traco, onvalue="traco_verde.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_traco, text="Incolor", variable=self.traco, onvalue="traco_incolor.txt", offvalue="todos.txt").pack(anchor="w")

        frame_scristalino=Frame(frame_pfisicas)
        frame_scristalino.pack(anchor="nw", fill=X)
        titulo_scristalino=Label(frame_scristalino, text="Sistema cristalino:")
        titulo_scristalino.pack(side=TOP, anchor="w")
        self.scristalino=StringVar()
        self.scristalino.set("todos.txt")
        Checkbutton(frame_scristalino, text="Isométrico", variable=self.scristalino, onvalue="isometrico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_scristalino, text="Tetragonal", variable=self.scristalino, onvalue="tetragonal.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_scristalino, text="Ortorrômbico", variable=self.scristalino, onvalue="ortorrombico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_scristalino, text="Romboédrico", variable=self.scristalino, onvalue="romboedrico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_scristalino, text="Hexagonal", variable=self.scristalino, onvalue="hexagonal.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_scristalino, text="Monoclínico", variable=self.scristalino, onvalue="manoclinico.txt", offvalue="todos.txt").pack(anchor="w")
        Checkbutton(frame_scristalino, text="Triclínico", variable=self.scristalino, onvalue="triclinico.txt", offvalue="todos.txt").pack(anchor="w")

check=Checkbuttons(root)
frame_mineral=Frame(root)
frame_mineral.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
u=Canvas(frame_mineral)
u.pack(side=LEFT, fill=BOTH, expand=TRUE)
caracteristicas=Message(frame_mineral)
caracteristicas.pack(side=LEFT, fill=Y, expand=TRUE)
sb=Scrollbar(frame_mineral)
sb.pack(side=RIGHT, fill=Y)
lista=Listbox(frame_mineral)
lista.pack(fill=Y, expand=TRUE)

sb.configure(command=lista.yview)
lista.configure(yscrollcommand=sb.set)
class Filtrar:
    def filtro_dureza(self):
        self.dur=set()
        arquivodureza=open(check.dureza.get(), "r")
        for linha in arquivodureza:
            self.dur.add(linha)
        
        return self.dur        

    def filtro_brilho(self):
        self.bri=set()
        arquivobrilho=open(check.brilho.get(), "r")
        for linha in arquivobrilho:
            self.bri.add(linha)
        return self.bri

    def filtro_clivagem(self):
        self.cli=set()
        arquivoclivagem=open(check.clivagem.get(), "r")
        for linha in arquivoclivagem:
            self.cli.add(linha)
        return self.cli

    def filtro_fratura(self):
        self.fra=set()
        arquivofratura=open(check.fratura.get(), "r")
        for linha in arquivofratura:
            self.fra.add(linha)
        return self.fra

    def filtro_habito(self):
        self.hab=set()
        arquivohabito=open(check.habito.get(), "r")
        for linha in arquivohabito:
            self.hab.add(linha)
        return self.hab
    def filtro_cor(self):
        self.cor=set()
        arquivocor=open(check.cor.get(), "r")
        for linha in arquivocor:
            self.cor.add(linha)
        return self.cor

    def filtro_diafaneidade(self):
        self.dia=set()
        arquivodiafaneidade=open(check.diafaneidade.get(), "r")
        for linha in arquivodiafaneidade:
            self.dia.add(linha)
        return self.dia

    def filtro_tenacidade(self):
        self.ten=set()
        arquivotenacidade=open(check.tenacidade.get(), "r")
        for linha in arquivotenacidade:
            self.ten.add(linha)
        return self.ten

    def filtro_scristalino(self):
        self.scr=set()
        arquivoscristalino=open(check.scristalino.get(), "r")
        for linha in arquivoscristalino:
            self.scr.add(linha)
        return self.scr

    def filtro_traco(self):
        self.tra=set()
        arquivotraco=open(check.traco.get(), "r")
        for linha in arquivotraco:
            self.tra.add(linha)
        return self.tra
        
    def filtrar(self):
        a=open("todos.txt", "r")
        self.filtrado=[]
               
        for linha in a:
            
            if linha in self.filtro_dureza() and linha in self.filtro_brilho() and linha in self.filtro_clivagem() \
               and linha in self.filtro_cor() and linha in self.filtro_diafaneidade() and linha in self.filtro_fratura() \
               and linha in self.filtro_habito() and linha in self.filtro_scristalino() and linha in self.filtro_tenacidade() and linha in self.filtro_traco():
                self.filtrado.append(linha.strip("\n"))
            
        for i in range(1000):
            lista.delete(0)        
        for i in self.filtrado:
            lista.insert(END, i)
            
        return self.filtrado
    

class Mineral_id:
    def __init__(self, root):
        self.root=root
        principal = Menu(self.root)
        arquivo = Menu(principal)
        arquivo.add_command(label="salvar lista", command=self.janela_salvar)        
        arquivo.add_command(label="adicionar mineral", command=self.janela_adicionar)
        principal.add_cascade(label="Arquivo", menu=arquivo)
        self.root.configure(menu=principal)
        
        f=Filtrar()        
        b1=Button(self.root, text="Filtrar", command=f.filtrar)
        b1.pack(side=TOP)        
        lista.bind("<ButtonRelease-1>", self.curprint)
        
        

    def curprint(self, x):        
        self.img=PhotoImage(file=(os.getcwd()+"\\FOTOS\\"+lista.get(lista.curselection())+".gif"))
        i=u.create_image(300,250, image=self.img)        
        ob=open("obs.txt", "r")
        for linha in ob:
            l=linha.split()
            if lista.get(lista.curselection())==l[0]:
                caracteristicas.configure(text=l[1:])
        ob.close()           

    def __call__(self, qualquer_coisa):
        return qualquer_coisa        

    def janela_salvar(self):
        ftypes = [('Text files', '*.txt')]
        dlg = tkFileDialog.SaveAs(self.root, filetypes = ftypes)        
        fl = dlg.show()        
        if fl != '':
            text = self.save(fl)
    def save(self, filename):
        f=Filtrar()
        s = open(filename+".txt", "w")
        l=""
        for i in f.filtrar():
            l+=i+"\n"
        s.write(l)
        s.close()
    def carregar_imagem(self):
        ftypes = [('GIF files', '*.gif')]
        dlg = tkFileDialog.Open(self.janela_add, filetypes = ftypes)        
        fl = dlg.show()
        if fl != '':
            image = self.imagem(fl)
            
            self.janela_add.focus()
            self.status.configure(text="Foto carregada com sucesso!", font="arial 10", foreground="blue")
        else:
            return 0
    def imagem(self, filename):
        im=Image.open(filename)
        
        
        im=im.resize((336, 336), Image.ANTIALIAS)
        im.save(filename)
        self.foto=PhotoImage(file=filename)
        print (self.foto.width())
        print (self.foto.height())
        
        
        self.copia=self.foto.copy()
        self.verifica.set("Y")
                
        i=self.img_carregar.create_image(200,200, image=self.foto)
                
    def janela_adicionar(self):
        self.janela_add=Toplevel(self.root)
        self.janela_add.title("Adicionar mineral")
        frame1=Frame(self.janela_add)
        frame1.pack(side=TOP, fill=X)
        titulo=Label(frame1, text="Nome do Mineral:", font="Arial 20 bold")
        titulo.pack(side=LEFT, fill=BOTH)
        self.mineral=StringVar(self.root)
        entrada=Entry(frame1, textvar=self.mineral)
        entrada.pack(side=LEFT, fill=X)        
        b1=Button(frame1, text="Adicionar", command=self.adiciona)
        b1.pack(side=LEFT)
        aviso_add=Label(frame1, text="<-- Preencha todos os dados antes de adicionar!", font="arial 12 bold")
        aviso_add.pack(side=LEFT)
        self.verifica=StringVar(self.root)
        self.verifica.set("N")
        self.check_add=Checkbuttons(self.janela_add)
        
        frame2=Frame(self.janela_add)
        frame2.pack(side=TOP, fill="both")
        label_obs=Label(frame2, text="Descreva o mineral no campo abaixo:", font="Arial 10 bold")
        label_obs.pack(side=TOP)
        self.obsv=StringVar(self.root)
        obs=Entry(frame2, textvar=self.obsv)
        obs.pack(side=TOP, fill="both")
        b2=Button(frame2, text="Carregar foto", command=self.carregar_imagem)
        b2.pack(side=TOP)
        self.img_carregar=Canvas(self.janela_add)
        self.img_carregar.pack(fill=Y, expand=TRUE)
        
        self.status=Label(self.janela_add, text="Selecione as propriedades físicas do mineral.")
        self.status.pack(side=BOTTOM)
        
    def adiciona(self):
        def adiciona_todos():
            add=open("todos.txt", "r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open("todos.txt", "w")
            add.write(l)
            add.close()
        def adiciona_dureza():
            add=open(self.check_add.dureza.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.dureza.get(), "w")
            add.write(l)
            add.close()
                        
        def adiciona_brilho():
            add=open(self.check_add.brilho.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.brilho.get(), "w")
            add.write(l)
            add.close()
                        
        def adiciona_clivagem():            
            add=open(self.check_add.clivagem.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.clivagem.get(), "w")
            add.write(l)
            add.close()
                        
        def adiciona_fratura():
            add=open(self.check_add.fratura.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.fratura.get(), "w")
            add.write(l)
            add.close()
                        
        def adiciona_habito():
            add=open(self.check_add.habito.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.habito.get(), "w")
            add.write(l)
            add.close()
                       
        def adiciona_tenacidade():
            add=open(self.check_add.tenacidade.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.tenacidade.get(), "w")
            add.write(l)
            add.close()
                       
        def adiciona_diafaneidade():
            add=open(self.check_add.diafaneidade.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.diafaneidade.get(), "w")
            add.write(l)
            add.close()
                        
        def adiciona_cor():
            add=open(self.check_add.cor.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.cor.get(), "w")
            add.write(l)
            add.close()
                  
        def adiciona_scristalino():
            add=open(self.check_add.scristalino.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.scristalino.get(), "w")
            add.write(l)
            add.close()
                       
        def adiciona_traco():
            add=open(self.check_add.traco.get(),"r")
            l=""
            for linha in add:
                l+=linha
                if linha.strip("\n")==str.upper(self.mineral.get()):
                    return 0
            l+=str.upper(self.mineral.get())+"\n"
            add.close()
            add=open(self.check_add.traco.get(), "w")
            add.write(l)
            add.close()
        if self.mineral.get()=="":
            self.status.configure(text="Faltou digitar o nome do Mineral!!!", font="arial 16 bold", foreground="red")
            return 0
        elif self.verifica.get()=="N":
            self.status.configure(text="falta carregar a imagem!!!", font="arial 12 bold", foreground="red")
            return 0
        elif (adiciona_dureza(), adiciona_todos(), adiciona_brilho(), adiciona_clivagem(), adiciona_fratura(), \
                       adiciona_habito(), adiciona_tenacidade(), adiciona_diafaneidade(), adiciona_cor(), \
                       adiciona_scristalino(), adiciona_traco()) == (0,0,0,0,0,0,0,0,0,0,0):
            self.status.configure(text=("o mineral %s já está presente no banco de dados" % self.mineral.get()), font="arial 16 bold", foreground="red")
            return 0
        else:
            self.copia.write(os.getcwd()+"\\FOTOS\\"+str.upper(self.mineral.get())+".gif", "gif")
            ob=open("obs.txt", "r")
            l=""
            for linha in ob:
                l+=linha
                if linha[0]==str.upper(self.mineral.get()):
                    return 0
            print (self.obsv.get())
            l+=str.upper(self.mineral.get())+" "
            l+=self.obsv.get().encode('latin-1')+"\n"
            ob.close()
            ob=open("obs.txt", "w")
            ob.write(l)
            ob.close()            
            self.status.configure(text="Mineral adicionado", font="arial 16 bold", foreground="blue")
            return adiciona_dureza(), adiciona_brilho(), adiciona_clivagem(), adiciona_fratura(), \
                   adiciona_habito(), adiciona_tenacidade(), adiciona_diafaneidade(), adiciona_cor(), \
                   adiciona_scristalino(), adiciona_traco(), adiciona_todos()
    
        
        

a=Mineral_id(root)
root.title("Mineral ID")

root.mainloop()
