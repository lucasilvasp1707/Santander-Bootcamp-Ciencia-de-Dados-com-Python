nome = ("  LUCas")

print(nome.upper(), "metodo upper ")
print(nome.lower(), 'metodo lower')
print(nome.title(), "metodo titulo")
print(nome.strip(), "metodo de tirar espaçamento")
print(nome.center(10,"#"), "metodo que centraliza")
print("_".join(nome), "metodo que add a cada caracter")

nome = "   Lucas   "
print(nome.strip() + "10")
print(nome.lstrip() + "10")
print(nome.rstrip()+ "10")