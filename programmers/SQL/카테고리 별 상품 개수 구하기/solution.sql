SELECT substring(product_code, 1, 2) as CATEGORY, count(product_code) as PRODUCTS
from product
group by substring(product_code, 1, 2)
order by 1;