create table customer(
    id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    email varchar(100) unique not null,
    data_created_at timestamp with time zone default  now()
);

create table accounts(
    acc_id serial primary key,
    customer_id int not null refrences customer(id) on delete  cascade,
    account_type varchar(30) not null,
    balance decimal(18,2) not null defaul 0 check(balance>=0),
    data_created_at timestamp with time zone default now()
);

create table transactions(
    trans_id serial primary key,
    acc_id int not null references accounts(acc_id) on delete cascade,
    txn_type varchar(30) not null,
    amount decimal(18,2) not null check(amount>0),
    related_acc_id int null,
    status varchar(30) not null default 'Completed',
    data_created_at timestamp with time zone default now()
);