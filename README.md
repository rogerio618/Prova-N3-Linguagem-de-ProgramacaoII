# Prova-N3-Linguagem-de-ProgramacaoII

Este script é a instância baseda em Python Flask REST API MongoDB CRUD. 
Definição de todos as URIs REST para executar operações CRUD.
Também consulta o servidor de banco de dados MongoDB para ler, inserir, atualizar, listar por Id e excluir.
Usei os métodos http GET, POST, PUT e DELETE no Postman para buscar, criar, atualizar, listar e excluir usuários do ou para o MongoDB.
Defini apenas o método 404 para lidar com o erro não encontrado. 
Aqui tenho que  lidar com os erros necessários, como erros do servidor para respostas http 500, ocorridos durante as chamadas API REST.
Usei a biblioteca BSON para convertes em JSON usando o bson.json_utilmódulo para evitar erros de serialização.
