s = input('Digite qualquer coisa: ')
print('Tipo do valor é: {} \nÉ um numeral? {} \nÉ alfabético? {} \nÉ um alfanumérico? {} '
'\nFaz parte do ASCII? {}\nEstá em upper?{} \nEstá em lower? {} \nPode ser um identificador válido? {} \nÉ um dígito? {} \nSó tem espaços? {} \nEstá capitalizada? {}'.
      format(type(s), s.isnumeric(), s.isalpha(), s.isalnum(), s.isascii(), s.isupper(), s.islower(), s.isidentifier(), s.isdigit(), s.isspace(), s.istitle()))
