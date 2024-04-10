@echo off
echo Compiling TypeScript...
call tsc > tsc_log.txt 2>&1
echo TypeScript compilation complete.
echo Starting Flask application...
py -m flask --app app run
pause