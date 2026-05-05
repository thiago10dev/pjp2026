print("---------------------------".center(60))
print("BEM VINDO".center(60))
print("---------------------------".center(60))
tentativas=0
senha = ''
usuario= ''
texto1=" LOGIN FEITO COM SUCESSO "
enchimento1="_"
 
while ( senha!= "senha123" and usuario!= "peixe dourado") and tentativas<= 2:   
    tentativas = tentativas + 1
    senha =input("digite a senha correta:")
    usuario= input("digite o usuario correto:")
    tentativas >2
    print("---------------------------".center(60))
if senha == "senha123" and usuario!= "peixe dourado":
  print("usuario incorreto")
 
elif senha != "senha123" and usuario== "peixe dourado":
  print("senha incorreta")
 
elif senha == "senha123" and usuario == "peixe dourado":
  print(texto1.center(60,enchimento1))
 
elif tentativas==3:
  print ("aguarde 30 minutos antes de tentar novamente!")
 
if senha == "senha123" and usuario == "peixe dourado":
 pergunta= str(input("digite o que deseja no sistema: "))
lista_de_veiculos=["chevrolet s10" , "ford raptor" , "volkswagen amarok" , "dogderam 2500"]
lista_de_pedidos=["corvette c6","chevrolet camaro" ,"ford mustang","porsche gt3 rs" ]
while pergunta != "sair" :
 
   match pergunta:
 
    case "ver lista de veiculos":
     print("---------------------------".center(60))
     print("\n".join (lista_de_veiculos))
     print("---------------------------".center(60))
     pergunta=str(input("digite o que deseja a seguir: "))
    case "ver lista de pedidos":
     print("---------------------------".center(60))
     print("\n".join (lista_de_pedidos))
     print("---------------------------".center(60))
     pergunta=str(input("digite o que deseja a seguir: "))
 
    case  "editar lista de veiculos":
     print("---------------------------".center(60))
     edicao_veiculos=str(input("voçê quer adicionar veiculos ou excluir da lista? :"))
 
     match edicao_veiculos:
        case "adicionar":
         print("---------------------------".center(60))
         edicao_veiculos=str(input("digite o veiculo a ser adicionado: "))
         lista_de_veiculos.extend([edicao_veiculos])
         print("VEICULO ADICIONADO COM SUCESSO!".center(60))
         print("---------------------------".center(60))
         pergunta=str(input("digite o que deseja a seguir: "))
 
        case "excluir":
         print("---------------------------".center(60))
         edicao_veiculos=int(input("digite a posição do veiculo a ser excluido: "))
         lista_de_veiculos.pop(edicao_veiculos)
         print("VEICULO EXCLUIDO COM SUCESSO!".center(60))
         print("---------------------------".center(60))
         pergunta=str(input("digite o que deseja a seguir: "))
    case  "editar lista de pedidos":
     edicao_pedidos=str(input("voçê quer adicionar pedidos ou excluir da lista? :"))
 
     match edicao_pedidos:
        case "adicionar":
         print("---------------------------".center(60))
         edicao_pedidos=str(input("digite o pedido a ser adicionado: "))
         lista_de_pedidos.extend([edicao_pedidos])
         print("PEDIDO ADICIONAR COM SUCESSO!".center(60))
         print("---------------------------".center(60))
         pergunta=str(input("digite o que deseja a seguir: "))
 
        case "excluir":
         print("---------------------------".center(60))
         edicao_pedidos=int(input("digite a posição do pedido a ser excluido: "))
         lista_de_pedidos.pop(edicao_pedidos)
         print("PEDIO EXCLUIDO  COM SUCESSO!".center(60))
         print("---------------------------".center(60))
         pergunta=str(input("digite o que deseja a seguir: "))
 
    case _:
     print("---------------------------".center(60))
     print("está opção não é valida!")
     print("---------------------------".center(60))
     pergunta=str(input("digite o que deseja a seguir: "))
 
texto2=" VOÇÊ SAIU DO SISTEMA "
enchimento2="_"
print(texto2.center(60,enchimento2))
 