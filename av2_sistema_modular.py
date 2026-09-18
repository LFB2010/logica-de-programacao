# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: 
# Data: 
# Link do Repositório: 
# ==============================================================================

# Lista inicial de dados brutos (Exemplo: Sistema de RH / Atendimento)
# Os dados estão no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
   "  carlos eduardo silva;desenvolvedor;11988887777  ",
   "  ana paula mendes;analista de rh;21977776666  ",
   "  roberto carlos oliveira;gerente de projetos;31966665555  "
]


# ------------------------------------------------------------------------------
# 1. FUNÇÕES DO SISTEMA (Mínimo de 3 funções)
# ------------------------------------------------------------------------------

def limpar_e_formatar_texto(texto):
   """
   FUNÇÃO 1:
   - Recebe uma string.
   - Remove espaços extras das pontas (.strip()).
   - Converte o texto para letras MAIÚSCULAS (.upper()).
   - Retorna o texto devidamente formatado.
   """
   return texto.strip().upper()


def extrair_codigo_ou_ddd(dado):
   """
   FUNÇÃO 2:
   - Recebe um dado em formato de string (ex: telefone ou CPF).
   - Remove espaços das pontas.
   - Utiliza fatiamento de string [x:y] para extrair os 2 primeiros dígitos (ex: DDD).
   - Retorna apenas os dígitos extraídos.
   """
   dado_limpo = dado.strip()
   return dado_limpo[0:2]


def processar_e_exibir_cadastros(lista_dados):
   """
   FUNÇÃO 3:
   - Recebe a lista de cadastros brutos como parâmetro.
   - Utiliza um laço FOR para percorrer cada item da lista.
   - Em cada iteração:
       1. Separa as partes usando .split(";")
       2. Chama a Função 1 para formatar o Nome e o Cargo.
       3. Chama a Função 2 para extrair o DDD/Código do telefone.
       4. Exibe o resultado final formatado na tela com f-string.
   - Retorna a quantidade total de registros processados.
   """
   contador = 0
   for registro in lista_dados:
       partes = registro.split(";")
       nome = limpar_e_formatar_texto(partes[0])
       cargo = limpar_e_formatar_texto(partes[1])
       telefone = partes[2].strip()
       ddd = extrair_codigo_ou_ddd(telefone)

       print(f"Nome: {nome} | Cargo: {cargo} | Telefone: {telefone} | DDD: {ddd}")
       contador += 1

   return contador


# ------------------------------------------------------------------------------
# 2. PROGRAMA PRINCIPAL (FLUXO DE EXECUÇÃO)
# ------------------------------------------------------------------------------

def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")

   print("Iniciando o processamento dos dados...\n")

   # Chamada da Função 3 passando a lista 'dados_brutos'
   total_processado = processar_e_exibir_cadastros(dados_brutos)

   # Mensagem final mostrando a quantidade total de registros processados
   print(f"\nTotal de registros processados: {total_processado}")

   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")


# Execução do programa
if __name__ == "__main__":
   main()
