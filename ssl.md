When uploading the keys into AppEngine, the file must be in RSA format. To verify, the beginning of the file should be: `-----BEGIN RSA PRIVATE KEY-----` . If you read `-----BEGIN PRIVATE KEY-----`, you have to convert it, using the following command:

```
openssl rsa -in key -out key.rsa.key
```



# Extracting Certificate and Private Key Files from a .pfx / PKCS#12 File (includes both the certificate and the private key)

- export the private key: `openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes`
- export the certificate: `openssl pkcs12 -in certname.pfx -nokeys -out cert.pem`
- create RSA key / remove passphrase from the key: `openssl rsa -in key.pem -out server.key`

# check if a given key matches a certificate (or CSR)

- `openssl rsa -noout -modulus -in privateKey.key | openssl md5`
- `openssl x509 -noout -modulus -in certificate.crt | openssl md5`
- `openssl req -noout -modulus -in CSR.csr | openssl md5`