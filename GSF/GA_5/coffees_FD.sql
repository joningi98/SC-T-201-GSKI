
Select 'coffees: did --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT did
     FROM coffees
     GROUP BY did
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'coffees: did --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT did
     FROM coffees
     GROUP BY did
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'coffees: did --> dn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT did
     FROM coffees
     GROUP BY did
     HAVING COUNT (DISTINCT dn) > 1
) X;
Select 'coffees: did --> ds' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT did
     FROM coffees
     GROUP BY did
     HAVING COUNT (DISTINCT ds) > 1
) X;
Select 'coffees: did --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT did
     FROM coffees
     GROUP BY did
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'coffees: did --> cm' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT did
     FROM coffees
     GROUP BY did
     HAVING COUNT (DISTINCT cm) > 1
) X;
Select 'coffees: hid --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM coffees
     GROUP BY hid
     HAVING COUNT (DISTINCT did) > 1
) X;
Select 'coffees: hid --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM coffees
     GROUP BY hid
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'coffees: hid --> dn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM coffees
     GROUP BY hid
     HAVING COUNT (DISTINCT dn) > 1
) X;
Select 'coffees: hid --> ds' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM coffees
     GROUP BY hid
     HAVING COUNT (DISTINCT ds) > 1
) X;
Select 'coffees: hid --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM coffees
     GROUP BY hid
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'coffees: hid --> cm' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM coffees
     GROUP BY hid
     HAVING COUNT (DISTINCT cm) > 1
) X;
Select 'coffees: cid --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM coffees
     GROUP BY cid
     HAVING COUNT (DISTINCT did) > 1
) X;
Select 'coffees: cid --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM coffees
     GROUP BY cid
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'coffees: cid --> dn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM coffees
     GROUP BY cid
     HAVING COUNT (DISTINCT dn) > 1
) X;
Select 'coffees: cid --> ds' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM coffees
     GROUP BY cid
     HAVING COUNT (DISTINCT ds) > 1
) X;
Select 'coffees: cid --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM coffees
     GROUP BY cid
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'coffees: cid --> cm' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM coffees
     GROUP BY cid
     HAVING COUNT (DISTINCT cm) > 1
) X;
Select 'coffees: dn --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT dn
     FROM coffees
     GROUP BY dn
     HAVING COUNT (DISTINCT did) > 1
) X;
Select 'coffees: dn --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT dn
     FROM coffees
     GROUP BY dn
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'coffees: dn --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT dn
     FROM coffees
     GROUP BY dn
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'coffees: dn --> ds' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT dn
     FROM coffees
     GROUP BY dn
     HAVING COUNT (DISTINCT ds) > 1
) X;
Select 'coffees: dn --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT dn
     FROM coffees
     GROUP BY dn
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'coffees: dn --> cm' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT dn
     FROM coffees
     GROUP BY dn
     HAVING COUNT (DISTINCT cm) > 1
) X;
Select 'coffees: ds --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT ds
     FROM coffees
     GROUP BY ds
     HAVING COUNT (DISTINCT did) > 1
) X;
Select 'coffees: ds --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT ds
     FROM coffees
     GROUP BY ds
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'coffees: ds --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT ds
     FROM coffees
     GROUP BY ds
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'coffees: ds --> dn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT ds
     FROM coffees
     GROUP BY ds
     HAVING COUNT (DISTINCT dn) > 1
) X;
Select 'coffees: ds --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT ds
     FROM coffees
     GROUP BY ds
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'coffees: ds --> cm' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT ds
     FROM coffees
     GROUP BY ds
     HAVING COUNT (DISTINCT cm) > 1
) X;
Select 'coffees: cn --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM coffees
     GROUP BY cn
     HAVING COUNT (DISTINCT did) > 1
) X;
Select 'coffees: cn --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM coffees
     GROUP BY cn
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'coffees: cn --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM coffees
     GROUP BY cn
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'coffees: cn --> dn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM coffees
     GROUP BY cn
     HAVING COUNT (DISTINCT dn) > 1
) X;
Select 'coffees: cn --> ds' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM coffees
     GROUP BY cn
     HAVING COUNT (DISTINCT ds) > 1
) X;
Select 'coffees: cn --> cm' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM coffees
     GROUP BY cn
     HAVING COUNT (DISTINCT cm) > 1
) X;
Select 'coffees: cm --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cm
     FROM coffees
     GROUP BY cm
     HAVING COUNT (DISTINCT did) > 1
) X;
Select 'coffees: cm --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cm
     FROM coffees
     GROUP BY cm
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'coffees: cm --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cm
     FROM coffees
     GROUP BY cm
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'coffees: cm --> dn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cm
     FROM coffees
     GROUP BY cm
     HAVING COUNT (DISTINCT dn) > 1
) X;
Select 'coffees: cm --> ds' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cm
     FROM coffees
     GROUP BY cm
     HAVING COUNT (DISTINCT ds) > 1
) X;
Select 'coffees: cm --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cm
     FROM coffees
     GROUP BY cm
     HAVING COUNT (DISTINCT cn) > 1
) X;