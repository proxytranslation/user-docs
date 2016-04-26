# What is Easyling?

Easyling is fundamentally a cloud-based translation proxy solution designed to make websites available in several languages. Easily.

**What does it mean?**<br>
If you are a **business owner**, it can help you reach a wider customer-base through providing information to your potential customers in their native language. What's more, you can do more than just translating the text on your website, you can ***localize*** it: you can also adapt your message, the images displayed, or even your product range offered to the targeted culture. And all this without the need of heavy upfront investment in IT infrastructure and personnel, and the hassle with regular maintenance and upgrade. Easyling takes care of the IT part, so that you could concentrate on the content - and growing your business.  


If you are a **language service provider** (LSP), you can offer cutting-edge website localization services to your customers - even under your own brand name! Easyling provides the technology, takes care of the IT infrastructure, leaving you to concentrate on your core business: cross-cultural communication. What's more, your translators don't need to learn using just another tool, they can keep using their own preferred CAT-tools.<br>
***Sounds good?***

There are several challenges both business owners and language service providers face during website translation. The "ideal" workflow would be to create the  content in the original language, get it translated into the desired languages, and then publish all language variants at the same time, from the website owner's own content management system (CMS) - right from the very first page on the website. But reality is different. Apart from the fact that not many CMSs are capable of handling several languages, usually website localization comes into the picture at a later stage, when there is already a huge amount of data published on the website. And, in most cases, the website owner can't extract the content for translation. If they can't extract the original, there's no easy way to load the translated content back either. Furthermore, if the website owner can't extract the content into translatable format, it is impossible to get a proper estimate for the translation costs in time and money...

Easyling can, however, discover the website by following links and grabbing translatable and localizable content - and convert it into a translatable format. This gives a realistic view of the magnitude of the translation task, and, thanks to the translation proxy, even a partially translated site can give full user experience on the website visitor's side.  
Data can be extracted with a couple of clicks - and the publication of the translated site is similarly easy.

----------
**More specifically:**  
- Easyling easily processes HTML, and with proper configuration it can handle JavaScript/AJAX/JSON, XML
- Easyling doesn't process Flash content
- Use the X-Proxy to determine what would be currently translated. If it doesn't, use the Advanced Settings to fine-tune the JSON/XML path settings
- The crawler can discover static pages / HTML content only. You have to manually add any extra AJAX URLs, with the proper parameters.
- When you run the crawler, always use Discovery first, and be incremental: "Unlimited" really means unlimited, and as such, can yield to very-very high cost. Running an unlimited crawl on an e-commerce website is a very-very bad idea.
- Based on the initial, limited crawls, fine-tune the "Ignore query" parameters, to help the crawler decide what URLs to handle as same, and what to visit in hope of new content to be discovered.
- Always check all the forms for error messages, congratulation messages, etc.
- Check all the images; some website like to bake the text into the image. Those will require your attention.
- Pay attention to forms etc included from domains outside of Easyling. Typical examples: Marketo, optimizely.com, etc. You'll have to create new Easyling project for them, then linking together the projects.
- Never underestimate the power of injecting CSS and/or JS into the translated pages
- Regular expression is a great way to reduce the amount of content to be translated
- Do read through and watch all the available documentation:

- [https://www.youtube.com/watch?v=S47kArNiJ1o](https://www.youtube.com/watch?v=S47kArNiJ1o)
- [https://www.youtube.com/watch?v=8VsBy2bGo64](https://www.youtube.com/watch?v=8VsBy2bGo64)
- [https://gitlab.com/easyling/wikis/home](https://gitlab.com/easyling/wikis/home)
- [https://drive.google.com/open?id=0Bw53oZELMrf8V1FIUnhmNEtubTA](https://drive.google.com/open?id=0Bw53oZELMrf8V1FIUnhmNEtubTA)

- [http://lesson101.tutorial.easyling.com/](http://lesson101.tutorial.easyling.com/)
- [http://lesson102.tutorial.easyling.com/](http://lesson102.tutorial.easyling.com/)
- [http://lesson103.tutorial.easyling.com/](http://lesson103.tutorial.easyling.com/)
- [http://lesson105.tutorial.easyling.com/](http://lesson105.tutorial.easyling.com/)

Follow the monthly Release Notes, along with the frequently updated Changelog

- [https://www.easyling.com/category/blogpost/release-notes/](https://www.easyling.com/category/blogpost/release-notes/)
- [https://www.easyling.com/change-logs/](https://www.easyling.com/change-logs/)
