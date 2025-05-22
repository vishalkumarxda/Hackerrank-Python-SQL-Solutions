DECLARE @X INT
SELECT @X = 20
WHILE @X > 0
BEGIN 
PRINT replicate ("* ", @x)
SET @X = @X - 1
END