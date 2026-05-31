/* Criação das tabelas  */
create table clientes (
	id serial primary key,
	nome varchar(100) not null,
	telefone varchar(20),
	email varchar(100)
);

create table flores (
	id serial primary key,
	nome varchar(100) not null, 
	preco numeric(10,2) not null, 
	estoque int not null
);

create table pedidos (
	id serial primary key,
	cliente_id int references clientes(id), 
	flor_id int references flores(id),
	quantidade int, 
	data_pedido date
);


/* Inserindo na tabela clientes os dados iniciais */
INSERT INTO clientes (id, nome, telefone, email)
VALUES
(1, 'Maria Helloísa', '(84)999990-0001', 'mariahelloisa@email.com'),
(2, 'Katielly', '(84)99999-0002', 'katielly@email.com'),
(3, 'Vivi Melo', '(84)99999-0003', 'vivimelo@email.com'),
(4, 'Ytalo Gabriel', '(84)99999-0004', 'ytalo@email.com'),
(5, 'João Felipe', '(84)99999-0005', 'joaofelipe@email.com');

/* Inserindo na tabela flores os dados iniciais */
INSERT INTO flores (id, nome, preco, estoque)
VALUES
(1, 'Margarida', 8.50, 40),
(2, 'Lirio', 15.00, 25),
(3, 'Tulipa', 12.50, 30),
(4, 'Rosa', 10.00, 50),
(5, 'Girassol', 9.00, 35);


/* Inserindo na tabela pedidos os dados iniciais */
INSERT INTO pedidos (id, cliente_id, flor_id, quantidade, data_pedido)
VALUES
(1, 1, 1, 4, '2026-07-01'),
(2, 2, 4, 5, '2026-06-02'),
(3, 3, 3, 1, '2026-04-03'),
(4, 4, 5, 3, '2026-06-04'),
(5, 5, 2, 2, '2026-08-05');