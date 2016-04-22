Easyling offers a white label version that can be customized with your corporate logos and domains to create a branded version, allowing you to use & sell Easyling as your own product. In order to create the branded version, six criteria must be met.

1. A €200 EUR topup / month (recurring): Easyling under your own brand name is special service, offered to customers who cater not only to one or two clients, but put their weight behind the punch and open up whole new markets with our proxy solution. 
2. A one-time setup fee of €200
3. A custom domain name: you will need a place to serve Easyling (as well as any previews) on. Generally, our clients settle on `app.${yourdomain}.com`, but we can use practically anything that comes to your mind - the only limitation is that we are unable to serve the proxy on a naked domain (for instance, `yourproxy.com`). Just keep in mind that once you settle on something, and we set up your branded Easyling, it becomes fixed, so your decision is final.
4. Two logos: one goes on the Dashboard, the other goes on the Workbench. They should be transparent PNGs, ideally, but we can use other file formats as well. However, their dimensions are fixed: the Dashboard logo is set at 200x62px, while the Workbench logo needs to be 109x44px. 
5. An SSL certificate: Easyling uses encrypted channels to communicate on, and for that, we require an SSL certificate to be made out for the domain name of your choice, and any subdomains it may have - Easyling uses your "app domain" to serve previews until they're published, so your certificate must be a so-called "wildcard certificate" (a type of SSL certificate valid not only for `app.yourdomain.com`, but also `*.app.yourdomain.com`). Certificate issuers are likely to request a Certificate Signing Request (CSR) for the certificate, which we will have to provide.  
In order to generate a CSR for you, you'll need to provide a few pieces of data related to your company, which need to be incorporated into the certificate. Please provide the following by replacing the fields (this should look fairly familiar to your IT department) with the appropriate data.
	1. `countryName_default = ${COUNTRY}`
	2. `localityName_default = ${CITY}`
	3. `streetAddress_default = ${ADDRESS}`
	4. `postalCode_default = ${ZIP}`
	5. `0.organizationName_default = ${COMPANY_NAME}`
	6. `organizationalUnitName_default = ${ORG_UNIT}`
6. The final step is to configure your DNS servers; and if you use Google Apps for `yourdomain.com`, the setup process will require someone with Google Apps admin rights as well.
7. Finally, if you want, you can specify the following information to customize the white label experience (this is completely voluntary and can be changed at any time):
	1. name: Name of your branded product
	2. greeter: Person signing the greeting emails for new users
	3. team: Team name 
	4. greeter address: Email address of the person sending the greeting emails
	5. greeter display name: Name of the person sending the greeting emails
	6. noreply address: Email address used for automated emails
	7. noreply name: Display name used for automated emails
	8. quote and wordcount signer: Person signing the quote and word count emails

Once all six main points are settled, and we have the logos and the SSL certificate with us, we'll set up the white label version for you, and you'll be ready to start cracking your target market wide open.