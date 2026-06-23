import os
from cloudlink import cloudlink

if __name__ == "__main__":
    cl = cloudlink()
    server = cl.server
    port = int(os.environ.get("PORT", 3000))
    server.run(host="0.0.0.0", port=port)
