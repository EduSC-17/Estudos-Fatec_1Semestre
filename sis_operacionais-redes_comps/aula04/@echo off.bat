@echo off
:menu
cls
echo 1. Abrir bloco de Notas
echo 2. Sair
set /p opcao=Escolha uma opcao:
if "%opcao%"=="1" start notepad.exe & goto menu
if "%opcao%"=="2" goto sair
goto menu
:sair