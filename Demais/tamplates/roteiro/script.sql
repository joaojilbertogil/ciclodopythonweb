/* Criação da base de dados do perfil   */
CRIAR BANCO DE  DADOS  SE NÃO EXISTIR perfil CONJUNTO DE CARACTERES PADRÃO utf8
    COLLATE utf8_general_ci;

/* Definição da base de dados padrão */
USE perfil;

/* Criação da tabela de contas */
CRIAR  TABELA  SE NÃO EXISTIR contas (
    id int ( 6 ) NÃO NULL AUTO_INCREMENT,
    Usuário varchar ( 50 ) NOT NULL ,
varchar ( 255 ) NÃO NULL     senha ,
    E-mail varchar ( 100 ) NÃO NULO ,
    Celular varchar ( 20 ) NÃO NULO ,
    Cidade varchar ( 60 ) NÃO NULO ,
    Estado varchar ( 40 ) NOT NULL ,
    CHAVE PRIMÁRIA (id)
);
