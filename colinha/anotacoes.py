#BANCO DE DADOS
'''
CREATE TABLE usuario
(id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, nome_usuario VARCHAR(100) NOT NULL, telefone varchar(50) NOT NULL, endereco varchar(50) NOT NULL, cpf varchar(50) NOT NULL, email varchar(50));

CREATE TABLE livro
( id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
nome_livro VARCHAR(100) NOT NULL, status varchar(50) NOT NULL, id_categoria varchar(50) NOT NULL, id_editora varchar(50) NOT NULL,autor varchar(50) NOT NULL,
CONSTRAINT  fk_livro_categoria FOREIGN KEY (id_categoria)REFERENCES categoria(id_categoria),
CONSTRAINT fk_livro_editora FOREIGN KEY (id_editora)REFERENCES editora(id_editora));

CREATE TABLE categoria
( id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
nome_categoria VARCHAR(100) NOT NULL,genero varchar(50) NOT NULL);

CREATE TABLE editora
( id_editora INTEGER PRIMARY KEY AUTOINCREMENT,
nome_editora VARCHAR(100) NOT NULL);

CREATE TABLE multa
( id_multa INTEGER PRIMARY KEY AUTOINCREMENT,
nome_multa VARCHAR(100) NOT NULL, id_emprestimo varchar(50) NOT NULL
CONSTRAINT fk_multa_emprestimo FOREIGN KEY (id_emprestimo)REFERENCES emprestimo(id_emprestimo));

CREATE TABLE emprestimo
( id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
nome_emprestimo VARCHAR(100)NOT NULL, data emprestimo varchar(50) NOT NULL, data devolicao varchar(50) NOT NULL, id_usuario varchar(50) NOT NULL, id_livro varchar(50) NOT NULL
CONSTRAINT fk_emprestimo_usuario FOREIGN KEY (id_usuario)REFERENCES usuario(id_usuario),
CONSTRAINT fk_emprestimo_livro FOREIGN KEY (id_livro)REFERENCES livro(id_livro));
'''
'''


 Comandos SQL no SQLite

Categoria	                Comando            Descrição	                         Exemplo
Criar tabela	            CREATE TABLE	     Cria uma nova tabela	               CREATE TABLE clientes (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER);
Excluir tabela	          DROP TABLE	       Remove uma tabela existente	       DROP TABLE clientes;
Alterar tabela	          ALTER TABLE	       Adiciona ou renomeia colunas	       ALTER TABLE clientes ADD COLUMN email TEXT;
Inserir dados	            INSERT INTO	       Insere registros	                   INSERT INTO clientes (nome, idade) VALUES ('Ana', 30);
Selecionar dados         	SELECT	           Consulta registros	                 SELECT nome, idade FROM clientes;
Atualizar dados	          UPDATE	           Modifica registros existentes	     UPDATE clientes SET idade = 31 WHERE id = 1;
Excluir dados	            DELETE 	           Remove registros	                   DELETE FROM clientes WHERE id = 1;
Ordenar resultados       	ORDER BY	         Ordena resultados	                 SELECT * FROM clientes ORDER BY idade DESC;
Filtrar resultados	      WHERE	             Aplica condições	                   SELECT * FROM clientes WHERE idade > 25;
Limitar resultados	      LIMIT	             Restringe quantidade de linhas	     SELECT * FROM clientes LIMIT 5;
Relacionar tabelas	      JOIN	             Une dados de tabelas	               SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id;
Chave estrangeira	        FOREIGN KEY	       Define relacionamento	             FOREIGN KEY(cliente_id) REFERENCES clientes(id)
renomeia                  RENAME             renomeia tabelas



 Comandos internos do shell sqlite3
(Executados diretamente no terminal do SQLite, começam com ponto)

Comando          	   Descrição
.tables	             Lista todas as tabelas do banco
.schema	             Mostra a estrutura (DDL) das tabelas
.headers on/off	     Liga/desliga exibição de cabeçalhos
.mode column	       Formata saída em colunas
.databases	         Lista bancos de dados anexados
.quit	               Sai do SQLite



Comandos SQL no SQLite
Categoria                   Comando            Descrição                             Exemplo
Criar tabela                CREATE TABLE       Cria uma nova tabela                  CREATE TABLE clientes (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER);
Excluir tabela              DROP TABLE         Remove uma tabela existente           DROP TABLE clientes;
Alterar tabela              ALTER TABLE        Adiciona ou renomeia colunas          ALTER TABLE clientes ADD COLUMN email TEXT;
Inserir dados               INSERT INTO        Insere registros                      INSERT INTO clientes (nome, idade) VALUES ('Ana', 30);
Selecionar dados            SELECT             Consulta registros                    SELECT nome, idade FROM clientes;
Atualizar dados             UPDATE             Modifica registros existentes         UPDATE clientes SET idade = 31 WHERE id = 1;
Excluir dados               DELETE             Remove registros                      DELETE FROM clientes WHERE id = 1;
Ordenar resultados          ORDER BY           Ordena resultados                     SELECT * FROM clientes ORDER BY idade DESC;
Filtrar resultados          WHERE              Aplica condições                      SELECT * FROM clientes WHERE idade > 25;
Limitar resultados          LIMIT              Restringe quantidade de linhas        SELECT * FROM clientes LIMIT 5;
Relacionar tabelas          JOIN               Une dados de tabelas                  SELECT * FROM pedidos JOIN clientes ON pedidos.cliente_id = clientes.id;
Chave estrangeira           FOREIGN KEY        Define relacionamento                 FOREIGN KEY(cliente_id) REFERENCES clientes(id)
renomeia                    RENAME             renomeia tabelas
conta                       COUNT              conta resgistros                      SELECT COUNT(*) AS total_clientes FROM clientes;



Operadores comuns no WHERE
 
Operador	               Descrição	                            Exemplo
=	                       igualdade	                            WHERE idade = 30
<> ou !=	               Diferente	                            WHERE cidade <>'SãoPaulo'
> / < / >= / <=          Comparações numéricas                  WHERE salario > 3000
BETWEEN ... AND ...	     Intervalo	            	              WHERE idade BETWEEN 18 AND 30
IN (...)	               Lista de valores	                      WHERE estado IN ('SP', 'RJ', 'MG')
LIKE			               Correspondência com curingas (% e _)	  WHERE nome LIKE 'Jo%'
IS NULL / IS NOT NULL	   Valores nulos	                        WHERE telefone IS NULL
AND / OR	               Combinação de condições	              WHERE idade > 18 AND cidade = 'Rio'
 



Ordenação e Limite
Sql
 
SELECT nome, idade
FROM clientes
WHERE idade >= 18
ORDER BY idade DESC
LIMIT 5;
ORDER BY: ordena os resultados (ASC crescente, DESC decrescente).
LIMIT: limita o número de linhas retornadas.


 
Agrupamento com filtro (GROUP BY + HAVING)
Sql
 
SELECT cidade, COUNT(*) AS total
FROM clientes
GROUP BY cidade
HAVING COUNT(*) > 10;
GROUP BY: agrupa registros.
HAVING: filtra grupos (diferente de WHERE, que filtra linhas antes do agrupamento).
 


Exemplo completo
Sql
 
SELECT nome, idade, cidade
FROM clientes
WHERE idade BETWEEN 25 AND 40
  AND cidade IN ('São Paulo', 'Rio de Janeiro')
ORDER BY idade ASC
LIMIT 10 OFFSET 5;
 
OFFSET: pula as primeiras linhas (útil para paginação).



'''
#COMANDOS GIT HUB
"""
 # Inicializar um Repositório #

git init
Copiar
Este comando cria um novo repositório Git no diretório atual.

 # Clonar um Repositório #

git clone <URL>
Copiar
Clona um repositório remoto para o seu computador local.

 # verificar o Status #

git status
Copiar
Exibe o estado atual dos arquivos no repositório, como alterações não rastreadas ou preparadas.

 # Adicionar Arquivos à Área de Preparação # 

git add <arquivo>
git add
Copiar
Adiciona arquivos específicos ou todos os arquivos ao estágio de preparação para commit.

 # Fazer Commit das Alterações #

git commit -m "Mensagem do commit"
Copiar
Salva as alterações preparadas no histórico do repositório com uma mensagem descritiva.

 # Visualizar Histórico de Commits #

git log
Copiar
Mostra o histórico de commits do repositório.

 # Criar e Alternar Entre Branches #

git branch <nome-do-branch>
git checkout <nome-do-branch>
Copiar
Cria um novo branch e alterna para ele.

 # Mesclar Branches #

git merge <nome-do-branch>
Copiar
Mescla as alterações de outro branch no branch atual.

 # Enviar Alterações para o Repositório Remoto #

git push origin <branch>
Copiar
Envia os commits locais para o repositório remoto.

 # Atualizar o Repositório Local com Alterações Remotas #

git pull origin <branch>
Copiar
Baixa e mescla as alterações do repositório remoto no branch atual.


"""