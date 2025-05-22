DECLARE @X INT
SELECT @X = 1
WHILE @X <= 20
BEGIN
PRINT replicate('* ', @x)
SET @x = @x + 1
END