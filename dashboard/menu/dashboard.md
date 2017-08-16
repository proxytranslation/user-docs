# Introduction

The Dashboard is your command center. It contains a variety of features you can use to manage your projects. In this manual, we'll take these options in the order that they appear in the menu on the left side of the screen.

When you open the Project Dashboard for the first time, the screen will display a few general settings described below.

## Project Alias

This alternative name will be displayed in the Project dropdown below the URL, for easy identification of your projects. Project aliases are project-internal, they will not be displayed anywhere on the translated site.

## Website Address

The website address is a property of your project that is unchanging. Once declared in the Add Project dialog, it cannot be altered.

There is one exception to this rule: by default, the proxy will follow redirects from the initial URL and will create the project for the address it is redirected to.

## Alternative Domains

It happens sometimes that a website serves content both on the `www` subdomain and the naked domain, such as `example.com`. In these cases, it is useful to set things up over the proxy so that the different URLs are handled similarly.

After creating a project, this field is automatically filled with the complement of the Website Address. Add any further subdomains that contain identical content to this list. Separate them with commas.

## Basic Authentication

Not to be confused with the project Access Control features of the proxy, the Basic Authentication username and password fields can be used for automatic authentication on the project website. Basic Authentication windows typically look like this: 

![Basic Authentication](/img/basic-authentication.png)

If a username and password is provided on the Dashboard, the proxy will rely on this information from then on. Use this option to enable Discoveries and Scans to work properly on these sites. The various Preview proxy modes will also rely on this authentication info to get past the login screen automatically. 

## Project workflow

Change the number of project participants and project workflow type using this dropdown. See [Collaboration](/workbench/workflow/workflow.html).

## Staging Domain

Although it is true that the project address cannot be changed after the project is created, the Staging Domain feature can still be used to change the origin server to which requests are sent.

For details, please see the Cookbook recipe
[on Staging domains](./../cookbook/stagingdomain.html)

## Language Selector

Select one or more from the available target languages to translate source language content.

Most useful translation facilities, such as the Workbench or the various instant preview features remain unavailable as long as there is no target language on a project.

You can remove or add target languages at any time. Note, however, that it is *not recommended* that you change the source language on a project that is published with translations.
