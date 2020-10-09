@echo off
set /p name="ICEART_DB_USER="
set /p pw="ICEART_DB_PW="
set /p path="ICEART_DB_PATH="
echo ICEART_DB_USER=%name%> .env
echo ICEART_DB_PW=%pw%>> .env
echo ICEART_DB_PATH=%path%>> .env
