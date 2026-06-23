import os
from cloudlink import cloudlink

if __name__ == "__main__":
    # Inicializa o objeto principal do CloudLink
    cl = cloudlink()
    
    # Nas versões 0.1.9.x, as propriedades são injetadas direto no objeto antes de ligar
    cl.host = "0.0.0.0"
    cl.port = int(os.environ.get("PORT", 3000))
    
    # Inicia o servidor usando as configurações injetadas acima
    cl.server()
