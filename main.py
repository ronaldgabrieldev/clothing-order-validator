def escolha (): #Função para terminar o valor unitário de acordo com o modelo de camiseta 
   while True: 
     print('Escolha o modelo desejado')
     print('MCS - MANGA CURTA SIMPLES')
     print('MLS - MANGA LONGA SIMPLES')
     print('MCE - MANGA CURTA COM ESTAMPA')
     print('MLE - MANGA LONGA COM ESTAMPA')
     mod = input('>>').strip().upper()
     if mod not in ['MCS', 'MLS', 'MCE', 'MLE']:
            print('Escolha inválida. Por favor, escolha um modelo válido.')
            print()
            continue
     else:
        if mod == 'MCS':
            preco = 1.80
            return preco
        elif mod == 'MLS':    
            preco = 2.10
            return preco
        elif mod == 'MCE':
            preco = 2.80
            return preco 
        else:
            if mod == 'MLE':
               preco = 3.20
               return preco
            
def num_camisetas(): # Função que solicita a quantidade de camisetas e aplica desconto 
    while True:
        try:
            num = int(input('Digite o número de camisetas: '))
            if num <= 0:
                print('Por favor, entre com um número de camisetas novamente.')
                print()
                continue
            elif num > 20000:
                print('Não aceitamos tantas camisetas de uma vez')
                print('Por Favor, entre com o número de camisetas novamente.')
                print()
                continue
            else:
               if num < 20:
                  num = int(num) 
                  return num 
               elif num >= 20 and num < 200:
                 num = int(num * 0.95)
                 return num
               elif num >= 200 and num < 2000:
                num = int(num * 0.93)    
               elif num >= 2000 and num <= 20000:
                  num = int(num * 0.88)
                  return num

        except ValueError:
           print('Digite um quantidade válida de camisetas.')
           print()
           continue           

def frete (): #Função para escolher o tipo de frete
    while True:
      print('Escolha o tipo de frete')
      print('1 - Frete por transportadora - R$ 100,00')
      print('2 - Frete por Sedex - R$ 200,00')
      print('0 - Retirar pedido na fábrica - R$ 0,00')
      fre = int(input('>>'))
      if fre == 1:
        return 100.00
      elif fre == 2:
        return 200.00
      elif fre == 0:
        return 0.00
      else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
        continue

# Programa principal
print('Bem-vindo à loja de camisetas do Ronald Gabriel Costa Silva!')
print()
modelo = escolha()
print()
qtd = num_camisetas()
print()
freteValor = frete()

Total = (modelo * qtd) + freteValor        
print(f'Total: {Total:.2f} (Modelo: {modelo} * Quantidade (com desconto):{qtd} + frete: {freteValor})')
