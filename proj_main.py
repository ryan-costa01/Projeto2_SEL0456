"""
Module providing a function printing python version.
SEL0456 - Desenvolvimento de Software Livre
Arquivo MAIN do Trabalho 2
Author: Ryan Fellipe Silva Costa - ryanfellipe2001@usp.br
n°USP: 11953369
"""
import hashlib
import os
import pickle

# Definição da classe referente ao usuário
class Usuario:
    """"Definição da classe referente ao usuário"""
    def __init__(self, nome, senha, hierarquia):
        self.nome = nome
        self.hierarquia = hierarquia
        self.salt = os.urandom(16)  # Gerar um valor de "salt" aleatório
        self.hash_senha = self._hash_senha(senha)

    def _hash_senha(self, senha):
        """Criar um hash a partir da senha e do 'salt'"""
        senha_concatenada = senha.encode('utf-8') + self.salt
        hash_obj = hashlib.sha256(senha_concatenada)
        return hash_obj.hexdigest()

    def verificar_senha(self, senha_inserida):
        """Verificar se a senha inserida corresponde ao hash armazenado"""
        senha_hash_inserida = self._hash_senha(senha_inserida)
        return senha_hash_inserida == self.hash_senha
    def __str__(self):
        return self.__class__.__name__

# Imprime os usuários salvos
def __str__(self):
    """Imprime os usuários salvos"""
    return f"Nome: {self.nome} Hierarquia: {self.hierarquia}"

# Lista para armazenar usuários
usuarios = []

# Função para adicionar um novo usuário à lista
def adicionar_usuario(nome, senha, hierarquia):
    """Função para adicionar um novo usuário à lista"""
    novo_usuario = Usuario(nome, senha, hierarquia)
    usuarios.append(novo_usuario)

# Função para verificar e retornar um usuário existente
def obter_usuario_por_nome(nome):
    """Função para verificar e retornar um usuário existente"""
    for usuario in usuarios:
        if usuario.nome == nome:
            return usuario
    return None

# Função para validar hierarquia escolhida"""
def select_hierarquia(nome_usuario, senha_inserida, op_hierarquia):
    """Função para validar hierarquia escolhida"""    
    while True:

        if op_hierarquia in ('a', 'b', 'c'):

            if op_hierarquia == 'a':
                hierarquia = 'MasterAdmin'
            elif op_hierarquia == 'b':
                hierarquia = 'Admin'
            elif op_hierarquia == 'c':
                hierarquia = 'Padrão'

            adicionar_usuario(nome_usuario, senha_inserida, hierarquia)

            break
        print("Hierarquia inválida. ")
        print("As hierarquias válidas são 'MasterAdmin', 'Admin' e 'Padrão'.")
        op_hierarquia = input('Tente novamente:')

# Função para analisar o nome de usuário
def analisar_nome(nome):
    """"Função para analisar o nome de usuário"""
    while not nome.isalpha():
        nome = input("Nome Inválido (Não utilize espaço nem caracteres especiais):")
    return nome

# Função para salvar usuários em um arquivo
def salvar_usuarios():
    """"Função para salvar usuários em um arquivo"""
    with open('usuarios.pkl', 'wb') as arquivo:
        pickle.dump(usuarios, arquivo)

# Função para carregar usuários de um arquivo
def carregar_usuarios():
    """Função para carregar usuários de um arquivo"""
    try:
        with open('usuarios.pkl', 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return []

# Carregar usuários do arquivo (se existir)
usuarios = carregar_usuarios()

# Menu de opções
def menu():
    """"Menu de opções"""
    while True:
        print("Opções:")
        print("1. Adicionar novo usuário")
        print("2. Usar usuário existente")
        print("3. Usuários exixtentes")
        print("4. Fechar Programa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome de usuário: ")
            nome_usuario = analisar_nome(nome)
            senha_inserida = input("Digite a senha: ")
            op_hierarquia = input("Selecione a hierarquia:\na.MasterAdmin\nb.Admin\nc.Padrão\n\nDigite 'a','b' ou 'c': ")
            select_hierarquia(nome_usuario, senha_inserida, op_hierarquia)
            salvar_usuarios()
            print("Usuários salvos com sucesso.")
        elif opcao == "2":
            while True:
                nome = input("Digite o nome de usuário: ")
                nome_usuario = analisar_nome(nome)
                senha_inserida = input("Digite a senha: ")
                usuario = obter_usuario_por_nome(nome_usuario)
                if usuario and usuario.verificar_senha(senha_inserida):
                    print("Senha correta para o usuário", usuario.nome)
                    print("Hierarquia:", usuario.hierarquia)
                    
                    break
                print("Senha incorreta ou usuário não encontrado.\n")
                sim_nao = input("Quer tentar novamente?(s/n):")
                if sim_nao == "n":
                    break
                
        # Imprimir informações dos usuários
        elif opcao == "3":
            print("Usuários existentes:")
            for usuario in usuarios:
                print(f"Nome: {usuario.nome}, Hierarquia: {usuario.hierarquia}")
        
        # Fechar Programa
        elif opcao == "4":
            exit(0)
        
        # Mensagem de Erro em Caso de Entrada errada
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso:
menu()

# End-of-file (EOF)