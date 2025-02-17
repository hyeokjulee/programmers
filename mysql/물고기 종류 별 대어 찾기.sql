select fi.ID, fni.FISH_NAME, grouped_fi.LENGTH
from FISH_INFO as fi
    join FISH_NAME_INFO as fni
    on fi.FISH_TYPE = fni.FISH_TYPE
    join (
        select FISH_TYPE, max(LENGTH) as LENGTH
        from FISH_INFO
        group by FISH_TYPE
    ) as grouped_fi
    on fi.FISH_TYPE = grouped_fi.FISH_TYPE and fi.LENGTH = grouped_fi.LENGTH
order by fi.ID asc;