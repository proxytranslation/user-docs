# Collaboration

Collaboration are a must with website localization. If you have used the Dashboard's Sharing settings to invite other people into the project, granted them the appropriate editing rights, the list of segments in the Workbench will look a bit different to each user.

## Workflow Roles

As mentioned previously, oles are predominantly a project management feature associated with work on the Workbench. To reiterate, there are four different roles:

![Workflow Roles](/img/workbench/workflow_tags.png)

**T** - Translator (default)

**P** - Proofreader

**Q** - Proofreader 2 (**Q**uality Check)

**C** - Customer (or **C**lient)

There are four different workflows on the proxy you may employ. You may set these on the Dashboard.

- Simple Translation Workflow (**T**)

- Translation + Proofreading (**TP**)

- Translation + Proofreading + Client Approval (**TPC**)

- Translation +Proofreading + Quality Check + Client Approval (**TPQC**)

Each setting will activate the necessary roles, which the Owner or Backup Owner may assign to any project participant. By default, only the Translator role is required. Owners have access to all workflow roles.

### Workflow Roles in Action

Use the Workflow role dropdown in the toolbar to switch between the available Workflow roles:

![Workflow Role Dropdown](/img/workbench/workflow_role_dropdown.png)

Take TPQC, the workflow with the most participants, for example.

1. Each **approved** segment is assigned to the Translator role.

2. When finished with a segment (either through manual edits, automatic translation or via XLIFF importing), the translator clicks on the Confirm tick to declare that segment cleared for that phase and send it to the next role, the _proofreader_.

3. The _proofreader_ (and much everyone else) may use Filters to display only those segments that are assigned to that role. He takes the segments sent by the Translator, edits them, changes their wording as required. When finished with an entry, the _proofreader_ clicks on the Confirm tick, sending the segment along to _Quality Check_.
   
And so on. This cycle is then repeated until a segment (more to the point, _all_ segments) reach the final workflow role, that of the Customer, who approves translated entries.

A few things to keep in mind:

- Each Role has access to the lists of **upstream** roles.

- Only Owners, Backup Owners and Project Managers have access to **all** roles.

- Entries/segments belonging to another role are **greyed out**.

- A segment remains available for editing after Confirming it just as long as it is not touched by the next Workflow role. If you ever mistakenly Confirm an entry, you may, so to speak, **reclaim** it for some more work before the next role can get to it.
  
And that's about it!

## Work Packages

If Workflow Roles is a method of grouping your users, then Work Packages are a method of grouping segments. See the Dashboard chapter for the details of how to generate them.

Use the Work Package dropdown to select a Work package, and the Workbench will display only those Entries that belong to that Work Package (note that an Entry may belong to more than one Work Package!). The dropdown looks like this.

![Work Package Dropdown](/img/workbench/work_package_dropdown.png)

The only default entry in the dropdown is "All", which means disabling Work Package based filtering on the Workbench. As new Work packages are generated, this list will automatically update after refreshing the window. The dropdown will always contain the names of the 100 latest Work Packages.

Clicking on "Manage workpackages..." will take you to the Dashboard where you can tend to your existing Work Packages or generate new ones.
