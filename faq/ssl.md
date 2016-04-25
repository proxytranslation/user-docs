# SSL Certificates

## Overview
Easyling has the ability to proxy HTTPS pages, but to do so, it must be provided a certificate and private key matching the URL. Otherwise, the proxy will be unable to identify itself as a valid server, and the browser will abort the connection for security reasons.  
Easyling support can assist in deploying an HTTPS site by providing a CSR (Certificate Signing Request) to generate the appropriate certificate if the required information is provided, or the client can prepare the certificate themselves.

Additionally, a certificate is required to provide a branded Easyling instance. For more information, you can check the Whitelabel article of the FAQ.

## The protocol
HTTPS (also called HTTP over TLS, HTTP over SSL, and HTTP Secure) is a protocol for secure communication over a computer network which is widely used on the Internet. HTTPS consists of communication over Hypertext Transfer Protocol (HTTP) within a connection encrypted by Transport Layer Security or its predecessor, Secure Sockets Layer. The main motivation for HTTPS is authentication of the visited website and protection of the privacy and integrity of the exchanged data.

In its popular deployment on the internet, HTTPS provides authentication of the website and associated web server with which one is communicating, which protects against man-in-the-middle attacks. Additionally, it provides bidirectional encryption of communications between a client and server, which protects against eavesdropping and tampering with and/or forging the contents of the communication. In practice, this provides a reasonable guarantee that one is communicating with precisely the website that one intended to communicate with (as opposed to an impostor), as well as ensuring that the contents of communications between the user and site cannot be read or forged by any third party.

Historically, HTTPS connections were primarily used for payment transactions on the World Wide Web, e-mail and for sensitive transactions in corporate information systems. In the late 2000s and early 2010s, HTTPS began to see widespread use for protecting page authenticity on all types of websites, securing accounts and keeping user communications, identity and web browsing private.

## SSL Manipulation Commands
When uploading the keys into AppEngine, the file must be in RSA format. To verify, the beginning of the file should be: `-----BEGIN RSA PRIVATE KEY-----` . If you read `-----BEGIN PRIVATE KEY-----`, you have to convert it, using the following command:

```
openssl rsa -in key -out key.rsa.key
```



### Extracting Certificate and Private Key Files from a .pfx / PKCS#12 File (includes both the certificate and the private key)

- export the private key: `openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes`
- export the certificate: `openssl pkcs12 -in certname.pfx -nokeys -out cert.pem`
- create RSA key / remove passphrase from the key: `openssl rsa -in key.pem -out server.key`

### Check if a given key matches a certificate (or CSR)

- `openssl rsa -noout -modulus -in privateKey.key | openssl md5`
- `openssl x509 -noout -modulus -in certificate.crt | openssl md5`
- `openssl req -noout -modulus -in CSR.csr | openssl md5`