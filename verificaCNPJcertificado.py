#FUNCIONALIDADE = verificar as chaves principais de um certificado

from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.backends import default_backend

# Caminho e senha do certificado
cert_path = r"C:\Users\Suporte TI AUTOCOM\Documents\scripts/GONCALVES NETO E BORGES LTDA - senha G2025 (2)"
senha = b"G2025"

# Ler o certificado
with open(cert_path, "rb") as f:
    pfx_data = f.read()

private_key, cert, additional_certs = pkcs12.load_key_and_certificates(pfx_data, senha, default_backend())

# Listar todos os campos do subject
for attr in cert.subject:
    print(f"{attr.oid._name}: {attr.value}")
