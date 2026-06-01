/* Criação das tabelas */
CREATE TABLE clientes (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	telefone VARCHAR(20),
	email VARCHAR(100)
);

CREATE TABLE flores (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	preco NUMERIC(10,2) NOT NULL,
	estoque INT NOT NULL
);

CREATE TABLE pedidos (
	id SERIAL PRIMARY KEY,
	cliente_id INT REFERENCES clientes(id),
	flor_id INT REFERENCES flores(id),
	quantidade INT,
	data_pedido DATE
);

/* Inserindo na tabela clientes os dados iniciais */
INSERT INTO clientes (nome, telefone, email)
VALUES
('Maria Helloísa', '(84)99999-0001', 'mariahelloisa@email.com'),
('Katielly', '(84)99999-0002', 'katielly@email.com'),
('Vivi Melo', '(84)99999-0003', 'vivimelo@email.com'),
('Ytalo Gabriel', '(84)99999-0004', 'ytalo@email.com'),
('João Felipe', '(84)99999-0005', 'joaofelipe@email.com');

/* Inserindo na tabela flores os dados iniciais */
INSERT INTO flores (nome, preco, estoque)
VALUES
('Margarida', 8.50, 40),
('Lirio', 15.00, 25),
('Tulipa', 12.50, 30),
('Rosa', 10.00, 50),
('Girassol', 9.00, 35);

/* Inserindo na tabela pedidos os dados iniciais */
INSERT INTO pedidos (cliente_id, flor_id, quantidade, data_pedido)
VALUES
(1, 1, 4, '2026-07-01'),
(2, 4, 5, '2026-06-02'),
(3, 3, 1, '2026-04-03'),
(4, 5, 3, '2026-06-04'),
(5, 2, 2, '2026-08-05');