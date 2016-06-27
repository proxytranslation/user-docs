# Getting Started With Easyling

## In a nutshell
  
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

- Follow the monthly Release Notes, along with the frequently updated Changelog

  - [https://www.easyling.com/category/blogpost/release-notes/](https://www.easyling.com/category/blogpost/release-notes/)
  - [https://www.easyling.com/change-logs/](https://www.easyling.com/change-logs/)


## Workflow overview

The standard translation workflow for an LSP consists of 3 main phases: quoting, translation and delivery. However, this workflow does not really fit the website translation task, as in this case the source, the website itself, might change by the time the first translation is ready. In this case the website lifecycle has to be taken into consideration: planning, implementation, publishing, maintenance and update.<br> 
To reflect this we created the following workflow:

![Workflow overview](/img/workflow.png)  

The first 2 phases, Prepare and Discovery, correspond to the quoting phase of LSPs, and the planning phase of the website lifecycle. In these 2 phases you get a thorough understanding of the site structure, and get an exact wordcount.<br>

The next 2 phases, Scanning (content extraction) and Translation correspond to the translation and implementation phases. The web content is extracted in a translation-ready format, and the contend goes through the standard translation and proofing workflow. Once it is done, the content is ready for delivery / publishing.<br>

In case of website translation the workflow does not stop here, when the translated site goes live. The translation is served through the proxy and new content might be added to the original site any time, so it needs the Maintenance phase as well.


## Getting started

To use Easyling, first you need to register and set up an account for the service: [https://app.easyling.com](https://app.easyling.com). You can register with your e-mail address or with an external account (XTM, Google or Yahoo), free of charge. A free one-month trial is also available, with access to all features, and a budget of 10 EUR.  

Right after registration you can start using the service. When you log in for the first time, you can select if you are a Website owner, a Freelance translator or a Language Service Provider. This is for statistical purposes only, it has no influence at all on the User Experience later on. The actual work starts with creating your first project. To do this, please click on **Create new project** and choose **Add project** from the drop-down menu.

**Add project:**

![Create|thumb](/img/create.png)  

## Creating a project

This opens the **Add project** dialog box, where you can enter the URL of the website you would like to translate, and also select the website language; this sets the source language of the translation project.  


**Add project dialog:**

![Add project](/img/add.png)  

The **Start discovering automatically** option is selected by default.<br>***Discovery*** is the preliminary assessment of the website, without storing the website content. This process starts from the URL you specified, scans all the pages, follows all links, and returns the URL list of the visited pages, together with the wordcount and repetition rates. As Discovery costs 1EUR per thousand pages, you may want to disable automatic discovery. You can run discovery manually at any later time. You can disable automatic discovery by removing the check mark.  
You can also select **Process pages in source language only** to restrict translatable pages; this feature is particularly useful for websites where content in different languages is mixed, without clear language distinction in the URL. Before using this option for the first time, you have to set up the Google Translate API by clicking on the link there. Please note that Google Translate API is available only as a paid service, and you need your own account.  

You can also use **Advanced options** to refine discovery. These include:  
- **Check if the domain redirects to another domain** - when creating the project, Easyling will first check for redirections. By disabling this option, you can force the creation of the project tot he domain you specify, regardless of its existence or redirection settings. However, the root page (`/`) will not be added by default!  
- **Include pages only starting with** - here you can limit discovery to a specific set of pages, like company  or contact information, services, products, etc. You can remove or add pages at any later stage, and you can remove this restriction as well.  
- **Ignore these paths** - here you can exclude pages that you don't want to be assessed, like blog, forum and news entries. These are typical examples of pages where an enormous amount of irrelevant or outdated information can accumulate as years pass. Any page excluded here, upon project creation, can later be included in the project, if needed.   
- **Provide custom SRX file** - easyling uses its own language-specific segmentation rules, but you also have the option to use your preferred rules, by uploading your own [.SRX file](https://en.wikipedia.org/wiki/Segmentation_Rules_eXchange). Please note that segmentation rules can't be modified once the project is created.  

**Advanced options:**

![Advanced options](/img/add-advanced.png)  

## Word count for a proposal

To get the word count you need the function called Discovery. You can run Discovery of the site automatically when you create the project, or at any later time manually from the Discovery menu.

**Run discovery:**

![Run discovery](/img/discovery.png)  

The process maps the structure of the site by scanning each page for link elements and trying to follow these links. The content of the website is not stored, only the URL address of the visited pages, together with their status info. Any page that is verified to exist is marked as **Discovered**, and the ones that returned an error message (most commonly *redirection* (HTTP301-302) and *page not found* (HTTP404)) are marked **Unvisited** in the list. For more information on HTTP status codes, see [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes "HTTP Status Codes on Wikipedia").  
Although this process doesn't extract content, it provides a preliminary wordcount and a repetition rate as well. It has a cost of 1EUR per thousand pages.  

Once the discovery is ready, you receive an e-mail notification, and the statistics is updated on the Discovery page. Based on the results you can give a rough estimation for the website translation cost - both in time and money.  

Discovery also collects ***resources*** from the website, like images, downloadable files, etc. You can find them under Discovery > Resources.  
**Please note that the translation/localisation of these resources is not done by Easyling**, which means that the ***content*** of these resources is not extracted for translation. You have the option to replace them with the localised version for every language, and you can also replace external links.

You can then remove or add pages to be translated, and run another discovery of the site with the new restricted or broadened options, or you can proceed to the next step, to extract content for translation.

## Source content extraction

Content extraction is called Scanning in Easyling. You can initiate it under Content. The process is similar to Discovery, but this time content is stored, and this process costs 2EUR per thousand **source words**. Once again, you will receive an e-mail notification once content extraction is ready. You will again receive a list of URL addresses, and the status of the pages will change to **NEW** after extraction.

**Scanning:**

![Scanning](/img/scan.png)  


## Translation

Once content is extracted, you can start translating the website to the chosen language(s). You can add target languages to your project on the Dashboard, under Languages.  

**Adding a target language:**

![Add target language](/img/add-target-language.png)  

You can use the online editor interface right from the dashboard, or you can also choose to export the bilingual file for translation in a CAT (Computer Aided Translation) tool. Easyling supports the standard XLIFF format, and also offers some pre-configured export options for the most commonly used CAT-tools.  


**XLIFF export:**

![XLIFF export](/img/export-bilingual.png)  

If you use the online editor you have visual feedback all along the translation process. You can also get live preview during transtation time in certain CAT tools. 

## In-context review and fine-tuning

If you decided to do the translation in an external tool or in the List View of the online editor, you need to check how your translation fits the original layout. Once translation is ready, you can import the XLIFF back to review and check the layout on the online editor interface in Highlight View, and make all the necessary correction. Your translated website is ready for publishing.  


## Maintenance

As content is regularly added to websites, website translation is a never-ending task. Maintenance is checking for new content on the website, extracting it for translation, and uploading the translated content. It is also possible to automate checks and content extractions: you can specify the frequency of the checks (daily, weekly, monthly), and if new content is added, Easyling automatically extracts it and sends you an e-mail notification. **Please note that this automation is not possible behind secure login.**


**Scheduled scan:**

![Scheduled scan](/img/scheduledScan.png)  

Additionally, if a new page, or page with new content is visited through the proxy, either on the live serving domain or in Preview, that content is automatically extracted, and an email notification is sent to the project owner.     


## Sales tool for mass quoting

Easyling also offers a Sales Tool to help LSPs and freelancers in growing their business.   
If you have a well-defined group of potential customers you'd like to offer your translation services to, like hotels or restaurants with only monolingual websites in your area, easyling makes it easy for you to impress the business owners. Just collect the URL addresses, add them to the Sales Tool, and easyling will automatically create a project for all webpages according to the settings you specify. Once the translation and post-editing of the translated main pages are ready, you can send a link to the business owners. If your potential clients are impressed with the translated page and the fact that no IT involvement is required on their end, you have a better chance to win the deal.
For more information see our [blog](https://www.easyling.com/blog/try-sales-tool-lsps-freelancers/) or this short [video] (https://www.easyling.com/features/mass-sales-tool/)  

## Pricing

Our pricing follows the 'pay-as-you-go' model, so you only get charged for what you use. The total cost is made up 2 types of fees: one-time fees and a monthly charge.

You pay the following one-time fees:
- Discovery: every time you run a discovery, a **1 EUR or 1.2 USD / 1000 pages** charge is applied
- Scan: content extraction costs **2 EUR or 2.4 USD / 1000 source words**
- Translation Memory: storing your (human or machine) translation in the database costs **10 EUR or 12 USD / 1000 source words / target language**
 
Content extraction and translation memory fees apply only once, so 102% repetitions are not counted. Once content is stored, every subsequent scan will treat it as repetition, so no additional charges will apply.

The monthly fee:
- for serving the translated site you pay a **1 EUR or 1.2 USD / 1000 page views** monthly proxy fee
 
For this fee you get a guaranteed 99.99% website availability, and a capacity to handle practically unlimited traffic. You also have the option to serve the translated site from your server (no proxy fee will apply), but in this case availability and traffic handling depends on your infrastructure.

## Terminology

***Scan*** <br>Extracting content from the website for translation<br>  

***Discovery*** <br>Checking the website for translatable content<br>  

***Resource*** <br>Binary content found on the website (images, PDFs, CSS and JS files, etc.)<br>  

***Workbench*** <br>The online editing view of Easyling<br>  

***List view*** <br>The main view of the Workbench; a simple editor for online translation<br>  

***Highlight view*** <br>The secondary view mode of workbench, allowing for in-context editing<br>  

***Bleedthrough*** <br>When newly added, untranslated content appears on the translated site in the original language<br>  

***Keep cache strategy*** <br>The strategy used to avoid bleedthrough. The last fully translated version is available on the translated pages, and new content is only added when the translation is ready<br>  

***Exclusion rule*** <br>A rule specified for explicitly excluding pages from the translatable list<br>  

***Inclusion rule*** <br>A rule specified for explicitly including pages in the translatable list<br>  

***Page freeze*** <br>No new items can be added to the page-list marked for translation<br>  

***Dictionary freeze*** <br>No new items can be added to the translation memory. Only available when Page freeze is activated.<br>  

***102% match*** <br>Strong contextual repetition. Every single segment within a block is a 101% match, and all tags are identical.<br> 

***101% match*** <br>Contextual repetition. Tags within the segment and the neighbouring segments are repetitions / exact matches as well.
