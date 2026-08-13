email = input("Digite seu e-mail institucional: ")

primeiro_nome = email[:email.index(".")]
dominio = email[email.index("@") + 1:]

print(f"Primeiro nome:, {primeiro_nome}")
print(f"Domínio:, {dominio}")