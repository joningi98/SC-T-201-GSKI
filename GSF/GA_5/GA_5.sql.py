table_arr = {
    "coffees": ['did', 'hid', 'cid', 'dn', 'ds', 'cn', 'cm'],
    "customers": ['cid', 'cn', 'cs', 'cnr', 'cc', 'cz', 'eid'],
    "projects": ['id', 'sid', 'pid', 'sn', 'pn', 'mid', 'mn'],
    "rentals": ['pid', 'hid', 'pn', 's', 'hz', 'hs', 'hc']
}


mvd_table_arr = {
    "coffees": ["did", "hid", "cid"],
    "projects": ["id", "sid", "pid"],
}

for table, param_array in table_arr.items():
    with open(str(table) + "_FD" + '.sql', 'w') as file:
        for j in param_array:
            for k in param_array:
                if j != k:
                    file.write(f"""
Select '{table}: {j} --> {k}' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (
     SELECT {j}
     FROM {table}
     GROUP BY {j}
     HAVING COUNT (DISTINCT {k}) > 1
) X;""")


for table, param_array in mvd_table_arr.items():
    with open(str(table) + "_MVD" + '.sql', 'w') as file:
        for j in param_array:
            for k in param_array:
                for u in param_array:
                    if j != k:
                        if k != u:
                            file.write(f"""
Select '{table}: {j} --> {k}, {j} --> {u}' AS FD,
    CASE WHEN COUNT(*)=0 THEN 'HOLDS'
    ELSE 'DOES NOT HOLD' END AS VALIDITY
FROM (SELECT {j}
      FROM {table}
      GROUP BY {j}
      HAVING (COUNT(DISTINCT {k}) * COUNT(DISTINCT {u})
                   <> COUNT(*))
) X;""")







