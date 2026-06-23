import os
from cloudlink import cloudlink

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    server = cloudlink()
    server.host(host="0.0.0.0", port=port)
