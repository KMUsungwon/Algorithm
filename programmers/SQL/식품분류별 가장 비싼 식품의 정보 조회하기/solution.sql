select CATEGORY, price as MAX_PRICE, PRODUCT_NAME from food_product
where CATEGORY in ("식용유", "과자", "김치", "국")
and price in (select max(price) from food_product group by category)
order by 2 desc;