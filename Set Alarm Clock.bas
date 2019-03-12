_TITLE "Set Alarm Clock 4 Directions"
DIM GIMME_TIME AS STRING

COLOR 10
PRINT "Set an alarm for Alarm Clock 4 Directions"
PRINT "Enter a time (HHMM)..."
DO
    INPUT "> ", GIMME_TIME
LOOP UNTIL LEN(GIMME_TIME) = 4

H0 = VAL(MID$(GIMME_TIME, 1, 1))
H1 = VAL(MID$(GIMME_TIME, 2, 1))
M0 = VAL(MID$(GIMME_TIME, 3, 1))
M1 = VAL(MID$(GIMME_TIME, 4, 1))

OPEN "data/alarm.sav" FOR OUTPUT AS #1
PRINT #1, H0
PRINT #1, H1
PRINT #1, M0
PRINT #1, M1
CLOSE #1

GIMME_TIME = MID$(GIMME_TIME, 1, 2) + ":" + MID$(GIMME_TIME, 3, 2)

PRINT "Alarm Clock 4 Directions is now set to ring at " + GIMME_TIME



