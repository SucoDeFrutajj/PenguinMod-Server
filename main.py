import os
from cloudlink import cloudlink

if __name__ == "__main__":
    # 1. Instancia o objeto pai do cloudlink
    cl = cloudlink()
    
    # 2. Inicializa o objeto de servidor conforme a documentação oficial
    server = cl.server(logs=True)
    
    # 3. Captura a porta dinâmica exigida pelo Render
    port = int(os.environ.get("PORT", 3000))
    
    # 4. Roda o servidor usando os argumentos corretos ('ip' e 'port')
    server.run(ip="0.0.0.0", port=port)
