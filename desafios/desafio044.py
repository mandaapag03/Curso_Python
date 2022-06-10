print('=' * 15 + ' LOJINHA ' + '=' * 15)
produto = input('Informe o valor bruto do produto: R$ ')
if ',' in produto or (',' in produto and '.' in produto):
      produto = produto.replace('.', '_')
      produto = produto.replace(',', '.')
produto = float(produto)
while True:
      print('Selecione a forma de pagamento:\n'
            '1 - à vista dinheiro/cheque\n2 - à vista no cartão\n3 - até 2x no cartão\n4 - 3x ou mais no cartão')
      opcao = int(input('--> '))
      if opcao in range(1, 5):
            if opcao == 1:
                  preco = produto - (produto * 0.10)
                  print('Você irá pagar com 10% de desconto!')
                  print(f'Valor a pagar: R$ {preco:.2f}')
            elif opcao == 2:
                  preco = produto - (produto * 0.05)
                  print('Você irá pagar com 5% de desconto!')
                  print(f'Valor a pagar: R$ {preco:.2f}')
            elif opcao == 3:
                  print(f'Valor a pagar: R$ {produto:.2f}')
            else:
                  preco = produto + (produto * 0.20)
                  total_parcelas = int(input('Quantidade de parcelas: '))
                  print('Você irá pagar com juros de 20%...')
                  print(f'Valor total da compra: R$ {preco:.2f}')
                  preco = preco/total_parcelas
                  print(f'Valor a pagar por parcela: R$ {preco:.2f}')
            break
      else:
            print('Escolha uma opcao válida!')
