SET SERVEROUTPUT ON;
DECLARE
X NUMBER;
RES CLOB := '';
BEGIN
    FOR I IN 2..1000 LOOP
        X := 0;
        FOR J IN 2..(I/2) LOOP
            IF MOD (I, J) = 0 THEN
                X := 1;
                EXIT;
            END IF;
        END LOOP;
        IF X = 0 THEN
            RES := RES || I || '&';
        END IF;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE(SUBSTR(RES,1,LENGTH(RES)-1));
END;
/          
        