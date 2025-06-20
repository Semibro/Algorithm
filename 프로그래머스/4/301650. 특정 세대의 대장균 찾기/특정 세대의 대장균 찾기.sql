-- 코드를 작성해주세요
SELECT ID
FROM (
    SELECT D.ID
    FROM (
        SELECT B.ID
        FROM (
            SELECT ID
            FROM ECOLI_DATA
            WHERE PARENT_ID IS NULL
        ) A, 
        ECOLI_DATA B
        WHERE A.ID = B.PARENT_ID
    ) C,
    ECOLI_DATA D
    WHERE C.ID = D.PARENT_ID
) E
ORDER BY ID ASC
