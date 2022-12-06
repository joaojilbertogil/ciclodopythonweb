from  flask  import  Flask , render_template , request , redirect , url_for , session 
de  flask_mysqldb  importar  MySQL 
importar  MySQLdb . cursores 
importar  re 
  
  
app  =  Frasco ( __name__ )
  
  
app . secret_key  =  'sua senha'
  
  
app . config [ 'MYSQL_HOST' ] =  'localhost'
app . config [ 'MYSQL_USER' ] =  'raiz'
app . config [ 'MYSQL_PASSWORD' ] =  ''
app . config [ 'MYSQL_DB' ] =  'perfil'
  
  
mysql  =  MySQL ( aplicativo )
  
  
@ aplicativo . rota ( '/' ) 
@ aplicativo . rota ( '/login' , métodos  = [ 'GET' , 'POST' ]) 
 login definido ():
    msg  =  '' 
    se  solicitar . método  ==  'POST'  e  'nome de usuário'  na  solicitação . formulário  e  'senha'  no  pedido . formulário :
        nome de usuário  =  solicitação . formulário [ 'nome de usuário' ]
        senha  =  solicitação . formulário [ 'senha' ]
        cursor  =  mysql . conexão . cursor ( MySQLdb . cursors . DictCursor )
        cursor . execute ( 'SELECT * FROM contas WHERE nome de usuário = % s AND senha = % s' , ( nome de usuário , senha , ))
        conta  =  cursor . buscar ()
        se  conta :
            sessão [ 'conectado' ] =  Verdadeiro
            sessão [ 'id' ] =  conta [ 'id' ]
            sessão [ 'nome de usuário' ] =  conta [ 'nome de usuário' ]
            msg  =  'Logado com sucesso !'
            return  render_template ( 'index.html' , msg  =  msg )
        senão :
            msg  =  'Usuário ou senha incorreta !'
    return  render_template ( 'login.html' , msg  =  msg )
  
@ aplicativo . rota ( '/logout' ) 
 sair def ():
   sessão . pop ( 'conectado' , Nenhum )
   sessão . pop ( 'id' , Nenhum )
   sessão . pop ( 'nome de usuário' , nenhum )
    redirecionamento de retorno ( url_for ( 'login' ))
  
@ aplicativo . rota ( '/register' , métodos  = [ 'GET' , 'POST' ]) 
 registro def ():
    msg  =  '' 
    se  solicitar . método  ==  'POST'  e  'nome de usuário'  na  solicitação . formulário  e  'senha'  no  pedido . formulário  e  'e-mail'  no  pedido . formulário  e  'celular'  no  pedido . formulário  e  'cidade'  no  pedido . formulário  e  'estado'  no  pedido . formulário :
        nome de usuário  =  solicitação . formulário [ 'nome de usuário' ]
        senha  =  solicitação . formulário [ 'senha' ]
        e-mail  =  solicitação . formulário [ 'e-mail' ]
        celular  =  pedido . formulário [ 'celular' ]
        cidade  =  solicitação . formulário [ 'cidade' ]
        estado  =  pedido . formulário [ 'estado' ]
        cursor  =  mysql . conexão . cursor ( MySQLdb . cursors . DictCursor )
        cursor . execute ( 'SELECT * FROM contas WHERE nome de usuário = %s' , ( nome de usuário ,))
        conta  =  cursor . buscar ()
        se  conta :
            msg  =  'Conta já existe !'
        elif  não  re . match ( r'[^@]+@[^@]+\.[^@]+' , email ):
            msg  =  'Endereço de e-mail inválido !'
        elif  não  re . match ( r'[A-Za-z0-9]+' , nome de usuário ):
            msg  =  'Nome deve conter somente caracteres e números !'
        senão :
            cursor . execute ( 'INSERT INTO contas VALUES (NULL, %s, %s, %s, %s, %s, %s)' , ( nome de usuário , senha , e- mail , celular , cidade , estado ,))
            . _ conexão . cometer ()
            msg  =  'Você foi registrado com sucesso !'
     pedido de elif . método  ==  'POST' :
        msg  =  'Por favor, preencha todos os campos !'
    return  render_template ( 'register.html' , msg  =  msg )
  
  
@ aplicativo . rota ( "/index" ) 
 índice de definição ():
    se  'conectado'  na  sessão :  
        return  render_template ( "index.html" )
     redirecionamento de retorno ( url_for ( 'login' ))
  
  
@ aplicativo . rota ( "/view" ) 
 vista def ():
    se  'conectado'  na  sessão :
        cursor  =  mysql . conexão . cursor ( MySQLdb . cursors . DictCursor )
        cursor . execute ( 'SELECT * FROM contas WHERE id = %s' , ( sessão [ 'id' ], ))
        conta  =  cursor . buscar ()     
        return  render_template ( "view.html" , conta  =  conta )
     redirecionamento de retorno ( url_for ( 'login' ))
  
@ aplicativo . rota ( "/update" , métodos  = [ 'GET' , 'POST' ]) 
 atualização de definição ():
    msg  =  '' 
    se  'conectado'  na  sessão :
        se  solicitar . método  ==  'POST'  e  'nome de usuário'  na  solicitação . formulário  e  'senha'  no  pedido . formulário  e  'e-mail'  no  pedido . formulário  e  'endereço'  no  pedido . formulário  e  'cidade'  no  pedido . formulário  e  'país'  no  pedido . formulário  e  'código postal'  no  pedido . forma  e 'organização'  no  pedido . formulário :
            nome de usuário  =  solicitação . formulário [ 'nome de usuário' ]
            senha  =  solicitação . formulário [ 'senha' ]
            e-mail  =  solicitação . formulário [ 'e-mail' ]
            celular  =  pedido . formulário [ 'celular' ]
            cidade  =  solicitação . formulário [ 'cidade' ]
            estado  =  pedido . formulário [ 'estado' ]             
            cursor  =  mysql . conexão . cursor ( MySQLdb . cursors . DictCursor )
            cursor . execute ( 'SELECT * FROM contas WHERE nome de usuário = % s' , ( nome de usuário ,))
            conta  =  cursor . buscar ()
            se  conta :
                msg  =  'Conta já existe !'
            elif  não  re . match ( r'[^@]+@[^@]+\.[^@]+' , email ):
                msg  =  'Endereço de e-mail inválido !'
            elif  não  re . match ( r'[A-Za-z0-9]+' , nome de usuário ):
                msg  =  'Nome deve conter apenas caracteres e números !'
            senão :
                cursor . execute ( 'UPDATE contas SET nome de usuário =% s, senha =% s, e-mail =% s, celular =% s, cidade =% s, estado =% s, WHERE id =% s' , ( usuário , senha , e- mail , celular , cidade , estado , ( sessão [ 'id' ], ), ))
                . _ conexão . cometer ()
                msg  =  'Você comeu os dados com sucesso !'
         pedido de elif . método  ==  'POST' :
            msg  =  'Por favor, preencha todos os campos !'
        return  render_template ( "update.html" , msg  =  msg )
     redirecionamento de retorno ( url_for ( 'login' ))
  
se  __name__  ==  "__main__" :
    app . run ( host  = "localhost" , porta  =  int ( "5000" ))