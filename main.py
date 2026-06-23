import os
from cloudlink import server
from cloudlink.server.protocols import clpv4

if __name__ == "__main__":
    # Inicializa o servidor moderno v0.2.0
    my_server = server()
    
    # Ativa o protocolo clpv4 que o PenguinMod exige
    protocol = clpv4(my_server)
    
    # Pega a porta automática do Render
    port = int(os.environ.get("PORT", 3000))
    
    # Coloca o servidor no ar
    my_server.run(port=port)
