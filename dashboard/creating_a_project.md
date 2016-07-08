You can create a new project with the **Add Project** dialog, using the dropdown menu on the Dashboard's top toolbar.  

![Create Project](img/create.png)  

This opens the **Add project** dialog box, where you can enter the URL of the website you would like to translate, and also select the website language; this sets the source language of the translation project.  


**Add project dialog:**

![Add project](/img/add-discovery.png)  

The **Start discovering automatically** option is selected by default.<br>***Discovery*** is the preliminary assessment of the website, without storing the website content. This process starts from the URL you specified, scans all the pages, follows all links, and returns the URL list of the visited pages, together with the wordcount and repetition rates. As Discovery costs 1EUR per thousand pages, you may want to disable automatic discovery. You can run discovery manually at any later time. You can disable automatic discovery by removing the check mark.  
You can also select **Process pages in source language only** to restrict translatable pages; this feature is particularly useful for websites where content in different languages is mixed, without clear language distinction in the URL. Before using this option for the first time, you have to set up the Google Translate API by clicking on the link there.   
***Please note that Google Translate API is available only as a paid service, and you need your own account.***  
  
**If you don't have a Google Translate API subscription, and the content is mixed, all content will be discovered and treated as if it was in the project source language.**

You can also use **Advanced options** to refine discovery. These include:  
- **Check if the domain redirects to another domain** - when creating the project, Easyling will first check for redirections. By disabling this option, you can force the creation of the project tot he domain you specify, regardless of its existence or redirection settings. However, the root page (`/`) will not be added by default!  
- **Include pages only starting with** - here you can limit discovery to a specific set of pages, like company  or contact information, services, products, etc. You can remove or add pages at any later stage, and you can remove this restriction as well.  
- **Ignore these paths** - here you can exclude pages that you don't want to be assessed, like blog, forum and news entries. These are typical examples of pages where an enormous amount of irrelevant or outdated information can accumulate as years pass. Any page excluded here, upon project creation, can later be included in the project, if needed.   
- **Provide custom SRX file** - Easyling uses its own language-specific segmentation rules, but you also have the option to use your preferred rules, by uploading your own [.SRX file](https://en.wikipedia.org/wiki/Segmentation_Rules_eXchange). Please note that segmentation rules can't be modified once the project is created.  

#### Advanced options in the Add Project dialog

##### Exclusion and inclusions rules on project creation:

These are the settings you specify under **Include pages only starting with** and **Ignore these paths**. You can input page inclusions and exclusions when you already have a concept before running a Discovery - e.g. a potential client asked for a quote by specifying the pages to be translated (or to be left out from translation).  
If you don't have a preliminary idea, or the initial discovery indicated a much higher volume than expected, this refining can be done later using the rules editor under Discovery / Pages or Content / Pages.

##### Provide custom SRX file:

Working with custom SRX files might be necessary in certain cases, like special requirements from clients, but more commonly for migration purposes.  
Some clients might require the use of custom segmentation rules to optimize website content segmentation to their existing translation memories. It is not uncommon that business owners already have product catalogs and other business-related materials translated before they decide to have their website translated as well - and it is a sound business idea to re-use existing resources to the most possible extent. To meet this requirement you can use the client's own segmentation rules for your projects.<br>  
It is not uncommon either that clients switch from one platform or service provider to another, and wish to migrate all their existing data - including their website content. This, again, might require the use of custom segmentation rules, so that existing resources could be re-used.<br>  
<br>As segmentation rules can't be modified once the project is created, please make sure to check if your client has any special segmentation requirements.

**Screenshot of the dialog:**

![Add Project dialog](/img/add-project.png)
