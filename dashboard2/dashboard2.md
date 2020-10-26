# Introduction - Project overview

The Dashboard 2.0 is your new and improved command center. It contains a variety of features you can use to manage your projects. In this manual, we'll take these options in the order that they appear in the menu on the left side of the screen.

When you open the Project overview, the screen will display a few general settings described below. Depending on your rights on the project, some of these may be hidden from you.

## Project info

![Project info](/img/dashboard2/project_overview/project_info.png)

This card displays the key properties of your project. They are the following:

- **Domain**: Exactly what it says on the tin, the website address is a property of your project that cannot be altered once declared during project creation. 

- **Project code**: An 8 character long identifier that's unique to your project. It can be used to track projects and is necessary when you ask help at our support email address.

- **Source language**: The language you translate from. It can't be changed after the fact.

- **Project created**: The creation date of your project.

- **Project alias**: This alternative name will be displayed in the Project dropdown below the URL, for easy identification of your projects. Project aliases are project-internal, they will not be displayed anywhere on the translated site.

- **Alternative domains**: Sometimes a website serves content both on the `www` subdomain and the naked domain, such as `example.com`. In these cases, it is useful to set things up over the proxy so that the different URLs are handled
 similarly. <br />
  After creating a project, this field is automatically filled with the complement of the Domain. Add any further subdomains that contain identical content to this list. Separate them with commas.
  
You can also use this card to delete or remove the project. Only the owner can delete a project completely. If you were simply invited but aren't the owner and you 'remove' a project, you will simply be removed from it.

## Project wallet

![Project wallet](/img/dashboard2/project_overview/project_wallet.png)

This card shows you information on the wallet of the project you are viewing. In most cases, this is the wallet of the user who created the project. You can see if it is expired and the remaining balance and let the user know if they
 need to top up.
 
## Statistics
 
![Statistics](/img/dashboard2/project_overview/statistics.png)
 
Here you can see the number of served requests and words added to your project recently. For more information, click the 'Go to statistics' button.
 
## Miscellaneous options
 
![Misc options](/img/dashboard2/project_overview/misc_options.png)
 
On this card, you have a couple of options that are the set once and forget kind. You may need to reference these settings later so it's handy that they are present here.
 
- **Project workflow**: Change the number of project participants and project workflow type using this dropdown. See [Collaboration](/workbench/workflow/workflow.html) for more information.
 
- **Gateway domain**: If the site you wish to translate has a strict firewall that blocks the proxy, the admins can set up a gateway for you. In this case, all of the requests go through that gateway and will arrive to the origin server
  from a fixed IP address that can be whitelisted. Here you can see whether the gateway is enabled.
  
- **Segmentation**: Whether the segmentation rules are applied to new segments that are added to the project. As this has the potential to break the project, not even the owner can change it. If you wish to have it disabled, please
   contact the support team about it.
   
- **Manual publishing**: It is an advanced project control feature that gives project owners the ability to hold back the translations from being published on the live page (but not the preview, as it will always display the latest
 translation available!) until further notice. <br />
Once activated, a new item will appear in the Bulk Actions menu of the Workbench, “Publish”. Selecting this action will cause all selected segments to be synchronized with their displayed translations, and once the action finishes, the
 markers in the status bar on the right of the entries will change to reflect this.
 
## Crawl settings

![Crawl settings](/img/dashboard2/project_overview/crawl_settings.png)

Settings that affect the way crawls work:

- **Process pages in source language only**: For every segment it encounters, the crawler uses Google's language selector API to determine whether it is in the selected source language. As this is a paid API, you must supply a key to use
 it.
 
- **Ignore queries**: By default, the crawler treats `example.com/?query=example1` and `example.com/?query=example1` as different pages. Adding `query` here will prevent this behaviour. It will treat the 2 pages if they were exactly the
 same.

- **Group pages by ignoring query parameters**: The crawler will visit both `example.com/?query=example1` and `example.com/?query=example1` but segments will be treated as coming from the same page (`example.com` in this case).

## Staging domains

![Staging domains](/img/dashboard2/project_overview/staging_domains.png)

Although it is true that the project address cannot be changed after the project is created, the Staging domain feature can still be used to change the origin server to which requests are sent.

For details, please see the Cookbook recipe [on Staging domains](./../cookbook/stagingdomain.html)

## Documentation

![Docs](/img/dashboard2/project_overview/docs.png)

A set of links pointing here so that it's always at hand.

## Crawl info

![Crawl info](/img/dashboard2/project_overview/crawl_info.png)

Some information on the latest crawl ran on the project. It is the same info you'd find on the right side of the [Crawl list](crawler/crawllist.html).

## Linked projects

![Linked projects](/img/dashboard2/project_overview/linked_projects.png)

If content is coming from multiple domains, you'll need to create multiple projects to translate them. To make sure that links between the projects are accurate, you must link them. Note that **links must be bidirectional** meaning that
 you must link one project 1 to project 2 and then go to the Dashboard of project 2 and link it to project 1 and that both projects must be published separately.
 
## Target languages

![Target languages](/img/dashboard2/project_overview/target_language.png)

Here you can see the current target languages and add more if you wish to.

## Referred domains

![Referred domains](/img/dashboard2/project_overview/referred_domains.png)

This is a list of the external domains that the Crawler encountered. These are sites that the original site relies on (e.g. to embed YouTube videos, maps or for analytics) or links to.

## Content timeline

![Content timeline](/img/dashboard2/project_overview/content_timeline.png)

This list contains the main events where content was manipulated on the project. These include crawls, content exports and imports as well as the creation of Work packages.

## Database word & repetition analysis

![Database word & repetition analysis](/img/dashboard2/project_overview/analysis.png)

Here you can see the number of words and repetitions on the site as found by the crawl specified on the bottom. Note that the data may be outdated if the crawl is outdated. You can use the 'Update' button to fill the chart with fresh
 data (or old, if you wish). 