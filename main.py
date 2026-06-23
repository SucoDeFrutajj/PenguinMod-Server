import os
from cloudlink import cloudlink

if __name__ == "__main__":
    # Inicializa o servidor CloudLink na versão 0.1.9.x
    server = cloudlink()
    
    # Captura a porta atribuída pelo contêiner do Render de forma dinâmica
    render_port = int(os.environ.get("PORT", 3000))
    
    # O comando oficial para rodar nesta versão precisa dos parâmetros exatamente nesta ordem
    server.server(render_port, "0.0.0.0")
