# api-treinamento - AWS Auto Scaling

===========================
2 - AMBIENTE APP - EC2

	Preparar o ambiente

	yes | sudo yum update
	yes | sudo yum install git
	sudo yum install nodejs npm —-enablerepo=epel

	sudo npm install -g vtop

	git clone https://github.com/jonathanbaraldi/api-treinamento.git

========================================================
3 - BANCO DE DADOS  - CRIAÇÃO TABELA - RDS - MYSQL
	
	Após terminar a configuração acima dentro da EC2, agora iremos fazer a conexão com o banco de dados e criar a tabela que iremos usar. Conexão no banco direto da EC2 para criação das tabelas
	
	# Instalar o CLI do mysql no linux com 

	yes | sudo yum install mysql

	mysql -u DBUSER -h DBSERVERNAME -p

	
	mysql>    CREATE DATABASE books;
	mysql>    CREATE TABLE books.book ( id MEDIUMINT NOT NULL AUTO_INCREMENT, BookName VARCHAR(100), AuthorName VARCHAR(100), Price VARCHAR(10), PRIMARY KEY (id));

	# Apensas para testar se está inserindo os registros corretamente 
	# mysql>   INSERT INTO books.book VALUES (1,”My first autoscalling app”,”YourName","12");
	#

	mysql> exit

-------------------------------------------------------

@BaraldiJonathan
