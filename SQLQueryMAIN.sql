select customer_name, o.id as o_id, g.id as g_id, g.[name], g_o.amount as g_am, p.id as p_id, p.name, g_p.product_amount as pr_am_for_g, p.amount as p_am_in_sklad, c.summ_money as price   
from customers as c 
inner join customers_orders as c_o on c.id = c_o.customer_id
inner join orders as o on c_o.order_id = o.id
inner join goods_order as g_o on g_o.order_id = o.id
inner join goods as g on g.id = g_o.goods_id
inner join goods_products as g_p on g.id = g_p.goods_id
inner join products as p on p.id = g_p.product_id
where c.id = 1;

ALTER Table goods_order
add constraint [goods_order_fk0] foreign key (goods_id) references goods(id);

select * from goods_products;
select * from goods_order;
select * from goods;
select * from orders;
select * from customers_orders;
select * from customers;
select * from products;

insert into orders values(9);
insert into customers_orders values(1,9) 

delete from goods_order;
delete from customers_orders;
delete from orders;

update customers
set summ_money = 0 where id = 1;

set IDENTITY_INSERT orders ON;
set IDENTITY_INSERT orders OFF;

DBCC CHECKIDENT ([orders], NORESEED);
DBCC CHECKIDENT ([orders], RESEED, 0);
