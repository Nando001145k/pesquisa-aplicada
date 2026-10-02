import pandas as pd

print("A processar dados da PRF...")
# Lê a base da PRF
df_prf = pd.read_csv(
    "prf_2020_2025.csv", sep=";", low_memory=False, on_bad_lines="skip"
)

# Filtra apenas a Paraíba e seleciona colunas essenciais para a dashboard
if "uf" in df_prf.columns:
    df_prf = df_prf[df_prf["uf"] == "PB"]

colunas_prf = [
    "data_inversa",
    "dia_semana",
    "horario",
    "uf",
    "br",
    "km",
    "municipio",
    "causa_acidente",
    "tipo_acidente",
    "classificacao_acidente",
]
df_prf = df_prf[[c for c in colunas_prf if c in df_prf.columns]]

# Salva uma versão leve para o GitHub
df_prf.to_csv("prf_pb_leve.csv", index=False)
print("-> PRF processada e salva como 'prf_pb_leve.csv'!")


print("A processar dados do INMET...")
# Lê a base do INMET
df_inmet = pd.read_csv(
    "inmet.csv",
    sep=",",
    encoding="latin1",
    low_memory=False,
    on_bad_lines="skip",
)

# Filtra apenas a Paraíba (ajuste o nome da coluna de UF se necessário)
if "UF" in df_inmet.columns:
    df_inmet = df_inmet[df_inmet["UF"] == "PB"]

# Salva uma versão leve para o GitHub
df_inmet.to_csv("inmet_pb_leve.csv", index=False)
print("-> INMET processado e salvo como 'inmet_pb_leve.csv'!")

print("Processo concluído! Já podes usar os ficheiros '_leve.csv'.")