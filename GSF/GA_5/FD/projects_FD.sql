
Select 'projects: id --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT id
     FROM projects
     GROUP BY id
     HAVING COUNT (DISTINCT sid) > 1
) X;
Select 'projects: id --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT id
     FROM projects
     GROUP BY id
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'projects: id --> sn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT id
     FROM projects
     GROUP BY id
     HAVING COUNT (DISTINCT sn) > 1
) X;
Select 'projects: id --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT id
     FROM projects
     GROUP BY id
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'projects: id --> mid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT id
     FROM projects
     GROUP BY id
     HAVING COUNT (DISTINCT mid) > 1
) X;
Select 'projects: id --> mn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT id
     FROM projects
     GROUP BY id
     HAVING COUNT (DISTINCT mn) > 1
) X;
Select 'projects: sid --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sid
     FROM projects
     GROUP BY sid
     HAVING COUNT (DISTINCT id) > 1
) X;
Select 'projects: sid --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sid
     FROM projects
     GROUP BY sid
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'projects: sid --> sn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sid
     FROM projects
     GROUP BY sid
     HAVING COUNT (DISTINCT sn) > 1
) X;
Select 'projects: sid --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sid
     FROM projects
     GROUP BY sid
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'projects: sid --> mid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sid
     FROM projects
     GROUP BY sid
     HAVING COUNT (DISTINCT mid) > 1
) X;
Select 'projects: sid --> mn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sid
     FROM projects
     GROUP BY sid
     HAVING COUNT (DISTINCT mn) > 1
) X;
Select 'projects: pid --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM projects
     GROUP BY pid
     HAVING COUNT (DISTINCT id) > 1
) X;
Select 'projects: pid --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM projects
     GROUP BY pid
     HAVING COUNT (DISTINCT sid) > 1
) X;
Select 'projects: pid --> sn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM projects
     GROUP BY pid
     HAVING COUNT (DISTINCT sn) > 1
) X;
Select 'projects: pid --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM projects
     GROUP BY pid
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'projects: pid --> mid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM projects
     GROUP BY pid
     HAVING COUNT (DISTINCT mid) > 1
) X;
Select 'projects: pid --> mn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM projects
     GROUP BY pid
     HAVING COUNT (DISTINCT mn) > 1
) X;
Select 'projects: sn --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sn
     FROM projects
     GROUP BY sn
     HAVING COUNT (DISTINCT id) > 1
) X;
Select 'projects: sn --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sn
     FROM projects
     GROUP BY sn
     HAVING COUNT (DISTINCT sid) > 1
) X;
Select 'projects: sn --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sn
     FROM projects
     GROUP BY sn
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'projects: sn --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sn
     FROM projects
     GROUP BY sn
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'projects: sn --> mid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sn
     FROM projects
     GROUP BY sn
     HAVING COUNT (DISTINCT mid) > 1
) X;
Select 'projects: sn --> mn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT sn
     FROM projects
     GROUP BY sn
     HAVING COUNT (DISTINCT mn) > 1
) X;
Select 'projects: pn --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM projects
     GROUP BY pn
     HAVING COUNT (DISTINCT id) > 1
) X;
Select 'projects: pn --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM projects
     GROUP BY pn
     HAVING COUNT (DISTINCT sid) > 1
) X;
Select 'projects: pn --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM projects
     GROUP BY pn
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'projects: pn --> sn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM projects
     GROUP BY pn
     HAVING COUNT (DISTINCT sn) > 1
) X;
Select 'projects: pn --> mid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM projects
     GROUP BY pn
     HAVING COUNT (DISTINCT mid) > 1
) X;
Select 'projects: pn --> mn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM projects
     GROUP BY pn
     HAVING COUNT (DISTINCT mn) > 1
) X;
Select 'projects: mid --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mid
     FROM projects
     GROUP BY mid
     HAVING COUNT (DISTINCT id) > 1
) X;
Select 'projects: mid --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mid
     FROM projects
     GROUP BY mid
     HAVING COUNT (DISTINCT sid) > 1
) X;
Select 'projects: mid --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mid
     FROM projects
     GROUP BY mid
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'projects: mid --> sn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mid
     FROM projects
     GROUP BY mid
     HAVING COUNT (DISTINCT sn) > 1
) X;
Select 'projects: mid --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mid
     FROM projects
     GROUP BY mid
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'projects: mid --> mn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mid
     FROM projects
     GROUP BY mid
     HAVING COUNT (DISTINCT mn) > 1
) X;
Select 'projects: mn --> id' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mn
     FROM projects
     GROUP BY mn
     HAVING COUNT (DISTINCT id) > 1
) X;
Select 'projects: mn --> sid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mn
     FROM projects
     GROUP BY mn
     HAVING COUNT (DISTINCT sid) > 1
) X;
Select 'projects: mn --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mn
     FROM projects
     GROUP BY mn
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'projects: mn --> sn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mn
     FROM projects
     GROUP BY mn
     HAVING COUNT (DISTINCT sn) > 1
) X;
Select 'projects: mn --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mn
     FROM projects
     GROUP BY mn
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'projects: mn --> mid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT mn
     FROM projects
     GROUP BY mn
     HAVING COUNT (DISTINCT mid) > 1
) X;