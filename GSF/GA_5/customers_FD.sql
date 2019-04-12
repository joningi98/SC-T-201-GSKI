
Select 'customers: cid --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM customers
     GROUP BY cid
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'customers: cid --> cs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM customers
     GROUP BY cid
     HAVING COUNT (DISTINCT cs) > 1
) X;
Select 'customers: cid --> cnr' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM customers
     GROUP BY cid
     HAVING COUNT (DISTINCT cnr) > 1
) X;
Select 'customers: cid --> cc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM customers
     GROUP BY cid
     HAVING COUNT (DISTINCT cc) > 1
) X;
Select 'customers: cid --> cz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM customers
     GROUP BY cid
     HAVING COUNT (DISTINCT cz) > 1
) X;
Select 'customers: cid --> eid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cid
     FROM customers
     GROUP BY cid
     HAVING COUNT (DISTINCT eid) > 1
) X;
Select 'customers: cn --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM customers
     GROUP BY cn
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'customers: cn --> cs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM customers
     GROUP BY cn
     HAVING COUNT (DISTINCT cs) > 1
) X;
Select 'customers: cn --> cnr' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM customers
     GROUP BY cn
     HAVING COUNT (DISTINCT cnr) > 1
) X;
Select 'customers: cn --> cc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM customers
     GROUP BY cn
     HAVING COUNT (DISTINCT cc) > 1
) X;
Select 'customers: cn --> cz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM customers
     GROUP BY cn
     HAVING COUNT (DISTINCT cz) > 1
) X;
Select 'customers: cn --> eid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cn
     FROM customers
     GROUP BY cn
     HAVING COUNT (DISTINCT eid) > 1
) X;
Select 'customers: cs --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cs
     FROM customers
     GROUP BY cs
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'customers: cs --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cs
     FROM customers
     GROUP BY cs
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'customers: cs --> cnr' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cs
     FROM customers
     GROUP BY cs
     HAVING COUNT (DISTINCT cnr) > 1
) X;
Select 'customers: cs --> cc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cs
     FROM customers
     GROUP BY cs
     HAVING COUNT (DISTINCT cc) > 1
) X;
Select 'customers: cs --> cz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cs
     FROM customers
     GROUP BY cs
     HAVING COUNT (DISTINCT cz) > 1
) X;
Select 'customers: cs --> eid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cs
     FROM customers
     GROUP BY cs
     HAVING COUNT (DISTINCT eid) > 1
) X;
Select 'customers: cnr --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cnr
     FROM customers
     GROUP BY cnr
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'customers: cnr --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cnr
     FROM customers
     GROUP BY cnr
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'customers: cnr --> cs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cnr
     FROM customers
     GROUP BY cnr
     HAVING COUNT (DISTINCT cs) > 1
) X;
Select 'customers: cnr --> cc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cnr
     FROM customers
     GROUP BY cnr
     HAVING COUNT (DISTINCT cc) > 1
) X;
Select 'customers: cnr --> cz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cnr
     FROM customers
     GROUP BY cnr
     HAVING COUNT (DISTINCT cz) > 1
) X;
Select 'customers: cnr --> eid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cnr
     FROM customers
     GROUP BY cnr
     HAVING COUNT (DISTINCT eid) > 1
) X;
Select 'customers: cc --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cc
     FROM customers
     GROUP BY cc
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'customers: cc --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cc
     FROM customers
     GROUP BY cc
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'customers: cc --> cs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cc
     FROM customers
     GROUP BY cc
     HAVING COUNT (DISTINCT cs) > 1
) X;
Select 'customers: cc --> cnr' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cc
     FROM customers
     GROUP BY cc
     HAVING COUNT (DISTINCT cnr) > 1
) X;
Select 'customers: cc --> cz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cc
     FROM customers
     GROUP BY cc
     HAVING COUNT (DISTINCT cz) > 1
) X;
Select 'customers: cc --> eid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cc
     FROM customers
     GROUP BY cc
     HAVING COUNT (DISTINCT eid) > 1
) X;
Select 'customers: cz --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cz
     FROM customers
     GROUP BY cz
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'customers: cz --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cz
     FROM customers
     GROUP BY cz
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'customers: cz --> cs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cz
     FROM customers
     GROUP BY cz
     HAVING COUNT (DISTINCT cs) > 1
) X;
Select 'customers: cz --> cnr' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cz
     FROM customers
     GROUP BY cz
     HAVING COUNT (DISTINCT cnr) > 1
) X;
Select 'customers: cz --> cc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cz
     FROM customers
     GROUP BY cz
     HAVING COUNT (DISTINCT cc) > 1
) X;
Select 'customers: cz --> eid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT cz
     FROM customers
     GROUP BY cz
     HAVING COUNT (DISTINCT eid) > 1
) X;
Select 'customers: eid --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT eid
     FROM customers
     GROUP BY eid
     HAVING COUNT (DISTINCT cid) > 1
) X;
Select 'customers: eid --> cn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT eid
     FROM customers
     GROUP BY eid
     HAVING COUNT (DISTINCT cn) > 1
) X;
Select 'customers: eid --> cs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT eid
     FROM customers
     GROUP BY eid
     HAVING COUNT (DISTINCT cs) > 1
) X;
Select 'customers: eid --> cnr' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT eid
     FROM customers
     GROUP BY eid
     HAVING COUNT (DISTINCT cnr) > 1
) X;
Select 'customers: eid --> cc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT eid
     FROM customers
     GROUP BY eid
     HAVING COUNT (DISTINCT cc) > 1
) X;
Select 'customers: eid --> cz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT eid
     FROM customers
     GROUP BY eid
     HAVING COUNT (DISTINCT cz) > 1
) X;