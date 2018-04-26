# Link projects

A proxy project supports translation of content on the project for which it was created, or the staging server that is set up for it. Any content coming from domains other than these has to be translated via a separate project.

`example.com` and `blog.example.com` are separate domains and separate projects are required to create an integrated translation for the whole.

Provided that each is set up appropriately, the proxy can make such related projects aware of each other using the Project Linking feature. This **enables the cross-mapping of URLs on the linked projects**. Where `example.com` referred to `blog.example.com` before, after linking, all URLs pointing to the latter will be mapped to its published target language domain.

The dialog for linking consists of a single input field:

![Link Projects](/img/link_project_dialog.png)

Copy & paste the linked project's project code into the field. Linking requires changes on each affected project, so it is recommended that you open all of them in separate tabs for this process.

Some projects are complex enough to warrant linking multiple auxiliary projects to them. You can cadd multiple projects codes to the field, separated by a colon.

A few restrictions apply to project linking:

- project linking is **two-way**: project A has to be linked on project B and then project B has to be linked on project A to complete the process.

- **refresh** the corresponding Dashboards of each project after saving in the linking dialog to ensure that each project is notified of the attempt to or completion of the linking.

- only a user who is **owner of all involved projects** can link them.

- linked projects have to be **published together** and with the **same target languages**.

## Project Linking & Forms

**Form** solutions tend to use content from external domains. The localization of **HubSpot forms**, for example, is a frequent and somewhat challenging use case of project linking.

The topic of translating such content using proxy features only is covered in detail [on this cookbook page](../../cookbook/hubspotforms.html).
