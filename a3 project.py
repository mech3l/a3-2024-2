import json
import os

# Caminho onde os arquivos da API estão armazenados
CAMINHO_ARQUIVOS = r"swagger"

def traduzir_para_libras(texto):
    if texto.strip():  # Verifica se o texto não está vazio
        try:
            # Caminho para o arquivo de resposta
            arquivo_resposta = os.path.join(CAMINHO_ARQUIVOS, f"{texto}.json")
            
            if os.path.exists(arquivo_resposta):
                with open(arquivo_resposta, "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)
                video_url = dados.get("video_url", "URL do vídeo não encontrada.")
                return f"Tradução realizada!\nAcesse: {video_url}"
            else:
                return "Tradução não encontrada para o texto informado."
        except Exception as e:
            return f"Erro ao acessar os arquivos: {e}"
    else:
        return "Digite um texto para traduzir."

# Entrada do usuário
entrada_texto = input("Digite o texto para tradução: ")
resultado = traduzir_para_libras(entrada_texto)
print(resultado)
