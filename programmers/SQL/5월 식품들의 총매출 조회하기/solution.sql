SELECT p.product_id, p.product_name, p.price * o.amount as "total_sales"
from food_product p join
(
    select product_id, sum(amount) as amount
    from food_order
    where date_format(produce_date, "%Y-%m") = "2022-05"
    group by product_id
) as o
on p.product_id=o.product_id
group by p.product_name
order by 3 DESC;