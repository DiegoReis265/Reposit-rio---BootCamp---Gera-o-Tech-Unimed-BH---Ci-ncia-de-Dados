## Alguns comandos básicos para manipulação de diretórios e arquivos no Git:happy:

### Estados

* Modified (modificado)
* Staged/index (Preparado)
* Committed (Consolidado)



###  Para pedir ajuda 

git help



### Configuração

#### Setar email:

git config --global --unset user.email 

#### Registrar novo email:

git config --global user.email descrição@exemplo.br

#### Setar nome:

git config --global --unset user.name

#### Registrar novo nome:

git config --global user.name "nome"

#### Listar configurações:

git config --list



## Repositório Local

#### Criar novo repositório:

git init

#### Verificar estado dos arquivos/diretórios:

git status

#### Adicionar arquivo/diretório (staged area):

##### Adicionar todos os arquivos/diretórios

git add .

##### Adicionar um diretório em específico

git add meu_diretorio

##### Adicionar um arquivo em específico

git add meu_arquivo.txt



#### Comitar arquivo/diretório:

##### Comitar um arquivo:

git commit arquivo.txt

##### Comitar vários arquivos:

git commit arquivo.txt outro_arquivo.txt

##### Comitar informando mensagem:

git commit arquivo.txt -m "mensagem de commit"



#### Remover arquivo/diretório:

##### Remover arquivo:

git rm arquivo.txt

##### Remover diretório:

git rm -r diretorio



### Enviar arquivos/diretórios para o repositório remoto

##### O primeiro **push** de um repositório deve conter o nome do repositório remoto e o branch:

git push -u origin master

##### Os demais **pushes** não precisam dessa informação:

git push

### Atualizar repositório local de acordo com o repositório remoto

##### Atualizar os arquivos no branch atual:

git pull

##### Buscar as alterações, mas não aplica-las no branch atual:

git fetch

### Clonar um repositório remoto já existente

git clone https://github.com/usuariox/Repositoriox