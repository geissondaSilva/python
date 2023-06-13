create table if not exists pessoa(
    id serial primary key,
    nome varchar(100),
    cpf varchar(11)
);