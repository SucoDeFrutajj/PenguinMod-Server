import os
from cloudlink import cloudlink

if __name__ == "__main__":
    # 1. Cria o objeto principal
    cl = cloudlink()
    
    # 2. Inicializa o componente de servidor interno
    server = cl.server(logs=True)
    
    # 3. Pega a porta dinâmica do Render
    port = int(os.environ.get("PORT", 3000))
    
    # 4. Roda o servidor passando os parâmetros corretos exigidos pela biblioteca
    server.run(ip="0.0.0.0", port=port)
