import os
from cloudlink import server
from cloudlink.server.protocols import clpv4

if __name__ == "__main__":
    # 1. Inicializa o servidor moderno
    my_server = server()
    
    # 2. Ativa o protocolo clpv4 (essencial para o PenguinMod se conectar)
    protocol = clpv4(my_server)
    
    # 3. Captura a porta gerada pelo Render
    port = int(os.environ.get("PORT", 3000))
    
    # 4. Coloca o servidor no ar na porta correta
    my_server.run(port=port)
