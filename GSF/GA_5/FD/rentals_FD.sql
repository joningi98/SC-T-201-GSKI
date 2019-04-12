
Select 'rentals: pid --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM rentals
     GROUP BY pid
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'rentals: pid --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM rentals
     GROUP BY pid
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'rentals: pid --> s' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM rentals
     GROUP BY pid
     HAVING COUNT (DISTINCT s) > 1
) X;
Select 'rentals: pid --> hz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM rentals
     GROUP BY pid
     HAVING COUNT (DISTINCT hz) > 1
) X;
Select 'rentals: pid --> hs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM rentals
     GROUP BY pid
     HAVING COUNT (DISTINCT hs) > 1
) X;
Select 'rentals: pid --> hc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pid
     FROM rentals
     GROUP BY pid
     HAVING COUNT (DISTINCT hc) > 1
) X;
Select 'rentals: hid --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM rentals
     GROUP BY hid
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'rentals: hid --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM rentals
     GROUP BY hid
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'rentals: hid --> s' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM rentals
     GROUP BY hid
     HAVING COUNT (DISTINCT s) > 1
) X;
Select 'rentals: hid --> hz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM rentals
     GROUP BY hid
     HAVING COUNT (DISTINCT hz) > 1
) X;
Select 'rentals: hid --> hs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM rentals
     GROUP BY hid
     HAVING COUNT (DISTINCT hs) > 1
) X;
Select 'rentals: hid --> hc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hid
     FROM rentals
     GROUP BY hid
     HAVING COUNT (DISTINCT hc) > 1
) X;
Select 'rentals: pn --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM rentals
     GROUP BY pn
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'rentals: pn --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM rentals
     GROUP BY pn
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'rentals: pn --> s' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM rentals
     GROUP BY pn
     HAVING COUNT (DISTINCT s) > 1
) X;
Select 'rentals: pn --> hz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM rentals
     GROUP BY pn
     HAVING COUNT (DISTINCT hz) > 1
) X;
Select 'rentals: pn --> hs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM rentals
     GROUP BY pn
     HAVING COUNT (DISTINCT hs) > 1
) X;
Select 'rentals: pn --> hc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT pn
     FROM rentals
     GROUP BY pn
     HAVING COUNT (DISTINCT hc) > 1
) X;
Select 'rentals: s --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT s
     FROM rentals
     GROUP BY s
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'rentals: s --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT s
     FROM rentals
     GROUP BY s
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'rentals: s --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT s
     FROM rentals
     GROUP BY s
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'rentals: s --> hz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT s
     FROM rentals
     GROUP BY s
     HAVING COUNT (DISTINCT hz) > 1
) X;
Select 'rentals: s --> hs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT s
     FROM rentals
     GROUP BY s
     HAVING COUNT (DISTINCT hs) > 1
) X;
Select 'rentals: s --> hc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT s
     FROM rentals
     GROUP BY s
     HAVING COUNT (DISTINCT hc) > 1
) X;
Select 'rentals: hz --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hz
     FROM rentals
     GROUP BY hz
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'rentals: hz --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hz
     FROM rentals
     GROUP BY hz
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'rentals: hz --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hz
     FROM rentals
     GROUP BY hz
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'rentals: hz --> s' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hz
     FROM rentals
     GROUP BY hz
     HAVING COUNT (DISTINCT s) > 1
) X;
Select 'rentals: hz --> hs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hz
     FROM rentals
     GROUP BY hz
     HAVING COUNT (DISTINCT hs) > 1
) X;
Select 'rentals: hz --> hc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hz
     FROM rentals
     GROUP BY hz
     HAVING COUNT (DISTINCT hc) > 1
) X;
Select 'rentals: hs --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hs
     FROM rentals
     GROUP BY hs
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'rentals: hs --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hs
     FROM rentals
     GROUP BY hs
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'rentals: hs --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hs
     FROM rentals
     GROUP BY hs
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'rentals: hs --> s' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hs
     FROM rentals
     GROUP BY hs
     HAVING COUNT (DISTINCT s) > 1
) X;
Select 'rentals: hs --> hz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hs
     FROM rentals
     GROUP BY hs
     HAVING COUNT (DISTINCT hz) > 1
) X;
Select 'rentals: hs --> hc' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hs
     FROM rentals
     GROUP BY hs
     HAVING COUNT (DISTINCT hc) > 1
) X;
Select 'rentals: hc --> pid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hc
     FROM rentals
     GROUP BY hc
     HAVING COUNT (DISTINCT pid) > 1
) X;
Select 'rentals: hc --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hc
     FROM rentals
     GROUP BY hc
     HAVING COUNT (DISTINCT hid) > 1
) X;
Select 'rentals: hc --> pn' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hc
     FROM rentals
     GROUP BY hc
     HAVING COUNT (DISTINCT pn) > 1
) X;
Select 'rentals: hc --> s' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hc
     FROM rentals
     GROUP BY hc
     HAVING COUNT (DISTINCT s) > 1
) X;
Select 'rentals: hc --> hz' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hc
     FROM rentals
     GROUP BY hc
     HAVING COUNT (DISTINCT hz) > 1
) X;
Select 'rentals: hc --> hs' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT hc
     FROM rentals
     GROUP BY hc
     HAVING COUNT (DISTINCT hs) > 1
) X;