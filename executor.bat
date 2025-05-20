REM  Script .bat para poder rodar os scripts python limpar_cabecalho_repetido e formatadorcsv 

@echo off
echo === Etapa 1: Limpando CSV ===
python limpar_cabecalho_repetido.py

IF EXIST saida1.csv (
    echo === Etapa 2: Processando dados ===
    python formatadorcsv.py

    REM Verifica se o script anterior executou com sucesso
    IF %ERRORLEVEL% EQU 0 (
        echo === Limpando arquivos temporarios ===
        del saida1.csv
        echo Arquivo saida1.csv removido com sucesso.
    ) ELSE (
        echo ERRO: O script formatadorcsv.py falhou. saida1.csv nao foi removido.
    )
) ELSE (
    echo ERRO: Arquivo saida1.csv nao encontrado. Abortando...
)

pause
