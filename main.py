import os
from cloudlink import cloudlink

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    # Inicializa o objeto do CloudLink
    server = cloudlink()
    # Nas versões 0.1.9.x o comando correto é .server e os parâmetros são nesta ordem
    server.server(port=port, host="0.0.0.0")
