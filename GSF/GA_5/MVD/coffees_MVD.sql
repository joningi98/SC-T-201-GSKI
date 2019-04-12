
Select 'coffees: did --> hid, did --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT did
      FROM coffees
      GROUP BY did
      HAVING (COUNT(DISTINCT hid) * COUNT(DISTINCT did)
                   <> COUNT(*))
) X;
Select 'coffees: did --> hid, did --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT did
      FROM coffees
      GROUP BY did
      HAVING (COUNT(DISTINCT hid) * COUNT(DISTINCT cid)
                   <> COUNT(*))
) X;
Select 'coffees: did --> cid, did --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT did
      FROM coffees
      GROUP BY did
      HAVING (COUNT(DISTINCT cid) * COUNT(DISTINCT did)
                   <> COUNT(*))
) X;
Select 'coffees: did --> cid, did --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT did
      FROM coffees
      GROUP BY did
      HAVING (COUNT(DISTINCT cid) * COUNT(DISTINCT hid)
                   <> COUNT(*))
) X;
Select 'coffees: hid --> did, hid --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT hid
      FROM coffees
      GROUP BY hid
      HAVING (COUNT(DISTINCT did) * COUNT(DISTINCT hid)
                   <> COUNT(*))
) X;
Select 'coffees: hid --> did, hid --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT hid
      FROM coffees
      GROUP BY hid
      HAVING (COUNT(DISTINCT did) * COUNT(DISTINCT cid)
                   <> COUNT(*))
) X;
Select 'coffees: hid --> cid, hid --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT hid
      FROM coffees
      GROUP BY hid
      HAVING (COUNT(DISTINCT cid) * COUNT(DISTINCT did)
                   <> COUNT(*))
) X;
Select 'coffees: hid --> cid, hid --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT hid
      FROM coffees
      GROUP BY hid
      HAVING (COUNT(DISTINCT cid) * COUNT(DISTINCT hid)
                   <> COUNT(*))
) X;
Select 'coffees: cid --> did, cid --> hid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT cid
      FROM coffees
      GROUP BY cid
      HAVING (COUNT(DISTINCT did) * COUNT(DISTINCT hid)
                   <> COUNT(*))
) X;
Select 'coffees: cid --> did, cid --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT cid
      FROM coffees
      GROUP BY cid
      HAVING (COUNT(DISTINCT did) * COUNT(DISTINCT cid)
                   <> COUNT(*))
) X;
Select 'coffees: cid --> hid, cid --> did' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT cid
      FROM coffees
      GROUP BY cid
      HAVING (COUNT(DISTINCT hid) * COUNT(DISTINCT did)
                   <> COUNT(*))
) X;
Select 'coffees: cid --> hid, cid --> cid' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT cid
      FROM coffees
      GROUP BY cid
      HAVING (COUNT(DISTINCT hid) * COUNT(DISTINCT cid)
                   <> COUNT(*))
) X;