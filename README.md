<a name="readme-top"></a>


# Projeto2 SEL0456
Segundo projeto da matéria SEL0456 - Técnicas em Desenvolvimento de Software Livre.

Este é um sistema de gerenciamento de usuários em Python, onde você pode adicionar e verificar informações de usuários, incluindo nome, senha e hierarquia. 

## :rocket: Rodando o projeto

1. Clone o repositório
   ```sh
   git clone git@github.com:ryan-costa01/Projeto2_SEL0456.git
   ```
2. Inicialize o programa
   ```cmd
   python proj_main.py
   ```
   
## :wrench: Explicação do programa
### Menu de Opções
Ao inicializar o programa, o usuário deverá inserir um número inteiro entre 1 e 4, onde cada número representa uma função do programa.
```
1. Adicionar novo usuário
```
Você pode adicionar um novo usuário inserindo seu nome, senha e escolhendo sua hierarquia. O nome deve conter apenas letras (um nome simples, sem espaços e caracteres especiais).
As hierarquias válidas são 'MasterAdmin', 'Admin' e 'Padrão'. O programa utiliza a biblioteca pickle para salvar os usuários em um arquivo `usuario.pkl` e carregá-los posteriormente.
```
2. Usar usuário existente
```
Você pode verificar a senha de um usuário existente inserindo seu nome e senha. Se a senha estiver correta, o programa exibirá as informações do usuário.
```
3. Usuários existentes
```
Esta opção permite visualizar a lista de todos os usuários cadastrados. Ela imprime o nome e a hierarquia de cada usuário.
```
4. Fechar Programa
```
Esta opção fecha o programa.

### Funcionalidades Adicionais
O programa verifica se a hierarquia escolhida é válida (MasterAdmin, Admin ou Padrão) ao adicionar um novo usuário.

O programa salva os usuários em um arquivo chamado `usuarios.pkl` e carrega os usuários do arquivo quando o programa é iniciado.

O programa verifica se o nome inserido ao adicionar um novo usuário atende aos requisitos (contém apenas letras, sem espaços).


Certifique-se de que o arquivo `usuarios.pkl` esteja na mesma pasta que o código quando você o executar.

Este é um sistema simples de gerenciamento de usuários que pode ser usado como base para projetos mais avançados. 
## :memo: License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

## :handshake: Colaboradores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/ryan-costa01">
        <img src="https://avatars.githubusercontent.com/u/63657064?s=400&u=cae3d15c188ed977d1713fb373a5a42a145ae3ba&v=4" width="100px;" alt="Foto de Ryan Costa no GitHub"/><br>
        <sub>
          <b>Ryan Costa</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
