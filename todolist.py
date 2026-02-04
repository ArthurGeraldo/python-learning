#TAREFAS.TXT
try:
    open("tarefas.txt", "r").close()
except FileNotFoundError:
    open("tarefas.txt", "w").close()
with open("tarefas.txt", "r") as arquivo:
    lista = arquivo.read().splitlines()

#IMPORTAÇÃO
import os

#FUNÇÃO

#-LISTAR TAREFAS
def listartarefa():
    for i, tarefa in enumerate(lista, start=1):
        print(f"{i}-{tarefa}")

#-LIMPAR TERMINAL
def limpar():
    os.system("cls")

#-SALVAR MUDANÇÃS EM TAREFAS.TXT
def salvar(lista):
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in lista:
            arquivo.write(tarefa + "\n")

#MENU
while True:
        limpar()

        #- MENU DE INTERAÇÃO
        print("LISTA DE TAREFAS")
        print("OQUE VOCÊ QUER FAZER?\n1-LISTAR\n2-ADICIONAR A LISTA\n3-REMOVER DA LISTA\n4-ATUALIZAR A LISTA\n5-APAGAR TODA LISTA")
        verificar = str(input(""))

        #1- LISTAR
        if verificar == "1":
            limpar()
            if not lista:
                print("LISTA VAZIA, NAO HÁ TAREFAS...\nENTER PARA VOLTAR")
                input("")
            else:
                print("LISTANDO...")
                listartarefa()
                input("Enter pra voltar")
            
        #2- ADICIONAR A LISTA
        elif verificar == "2":
            limpar()        
            print("O QUE VOCE DESEJA ADICIONAR")
            add = str(input("."))
            print("SUCESSO")
            lista.append(add)
            salvar(lista)
            input("ENTER PARA VOLTAR")

        #3- REMOVER DA LISTA
        elif verificar == "3":
            limpar()
            if not lista:
                print("LISTA VAZIA, NAO HÁ TAREFAS...\nENTER PARA VOLTAR")
                input("")
            else:
                print("QUAL TAREFA VOCE QUER APAGAR?\n")
                for i, tarefa in enumerate(lista, start=1):
                        print(f"{i}-{tarefa}")
                apagar = int(input())
                lista.pop(apagar - 1)
                salvar(lista)
                print("SUCESSO.")
                input("Enter pra voltar")

        #4- ATUALIZAR A LISTA
        elif verificar == "4":
            limpar()
            if not lista:
                print("LISTA VAZIA, NAO HÁ TAREFAS...\nENTER PARA VOLTAR")
                input("")
            else:
                print("QUAL TAREFA VOCE QUER CONCLUIR?")
                listartarefa()
                concluir = int(input())
                lista.insert(concluir - 1," - CONCLUIDO")
                lista.pop(concluir)
                salvar(lista)
                input("ENTER PARA VOLTAR")

        #5- APAGAR TODA LISTA
        elif verificar == "5":
            limpar()
            if not lista:
                print("LISTA VAZIA, NAO HÁ TAREFAS...\nENTER PARA VOLTAR")
                input("")
            else:
                print("VOCE TEM CERTEZA?\n*DIGITE SIM*\n*ENTER PARA CANCELAR*")
                sim = str(input(""))
                if sim.lower() == "sim":
                    limpar()
                    lista.clear()
                    salvar(lista)
                    print("SUCESSO. LISTA APAGADA.\nENTER PARA VOLTAR")
                    input("")
