create table titular_pseudonimo
(
    id             integer      not null  primary key autoincrement,
    pseudonimo     varchar(200),
    is_principal   bool         not null,
    dt_inclusao    datetime     not null,
    dt_alteracao   datetime,
    owner_id       integer      references auth_user,
    cod_pseudo_mdb integer
);

create index titular_pseudonimo_owner_id_32bd3c4c
    on titular_pseudonimo (owner_id);



-- auto-generated definition
create table titular_titular
(
    id               integer      not null  primary key autoincrement,
    owner_id         integer      references auth_user,
    tp_cpf           varchar(50)  not null,
    tp_pessoa        varchar(50)  not null,
    estado_civil     varchar(50),
    cod_ecad         integer
        unique,
    nome_razao       varchar(200) not null,
    fantasia         varchar(200),
    cpf              varchar(14),
    cnpj             varchar(18),
    rg               varchar(13),
    ifpi             varchar(3),
    radical_ifpi     varchar(2),
    insc_estadual    varchar(30),
    insc_municipal   varchar(30),
    orgao_emissor    varchar(10),
    profissao        varchar(50),
    nacionalidade    varchar(50)  not null,
    dt_inclusao      datetime     not null,
    dt_alteracao     datetime,
    dt_nascimento    date,
    is_master        bool         not null,
    is_editora       bool         not null,
    is_produtor_fono bool         not null,
    is_interprete    bool         not null,
    is_musico        bool         not null,
    is_deleted       bool         not null,
    observacao       text,
    enderecos_id     integer     references titular_endereco,
    sociedades_id    integer     references titular_sociedade,
    sexo             varchar(50)  not null,
    is_autor         bool         not null,
    cod_titular_mdb  integer,
    email            varchar(254),
    pais             varchar(50)
);

create index titular_titular_13b7631e
    on titular_titular (sociedades_id);

create index titular_titular_5e7b1936
    on titular_titular (owner_id);

create index titular_titular_7489a7a1
    on titular_titular (enderecos_id);



-- auto-generated definition
create table titular_titular_pseudos
(
    id            integer not null    primary key  autoincrement,
    titular_id    integer not null    references titular_titular,
    pseudonimo_id integer not null    references titular_pseudonimo,
    unique (titular_id, pseudonimo_id)
);

create index titular_titular_pseudos_6245cb07
    on titular_titular_pseudos (pseudonimo_id);

create index titular_titular_pseudos_96c9b8a9
    on titular_titular_pseudos (titular_id);

-- auto-generated definition
create table titular_pseudonimo
(
    id             integer  not null    primary key autoincrement,
    pseudonimo     varchar(200),
    is_principal   bool     not null,
    dt_inclusao    datetime not null,
    dt_alteracao   datetime,
    owner_id       integer             references auth_user,
    cod_pseudo_mdb integer
);

create index titular_pseudonimo_owner_id_32bd3c4c
    on titular_pseudonimo (owner_id);



-- auto-generated definition
create table obra_obra
(
    id              integer      not null        primary key autoincrement,
    cod_ecad        integer unsigned,
    cod_iswc        varchar(20),
    titulo          varchar(200) not null,
    subtitulo       varchar(200),
    is_versao       bool         not null,
    versao          varchar(200),
    dt_inclusao     datetime     not null,
    dt_alteracao    datetime,
    is_estrangeira  bool         not null,
    is_instrumental bool         not null,
    is_delete       bool         not null,
    genero_id       integer      references obra_genero,
    owner_id        integer      references auth_user,
    cod_obra_mdb    integer unsigned
);

create index obra_obra_genero_id_68408bed
    on obra_obra (genero_id);

create index obra_obra_owner_id_efc0ecf6
    on obra_obra (owner_id);

-- auto-generated definition
create table obra_obrastitulares
(
    id                   integer not null        primary key autoincrement,
    percentual           real,
    categoria_id         integer                 references obra_categoria,
    obra_id              integer not null        references obra_obra,
    owner_id             integer                 references auth_user,
    titular_id           integer not null        references titular_titular,
    cod_obra_titular_mdb integer unsigned
);

create index obra_obrastitulares_categoria_id_f2f2f020
    on obra_obrastitulares (categoria_id);

create index obra_obrastitulares_obra_id_eec0d043
    on obra_obrastitulares (obra_id);

create index obra_obrastitulares_owner_id_4a538748
    on obra_obrastitulares (owner_id);

create index obra_obrastitulares_titular_id_fffd9ff7
    on obra_obrastitulares (titular_id);

