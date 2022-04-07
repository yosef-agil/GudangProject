@echo off

title Cloud SQL Proxy SAT-KAPITA
echo jangan di close selama koneksi
"./cloud_sql_proxy" -instances=sat-kapita-selekta-b:asia-southeast2:training-kapita-selekta=tcp:5432