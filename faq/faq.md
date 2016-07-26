# FAQ

## General

### **Some parts of a site are on a subdomain. How will the crawler pick them up?**

The sites www.company.com and blog.company.com are treated as separate domains by the crawler. From the vantage point of a crawler running on www.company.com, a path on blog.company.com is an external and will be treated as such. The solution is to create two separate projects and link those with each other.

### **The Discovery went beyond the limit I set. Why?**

A crawl will finish the current round and visit the redirects and links on the last page. If it took the limit too literally, that could potentially result in trailing links being thrown out.

### **Can I get page-specific repetition statistics?**

Repetition statistics make the most sense in a site-wide context. The problem with controlling calculations on a per-page basis is that it is not true to life to call a segment on a given page a “canonical instance”. Take a navigation bar or a footer, for example. It will be “repeated” on all pages, but it cannot be said to “belong” to any one of them. Easyling stores the first instance it comes across and then propagates its translation to all other instances.

### **The page I'm trying to translate has prices. What can I do to handle local currencies?**

The prices themselves can be made translation-invariable, but real-time price handling for different currencies will have to be implemented by the client on the source site, making it possible for the proxied site to access the locale-specific information. Pricing of products and services also has legal / market implications that are beyond the tasks of LSPs. Of course, once currency-specific information is accessible from the original site, we are happy to help with integrating any backend calls / ajax requests on the proxy.

### **How do I enable automated scan on my project?**

To enable automated content extraction on your site, please go to Content, and choose either of the daily, weekly or monthly options in the drop-down next to the Look for changes option.

### **Is it possible to set up automated scanning behind secure login?**

No, scanning can't be automated behind secure login. For such processes you need to [extract cookies](secure-login.html) with you browser's dev. tools and pass them on to the proxy. Some cookies get invalidated over time, and we don't store cookies either.

## Caches

### **Can I preview newer content on the workbench without causing bleedthrough on the published site?**

You can customize which Source Cache to use on which proxy mode - go into Page Cache, choose custom settings and select Disabled from the dropdown menu. The preview mode will display all new content. It is recommended that you keep TM Freeze turned on while exploring the new content, otherwise everything will be automatically added to the Workbench.

### **Does building a Source Cache cost any money?**

You can use Content Scan with the appropriate options checked to build your Source Cache. As long as there is no new content to pick up, Scan costs the same as a Discovery.

### **How can I check if a page uses the Source Cache?**

Go into **Pages view** in the Dashboard. If you hover with the mouse over a page in the list, you will see a **Cache** button. Click on it to verify Source Cache information for that page. If there is no Source Cache for that page, you will see the following screen:

[[Source cache does not exist]]

### **Does building a Target Cache cost any money?**

Setting aside the inherent cost of the Page Visits you have to accrue to build them, Target Caches are free of charge.
