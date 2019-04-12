
Select 'projects: id --> sid, id --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT id
      FROM projects
      GROUP BY id
      HAVING (COUNT(DISTINCT sid) * COUNT(DISTINCT id)
                   <> COUNT(*))
) X;
Select 'projects: id --> sid, id --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT id
      FROM projects
      GROUP BY id
      HAVING (COUNT(DISTINCT sid) * COUNT(DISTINCT pid)
                   <> COUNT(*))
) X;
Select 'projects: id --> pid, id --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT id
      FROM projects
      GROUP BY id
      HAVING (COUNT(DISTINCT pid) * COUNT(DISTINCT id)
                   <> COUNT(*))
) X;
Select 'projects: id --> pid, id --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT id
      FROM projects
      GROUP BY id
      HAVING (COUNT(DISTINCT pid) * COUNT(DISTINCT sid)
                   <> COUNT(*))
) X;
Select 'projects: sid --> id, sid --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT sid
      FROM projects
      GROUP BY sid
      HAVING (COUNT(DISTINCT id) * COUNT(DISTINCT sid)
                   <> COUNT(*))
) X;
Select 'projects: sid --> id, sid --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT sid
      FROM projects
      GROUP BY sid
      HAVING (COUNT(DISTINCT id) * COUNT(DISTINCT pid)
                   <> COUNT(*))
) X;
Select 'projects: sid --> pid, sid --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT sid
      FROM projects
      GROUP BY sid
      HAVING (COUNT(DISTINCT pid) * COUNT(DISTINCT id)
                   <> COUNT(*))
) X;
Select 'projects: sid --> pid, sid --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT sid
      FROM projects
      GROUP BY sid
      HAVING (COUNT(DISTINCT pid) * COUNT(DISTINCT sid)
                   <> COUNT(*))
) X;
Select 'projects: pid --> id, pid --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT pid
      FROM projects
      GROUP BY pid
      HAVING (COUNT(DISTINCT id) * COUNT(DISTINCT sid)
                   <> COUNT(*))
) X;
Select 'projects: pid --> id, pid --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT pid
      FROM projects
      GROUP BY pid
      HAVING (COUNT(DISTINCT id) * COUNT(DISTINCT pid)
                   <> COUNT(*))
) X;
Select 'projects: pid --> sid, pid --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT pid
      FROM projects
      GROUP BY pid
      HAVING (COUNT(DISTINCT sid) * COUNT(DISTINCT id)
                   <> COUNT(*))
) X;
Select 'projects: pid --> sid, pid --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT pid
      FROM projects
      GROUP BY pid
      HAVING (COUNT(DISTINCT sid) * COUNT(DISTINCT pid)
                   <> COUNT(*))
) X;