usuario = input("Usuário: ").lower()
senha = int(input("Senha: "))
idade = int(input("Digite sua idade"))

if usuario == "admin" and senha == 123 and idade >= 18:
    print("Acesso permitido")
elif idade < 18:
    print(f"Menor de idade, {idade} anos, acesso negado")
else:
    print("Acesso negado")