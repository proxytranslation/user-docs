# Introduction

The Dashboard is your command center. It contains a variety of features you can use to manage your projects. In this manual, we'll take these options in the order that they appear in the menu on the left side of the screen.

When you open the Project Dashboard for the first time, the screen will display general project settings that we describe briefly in the following sections.

## Project Alias

The project alias will be displayed in the Project dropdown for easy identification of your projects. Project aliases are project-internal, they will not be displayed anywhere on the translated site. Feel free to change the alias anytime.

## Website Address

As it say on the tin, the website address is the domain URL that the project was created for. Once declared as part of the project creation process, this property of the Project can not be changed at all.

## Alternative Domains

It happens sometimes that a website serves content both on the `www` subdomain and the naked domain, such as `example.com`. In these cases, it is useful to set things up over the proxy so that the different URLs are handled similarly.

After creating a project, this field is automatically filled with the complement of the Website Address. Add any further subdomains that contain identical content to this list. Separate them with commas.

## Basic Authentication

Not to be confused with the project Access Control features of the proxy, the Basic Authentication username and password fields can be used to authenticate to the project website through the proxy. If the original site asks for a login in the following fashion: 

![Basic Authentication](/img/basic-authentication.png)

If a username and password is provided here, the proxy will use this info from then on. In some cases, this is a necessity - Discoveries and Scans will need the authentication info to be operational. It also saves you the trouble of having to log in over the variety of proxy preview modes.

## Project workflow

Change the number of project participants and project workflow type using this dropdown. See [Collaboration](/workbench/workflow/workflow.html). 

## Staging Domain 

Please see the Cookbook recipe [on Staging domains](../../cookbook/stagingdomain.html)


## Language Selector

