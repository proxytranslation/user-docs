# SSL Certificates

## Overview
Easyling has the ability to proxy HTTPS pages, but to do so, it must be provided a certificate and private key matching the URL. Otherwise, the proxy will be unable to identify itself as a valid server, and the browser will abort the connection for security reasons.  
Easyling support can assist in deploying an HTTPS site by providing a CSR (Certificate Signing Request) to generate the appropriate certificate if the required information is provided, or the client can prepare the certificate themselves.

Additionally, a certificate is required to provide a branded Easyling instance. For more information, you can check the [Whitelabel](/faq/whitelabel.html) article of the FAQ.

## The protocol
HTTPS (also called HTTP over TLS, HTTP over SSL, and HTTP Secure) is a protocol for secure communication over a computer network which is widely used on the Internet. HTTPS consists of communication over Hypertext Transfer Protocol (HTTP) within a connection encrypted by Transport Layer Security or its predecessor, Secure Sockets Layer. The main motivation for HTTPS is authentication of the visited website and protection of the privacy and integrity of the exchanged data.

In its popular deployment on the internet, HTTPS provides authentication of the website and associated web server with which one is communicating, which protects against man-in-the-middle attacks. Additionally, it provides bidirectional encryption of communications between a client and server, which protects against eavesdropping and tampering with and/or forging the contents of the communication. In practice, this provides a reasonable guarantee that one is communicating with precisely the website that one intended to communicate with (as opposed to an impostor), as well as ensuring that the contents of communications between the user and site cannot be read or forged by any third party.

Historically, HTTPS connections were primarily used for payment transactions on the World Wide Web, e-mail and for sensitive transactions in corporate information systems. In the late 2000s and early 2010s, HTTPS began to see widespread use for protecting page authenticity on all types of websites, securing accounts and keeping user communications, identity and web browsing private.  
(Courtesy of Wikipedia)

## Issuing an SSL certificate
Issuing universally accepted certificates is restricted to the so-called "Root Certificate Authorities". However, root authorities will generally delegate their powers to "Intermediate Authorities", who will sign certificates as requested by the end user (provided ownership of the domain can be verified).  
When requesting a certificate for your whitelabel installation or HTTPS site, you will most likely interact with an intermediate authority, by providing them an encrypted configuration file (the Certificate Signing Request), which the provider consumes to produce a cryptographically signed certificate.

Using a CSR has several distinct advantages over generating your own certificate at the issuer: since the Easyling support crew is in control of the final product, we can tailor the request to generate the certificate we need from you; and since the private key remains safe with us, you do not need to take special precautions when sending it.  
However, we require some information to be provided to us beforehand:  
1. `countryName_default = ${COUNTRY}`
2. `localityName_default = ${CITY}`
3. `streetAddress_default = ${ADDRESS}`
4. `postalCode_default = ${ZIP}`
5. `0.organizationName_default = ${COMPANY_NAME}`
6. `organizationalUnitName_default = ${ORG_UNIT}`

Issuing a certificate consists of several predetermined steps. First, a cryptographic key pair is generated, one half public, the other private. Then, a file indicating the domain the certificate is to be issued for, as well as various data about the entity holding the domain (generally, you or your client) is created. This file is then combined with the public half of the key, and signed with the private half. The resulting encrypted file is then handed to the issuer, who verifies the information contained within, and if successful, encodes the information into a public certificate, signing it with its own private key. This is the file that needs to be provided to Easyling support.

## Providing us with a certificate
Following the previous phase, you are now in possession of a cryptographic certificate, and possibly its private key (if you elected to create your own certificate instead of requesting a CSR from us).

If we provided you with a CSR file, you need to send only the certificate. On its own, the certificate is not viable - it requires the private key to be useful, thus, it can be sent via email safely. The private key remains safe with us, and we will use it to upload the certificate to Google AppEngine, from where it will be available to authenticate the proxied site to the browser, and enable HTTPS for the translations.

If you elected to forgo the CSR and generate your own certificate, we will need the associated private key as well (and any passwords used to lock the private key). In this case, however, care must be taken to prevent the certificate falling into the wrong hands: the certificate and its keyfile, or the keyfile and its password must never travel together - if the email carrying both is intercepted, the malicious third party can use it to impersonate your site! Either use two separate emails, or even two different channels (email and Skype, for instance) to provide us the key and password and the certificate.  
Once we receive the files, we will again upload them to AppEngine after decrypting the keyfile, at which point it will be available for use with the proxied site.

## SSL Manipulation Commands
### Converting private keys to RSA
When uploading the keys into AppEngine, the file must be in RSA format. To verify, the beginning of the file should be: `-----BEGIN RSA PRIVATE KEY-----` . If you read `-----BEGIN PRIVATE KEY-----`, you have to convert it, using the following command:

```
openssl rsa -in key -out key.rsa.key
```

### Extracting Certificate and Private Key Files from a .pfx / PKCS#12 File (includes both the certificate and the private key)

- export the private key: `openssl pkcs12 -in certname.pfx -nocerts -out key.pem -nodes`
- export the certificate: `openssl pkcs12 -in certname.pfx -nokeys -out cert.pem`
- create RSA key / remove passphrase from the key: `openssl rsa -in key.pem -out server.key`

### Check if a given key matches a certificate (or CSR)
By running these commands on the keyfile and certificate, you can verify that the key used to generate the certificate matches the one you have on hand. If the two outputs match, so do the keyfiles. But if not, your client may have used their own private keys to create the certificate, which you will have to obtain before forwarding it to us.

- `openssl rsa -noout -modulus -in privateKey.key | openssl md5`
- `openssl x509 -noout -modulus -in certificate.crt | openssl md5`

Alternatively, if you have the CSR as well, you can use the following command to obtain the checksum of the CSR's key and verify that the CSR you have on hand was used to generate the certificate.
- `openssl req -noout -modulus -in CSR.csr | openssl md5`
