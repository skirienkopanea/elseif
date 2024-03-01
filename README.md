# elseif
Parse SQL based IF ... THEN, ELSEIF ... THEN, ELSE, END IF logic to single line IF so that cursor (for loop) logic can be executed in UPDATE statements WHERE parsed "if,else,elseif" condition

## Sample input

```
do something 0
IF a THEN
   do something 1
   IF aa THEN
      do something 2
   ELSE
      do something 3
   END IF
      do something 4
ELSEIF b THEN
   do something 5
   IF 1 THEN
      do something 6
   ELSEIF 2
      do something 7
   ELSEIF 3
      do something 8
   END IF
      do something 9
ELSEIF c THEN
   do something 10
   IF cc THEN
      do something 11
   ELSE
      do something 12
   END IF
   do something 13
ELSE
   do something 14
END IF;
do something 15
```

## Sample output
```
do something 0 WHERE 1 = 1
do something 1 WHERE a
do something 2 WHERE a AND aa
do something 3 WHERE a AND NOT (aa)
do something 4 WHERE a
do something 5 WHERE b AND NOT (a)
do something 6 WHERE b AND 1 AND NOT (a)
do something 7 WHERE b AND 2 AND NOT (a OR 1)
do something 8 WHERE b AND 3 AND NOT (a OR 1 OR 2)
do something 9 WHERE b AND NOT (a)
do something 10 WHERE c AND NOT (a OR b)
do something 11 WHERE c AND cc AND NOT (a OR b)
do something 12 WHERE c AND NOT (a OR b OR cc)
do something 13 WHERE c AND NOT (a OR b)
do something 14 WHERE NOT (a OR b OR c)
do something 15 WHERE 1 = 1
```
