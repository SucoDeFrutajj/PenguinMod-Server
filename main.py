import os
from cloudlink import cloudlink

if __name__ == "__main__":
    # Inicializa o objeto pai do cloudlink
    cl = cloudlink()
    
    # Pega a porta automática gerada pelo ambiente do Render
    port = int(os.environ.get("PORT", 3000))
    
    # Cria a instância correta do servidor
    server = cl.server
    
    # Roda o servidor passando apenas a porta (o host interno roda em 0.0.0.0 por padrão)
    server.run(port=port)
