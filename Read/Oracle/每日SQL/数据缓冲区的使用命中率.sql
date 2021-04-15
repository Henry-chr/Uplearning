SELECT name, value
  FROM v$sysstat
 WHERE name IN ('db block gets', 'consistent gets', 'physical reads')
union all
select '���ݻ�������ʹ��������' name,
       1 - (max(case
                  when a.name = 'physical reads' then
                   a.value
                end) /
       (max(case
                   when a.name = 'db block gets' then
                    a.value
                 end) + max(case
                                    when a.name = 'consistent gets' then
                                     a.value
                                  end)))
  from (SELECT name, value
          FROM v$sysstat
         WHERE name IN
               ('db block gets', 'consistent gets', 'physical reads')) a
