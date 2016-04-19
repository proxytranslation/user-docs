+ [[Workflow overview|Getting-started#getting-started]]  
   - [[Creating a project|Getting-started#creating-a-project]]  
  
   - [[Discovering the site|Getting-started#discovery]]  
  
   - [[Extracting content for translation|Getting-started#scanning]]  

   - [[Translation|Getting-started#translation]]  
  
   - [[Maintenance|Getting-started#maintenance]]

+ [[Sales tool for LSPs and freelancers|Getting-started#sales-tool-for-lsps-and-freelancers]]

+ [[Basic concepts|Getting-started#basic-concepts]]
  
| Workflow overview |
|-------------|
|[[https://github.com/easyling/public/wiki/img/workflow.jpg|alt=Workflow overview|thumb]]|  

##Getting started##
To use easyling, first you need to register and set up an account for the service: [https://app.easyling.com](https://app.easyling.com). You can register with your e-mail address or with an external account (XTM, Google or Yahoo), free of charge. A free one-month trial is also available, with access to all features, and a budget of 10 EUR.  

Right after registration you can start using the service. When you log in for the first time, you can select if you are a Website owner, a Freelance translator or a Language Service Provider. This is for statistical purposes only, it has no influence at all on the User Experience later on. The actual work starts with creating your first project. To do this, please click on **Create new project** and choose **Add project** from the drop-down menu. 
 
| Add project |
|-------------|
|[[https://github.com/easyling/public/wiki/img/create.jpg|alt=Create|thumb]]|  
 
###Creating a project###
This opens the **Add project** dialog box, where you can enter the URL of the website you would like to translate, and also select the website language; this sets the source language of the translation project.  
  
   
| Add project dialog |
|-------------|
|[[https://github.com/easyling/public/wiki/img/add.jpg|alt=Add project]]|  
  
The **Start discovering automatically** option is selected by default. ***Discovery*** is the preliminary assessment of the website, without storing the website content. This process starts from the URL you specified, scans all the pages, follows all links, and returns the URL list of the visited pages, together with the wordcount and repetition rates. As Discovery costs 1EUR per thousand pages, you may want to disable automatic discovery. You can run discovery manually at any later time. You can disable automatic discovery by removing the check mark.  
You can also select **Process pages in source language only** to restrict translatable pages; this feature is particularly useful for websites where content in different languages is mixed, without clear language distinction in the URL. Before using this option for the first time, you have to set up the Google Translate API by clicking on the link there. Please note that Google Translate API is available only as a paid service, and you need your own account.  

You can also use **Advanced options** to refine discovery. These include:  
- **Check if the domain redirects to another domain** - when creating the project, Easyling will first check for redirections. By disabling this option, you can force the creation of the project tot he domain you specify, regardless of its existence or redirection settings. However, the root page (`/`) will not be added by default!  
- **Include pages only starting with** - here you can limit discovery to a specific set of pages, like company  or contact information, services, products, etc. You can remove or add pages at any later stage, and you can remove this restriction as well.  
- **Ignore these paths** - here you can exclude pages that you don't want to be assessed, like blog, forum and news entries. These are typical examples of pages where an enormous amount of irrelevant or outdated information can accumulate as years pass. Any page excluded here, upon project creation, can later be included in the project, if needed.   
- **Provide custom SRX file** - easyling uses its own language-specific segmentation rules, but you also have the option to use your preferred rules, by uploading your own [.SRX file](https://en.wikipedia.org/wiki/Segmentation_Rules_eXchange). Please note that segmentation rules can't be modified once the project is created.  
  
| Advanced options |
|-------------|
|[[https://github.com/easyling/public/wiki/img/add_advanced.jpg|alt=Advanced options]]|  
  
###Discovery###
You can run Discovery of the site automatically when you create the project, or at any later time manually from the Dashboard. 

| Run discovery |
|-------------|
|[[https://github.com/easyling/public/wiki/img/discovery.jpg|alt=Run discovery]]|  
  
The process maps the structure of the site by scanning each page for link elements and trying to follow these links. The content of the website is not stored, only the URL address of the visited pages, together with their status info. Any page that is verified to exist is marked as **Discovered**, and the ones that returned an error message (most commonly *redirection* (HTTP301-302) and *page not found* (HTTP404)) are marked **Unvisited** in the list. For more information on HTTP status codes, see [here](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes "HTTP Status Codes on Wikipedia").  
Although this process doesn't extract content, it provides a preliminary wordcount and a repetition rate as well. It has a cost of 1EUR per thousand pages.  
  
Once the discovery is ready, you receive an e-mail notification, and the statistics is updated on the Discovery page. Based on the results you can give a rough estimation for the website translation cost - both in time and money.  
  
Discovery also collects ***resources*** from the website, like images, downloadable files, etc. You can find them under Discovery > Resources.  
Please note that the translation/localisation of these resources is not done by easyling, which means that the **content** of these resources is not extracted for translation. You have the option to replace them with the localised version for every language, and you can also replace external links.

You can then remove or add pages to be translated, and run another discovery of the site with the new restricted or broadened options, or you can proceed to the next step, to extract content for translation.
 
###Scanning###
Scanning is practically extracting content from the website for translation. You can initiate it under Content. The process is similar to Discovery, but this time content is stored, and this process costs 2EUR per thousand *source* words. Once again, you will receive an e-mail notification once content extraction is ready. You will again receive a list of URL addresses, and the status of the pages will change to **NEW** after extraction. 

| Scanning |
|-------------|
|[[https://github.com/easyling/public/wiki/img/scan.jpg|alt=Scanning]]|  
 
  
###Translation###
Once content is extracted, you can start translating the website to the chosen language(s). You can add target languages to your project on the Dashboard, under Languages.  
  
| Adding a target language|
|-------------|
|[[https://github.com/easyling/public/wiki/img/add_target_language.jpg|alt=Add target language]]|  
  
You can use the online editor interface right from the dashboard, or you can also choose to export the bilingual file for translation in a CAT (Computer Aided Translation) tool. Easyling supports the standard XLIFF format, and also offers some pre-configured export options for the most commonly used CAT-tools.  
  
  
| XLIFF export|
|-------------|
|[[https://github.com/easyling/public/wiki/img/export_bilingual.jpg|alt=XLIFF export]]|  

Once translation is ready, you can import the translated XLIFF back to review and check the layout on the online editor interface in Highlight View, and make all the necessary correction. Your translated website is ready for publishing.  
  
###Maintenance  
As content is regularly added to websites, website translation is a never-ending task. Maintenance is checking for new content on the website, extracting it for translation, and uploading the translated content. It is also possible to automate checks and content extractions: you can specify the frequency of the checks (daily, weekly, monthly), and if new content is added, easyling automatically extracts it and sends you an e-mail notification. Please note that this automation is not possible behind secure login. 

  
| Scheduled scan|
|-------------|
|[[https://github.com/easyling/public/wiki/img/scheduledScan.jpg|alt=Scheduled scan]]|

Additionally, if a new page, or page with new content is visited through the proxy, either on the live serving domain or in Preview, that content is automatically extracted, and an email notification is sent to the project owner.     
    
  
###Sales tool for LSPs and freelancers###
  
Easyling also offers a Sales Tool to help LSPs and freelancers in growing their business.   
If you have a well-defined group of potential customers you'd like to offer your translation services to, like hotels or restaurants with only monolingual websites in your area, easyling makes it easy for you to impress the business owners. Just collect the URL addresses, add them to the Sales Tool, and easyling will automatically create a project for all webpages according to the settings you specify. Once the translation and post-editing of the translated main pages are ready, you can send a link to the business owners. If your potential clients are impressed with the translated page and the fact that no IT involvement is required on their end, you have a better chance to win the deal. 
For more information see our [blog](https://www.easyling.com/blog/try-sales-tool-lsps-freelancers/) or this short [video] (https://www.easyling.com/features/mass-sales-tool/)  

###Basic concepts###
  
| Term | Definition|  
|:-----|--------|  
| Scan | Extracting content from the website for translation |  
| Discovery|Checking the website for translatable content|  
| Resource | Binary content found on the website (images, PDFs, CSS and JS files, etc.) |  
| Workbench | The online editing view of easyling |  
| List view | The main view of the Workbench; a simple editor for online translation|  
| Highlight view | The secondary view mode of workbench, allowing for in-context editing | 