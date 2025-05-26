import csv
import os

# --- Nomes dos arquivos que o programa vai usar ---
ARQUIVO_USUARIOS = 'usuarios.csv'
ARQUIVO_TABELA = 'tabela_imc.csv'
ARQUIVO_INSTRUCOES = 'instrucoes.txt'

def limpar_tela():
    """Função para limpar o terminal, funciona em Windows, Linux e macOS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_dados_usuario():
    """Pede nome, peso e altura ao usuário."""
    # Variável ajustada para nome_usuario
    nome_usuario = input("Qual é o seu nome? ")
    
    while True:
        try:
            peso_str = input("Qual seu peso (em KG)? ")
            altura_str = input("Qual sua altura (em metros e usando ponto)? ")

            peso = float(peso_str)
            altura = float(altura_str)

            if peso > 0 and altura > 0:
                # Retorna a variável ajustada
                return nome_usuario, peso, altura
            else:
                print("\nDados Inválidos: Peso e altura devem ser maiores que zero.")
        except ValueError:
            print("\nDados Inválidos: Por favor, digite apenas números para peso e altura.")
        
        continuar = input("Pressione [C] para tentar novamente ou [S] para sair: ").upper()
        if continuar != 'C':
            return None, None, None

def calcular_imc(peso, altura):
    """Calcula o IMC com base no peso e altura."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Verifica em qual faixa o IMC se encaixa e retorna o id_Registro."""
    if imc < 18.5:
        return 1
    elif imc < 25:
        return 2
    elif imc < 30:
        return 3
    else:
        return 4

def gravar_usuario(nome_usuario, peso, altura, imc, id_registro):
    """Insere um novo registro no arquivo de usuários."""
    try:
        with open(ARQUIVO_USUARIOS, 'a', newline='', encoding='utf-8') as arquivo:
            escritor_csv = csv.writer(arquivo, delimiter=';')
            # Usa a variável ajustada ao escrever no arquivo
            escritor_csv.writerow([nome_usuario, f"{peso:.2f}", f"{altura:.2f}", f"{imc:.2f}", id_registro])
    except FileNotFoundError:
        print(f"Erro: O arquivo '{ARQUIVO_USUARIOS}' não foi encontrado.")

def mostrar_resultados(nome_usuario, peso, altura, imc, id_registro):
    """Limpa a tela e exibe os resultados completos para o usuário."""
    limpar_tela()
    
    print("--- RESULTADO DO SEU IMC ---")
    # Usa a variável ajustada para mostrar o nome
    print(f"☑ Nome: {nome_usuario}")
    print(f"☑ Peso: {peso:.2f} kg")
    print(f"☑ Altura: {altura:.2f} m")
    print(f"☑ IMC: {imc:.2f} kg/m²")
    print("-" * 30)
    
    try:
        with open(ARQUIVO_TABELA, 'r', encoding='utf-8') as arquivo:
            leitor_csv = csv.DictReader(arquivo, delimiter=';')
            for linha in leitor_csv:
                if int(linha['id_registro']) == id_registro:
                    print(f"Faixa de IMC: {linha['faixa_imc']}")
                    print(f"Classificação: {linha['classificacao']}")
                    print(f"\nSugestões de Atividades Físicas:\n{linha['sugestoes_atividades']}")
                    print(f"\nSugestões Alimentares:\n{linha['sugestoes_alimentares']}")
                    break
    except FileNotFoundError:
        print(f"Erro: O arquivo '{ARQUIVO_TABELA}' não foi encontrado.")
        return
        
    print("\n" + "-" * 30)
    try:
        with open(ARQUIVO_INSTRUCOES, 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print(f"Erro: O arquivo '{ARQUIVO_INSTRUCOES}' não foi encontrado.")

# --- Programa Principal ---
print("--- Bem vindo a Calculadora de IMC Avançada ---")

while True:
    # Recebe a variável com o nome ajustado
    nome_usuario, peso, altura = obter_dados_usuario()

    if nome_usuario is None:
        break

    imc = calcular_imc(peso, altura)
    id_registro = classificar_imc(imc)
    
    gravar_usuario(nome_usuario, peso, altura, imc, id_registro)
    
    mostrar_resultados(nome_usuario, peso, altura, imc, id_registro)

    print("\n" + "=" * 30)
    continuar = input("\nPressione [C] para calcular novamente ou qualquer outra tecla para sair: ").upper()
    if continuar != 'C':
        break

print("\nObrigado por usar a Calculadora de IMC. Até a próxima!")