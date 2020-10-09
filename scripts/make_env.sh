#!/bin/bash
echo -n "ICEART_DB_USER="
read user
echo -n "ICEART_DB_PW="
read pw
echo -n "ICEART_DB_PATH="
read path
echo "ICEART_DB_USER=$user" > ".env"
echo "ICEART_DB_PW=$pw" >> ".env"
echo "ICEART_DB_PATH=$path" >> ".env"
