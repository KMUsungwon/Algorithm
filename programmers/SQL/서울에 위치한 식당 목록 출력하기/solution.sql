select i.rest_id, i.rest_name, i.food_type, i.favorites,
i.address, r.score
from rest_info i join
(
    select round(sum(review_score)/count(rest_id), 2) as score, rest_id from rest_review 
    group by rest_id
) as r on i.rest_id = r.rest_id
where i.address like "서울%"
order by r.score desc, i.favorites desc;