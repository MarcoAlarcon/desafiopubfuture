# programa_pub_future

Neste repositório se encontra meu código para o desafio do programa pubfuture promovido pela empresa Pública tecnologia.

<h1>Instruções</h1>

A linguagem utilizada no script para esse teste foi a linguagem python, então antes de prosseguir com o restante das intruções, verifique se o python esa instalado na sua máquina.
Se não tiver o python instalado na máquina, basta seguir este tutorial para instalar o python: https://www.youtube.com/watch?v=pDBnCDuL-dc
Após a instalação do python, abra ele e digite o comando: pip install-mysql-connector-python e pressione enter.

O banco de dados relacional usado para integração com o script, foi o MySQL, se não tiver MySQL instalado em sua máquina, vamos precisar instalar também.
Isso pode feito seguindo este tutorial: https://www.youtube.com/watch?v=fmerTu7dWk8

<h2>Após a instalação do Python e MySQL.</h2>

Baixe e extraia os arquivos deste repositório, fique atento para _deixar todos os arquivos na mesma pasta__.<br>
Feito isso abra seu MySQL Workbench e inicie uma nova conexão no botão "+" localizado ao lado de "MySQL Connections".<br>
Configure essa nova conexão normalmente, informando o nome da conexão e o usuário e se cadastrada, a senha, é importante manter em mente o usuário e a senha, se informada.<br>
Após criado, digitar a seguinte query: create database projeto_pubfuture.<br>
O próximo passo é ir até a aba "Administração" e no menu "Gerenciamento" selecionar Data Import/Restore<br>
A seguir selecione a opção "Import from Self-Contained File" e no botão de reticensias selecione o arquivo projeto_pubfuture.sql que foi baixado junto com os outros arquivos deste repositório.<br>
Em "Default Target Schema" selecione projeto_pubfuture e clique em Start Import, a segui uma imagem para auxiliar nesta parte:
![MySQL setup](https://imgur.com/a/pizMWjv)
Na tela seguinte se você tiver uma senha cadastra, informe-a, se não tiver nenhuma senha, basta clicar em ok.
Agora abra os arquivos index.py, receitas.py, despesas.py e contas.py no IDE de sua preferência.
Nos arquivos receitas, despesas e contas, existe a classe conexao no começo de cada arquivo, para acessar o banco de dados é necessario informar as credênciais nos campos host, user e password de cada arquivo.
Os campos host e password já vem setados como localhost e vazio respectivamente nesta ordem, __apenas altere os campos se o seu host do MySQL for cadastrado com um nome diferente e se você tiver uma senha cadastrada para acessar suas conexões no MySQL__.
A seguir uma imagem para auxiliar na identificação desse metodo de classe:
![Conexao setup](https://imgur.com/a/tjXb7JQ)

Seguindo esses passos, basta executar o script do arquivo index.py para acessar o sistema financeiro proposto no desafio.
Nele você encontrara instruições de como realizar operações CRUD no banco de dados.

Nota para o tester desse script:
  Este é meu segundo desafio para programas de capacitação e o primeiro desenvolvido na linguagem python. No desafio foi informado que era permitido o uso de libs para auxliar
  na construção do script, porém obtei por não usar para tirar máximo proveito da linguagem e o que ela tem a oferecer, e também para servir de termometro para a questão de 
  dominio na linguagem, fiquei muito feliz com o resultado e com o tanto de conhecimento que esse desafio trouxe, espero que gostem! 
