# Menu

## Dashboard

The Dashboard is your command center. It contains a variety of
features you can use to manage your projects. In this manual, we'll
take these options in the order that they appear in the menu on the
left side of the screen.

### Project statistcs

### Alarm

You can set up alarms to be notified of any actions in your project
that could potentially lead to undue expenses. Enter the value for the
timeout (snooze) between subsequent e-mail notifications, to prevent
the Alarm from flooding you with e-mails. After that, check one of the
alarm options and enter the limit above which you want to receive a
notification. You can set an alarm for:

**Page Views**: if you wish to detect unusually large amounts of
requests to the proxy. As Scans and Discoveries count as Page Views,
you can also use this alarm to detect if a Scan was started.

**Words added**: if you wish to receive notification about new content
that exceeds the set amount. 

**Words translated**: if you wish to receive notification about
Machine Translation or reimport events on the project.

The e-mails are sent to the owner by default, but you can add the
'Receive notification emails' right to any participant in Dashboard >
Sharing settings (see below).

### Audit log

The audit log is the minutes-taking feature of Easyling. It records
all activity on the project with a username/e-mail address attached to
each entry.

Some Audit Log entries can get quite long, such as when Page Modifier
or CSS overrides are being edited and saved multiple times. For this
reason, the Audit log displays onlythe first three lines of long
entries by default. Use the grey bar with the downward-pointing arrow
under a log entry to see the full text of that entry.

### Sharing settings

In the world of website localization, it is rare for a project to be
realized by a single person. As project owner or backup owner, use the
Sharing settings dialog to invite people into the project and assign
roles/editing roles to any one of them.

At the bottom of the Dialog, you will see the line, "Invite People:"
if you click on the field, the invitation settings part of the dialog
will slide up, allowing you to enter further details of the project
participant to be added. You can assign languages, enable admin/access
features and workflow roles for each user you invite. You can do this
by clicking on the blue plus icon next to each of those options. Make
your choices in the small pop-up lists. **These settings are not
final, you can change them later.**

The various **features**, (administrative rights) deserve to be
detailed, Here they are:

**All features**: every feature you see below the separator in the
list will be added for the user. Note that this has a potential to
cause problems: If, for example, you simultaneously set __Advanced
features__ and __Manage segments__, it results in an editing rights
conflict. There are security implications you need to consider when
giving your users rights, so use this feature with care.

**XLIFF export/import**: enables XLIFF export/import of segments for
the user. Especially important for those users who will be
coordinating the translation effort throughout the project.

**Receive notification e-mails**: Add user to the list of recipients
of Discovery/Content Scan/Alarm, etc notifications.

**Can invite others**: designates the user as a Project Manager, able
to invite others onto the project. Take care not to include other,
conflicting roles, such as __Customer__, which could re-restrict
access.

**Advanced features**: give the user the power to edit languages as
well as any entry in the project, and editing most setting, up to, and
including, the URL inclusion-exclusion rules. Segmentation, publishing
and certain advanced settings remain beyond the reach of the user.

**Manage segments**: in other words, the Customer is a special user
class, given the ability to manage (approve or exclude) pending source
segments. A user with these segments requires a workflow role and an
assigned target language to access the Workbench to manage
segments. **WARNING! This right restricts the user to this role,
other features will be disabled!**

**NOTE** __Features__ are predominantly important from a project
management viewpoint. __Workflow roles__, on the other hand, are used
to manage user interaction __on the Workbench__, based on expertise
(whether a user is a translator, proofreader or client will decide
what sets of segments are available to them for editing - see the
documentation of the Workbench for details).

After a user redeems their invitation using the link they receive in
an e-mail, their address and username will appear under the
owner. Their features and workflow roles can be edited in the list.

### Link projects

Use this function to link two projects together. For example,
__example.com__ and __blog.example.com__ are separate domains, so two
separate Projects (and Scans!) are required to create a full
translation for the site. When both projects are ready to be
published, use this function to link and serve them together on the
proxy.

### Page Cache

Caches can be one of the most useful and least understood features in
Easyling, so we dedicate a separate section for their
explanation. Please refer to it here.

### Path settings - Cache & Cookie, Content Type Overrides

You can add project paths here and define Cache and Cookie overrides
for them. Enter a new path, which you can set to be a prefix or an
exact URL, and click on Add Path. A NEw rule dropdown menu will
appear. You can choose either Cache and Cookie Overrides, Content Type
Overrides, or both. After selecting one, the dropdown will disappear,
but you'll still be able to add the other using the plus icon that
appears next to the path.

By clicking on 'Edit rule', you can set the Cache override to public,
private or ignore according to your needs. set the maxAge and override
type (whether to clear or use cookies) and you're set.

Use the Save icon next to the rule name or the blue 'Save all' button
to save your settings.

You can always return here and add new paths and rules using the 'Add
new path' button if there is a need for it.

### Advanced settings

It is not an exxageration that the Advanced settings screen is where
you can get a first taste of the advanced capabilities (the
nitty-gritty) of Easyling.

Some, such az Freezes, are general enough to warrant close attention
from all users, others, such as the Tweaks checkbox list are required
only in specific cases, so you can go through many, many projects
without ever having to worry about them. Let's take these features one
by one.

**Pattern matching**: there is often a great deal of text on a website
that is not targeted for translation, because they are highly
repetitive (usernames, dates) or numeric in nature (prices), just to
mention a few possibilities.

You can construe regular expressions and add them here, one regular
expression per line, and if that regex has a capturing group, anything
that is **matched by that capturing group** will be treated as
translation-invariable.

It is important to note that if you add regexes here later into the
project, your existing segments will remain in the Workbench. Pattern
matching does **NOT** delete any segments.

**Example: filtering usernames and dates**

Let's say you have content like the following on a site:

```
Posted by youTuTroll on Apr. 4, 13:22, 2010
Posted by joey0405 on Apr. 6, 03:29, 2010
Posted by cunning_linguist on Apr. 6, 03:45, 2010
Posted by bornToBe27 on Apr. 6, 10:01, 2010
Posted by OMEGA on Apr. 7, 11:59, 2010
```

Repetitive and inconsequential from a translation/word count
viewpoint, the usernames and dates should be made
translation-invariant. You can add a regex for it (such as the one
below) in the textbox and Easyling will exclude whatever is matched
within a capturing group.

`Posted by ([\w]+) on ([\w]{3}\.\s[0-9]{1,2},\s[0-9]{2}:[0-9]{2},\s2[0-9]{3})`

We recommend that you visit regex101.com and test your regular
expressions with example snippets before setting them on a live
project.

### Freeze

These options become important after translation has begun in
earnest. At this point, it is a good idea to __freeze__ the page list
and the segments - that is, prevent _inadvertent_ addition of new
text or pages to the list you are currently working on.

**WARNING:** These settings can be overriden via explicit user action:
adding Pages via the blue icon in the page list, or running Scans with
the appropriate settings in place.

As you based quote on a specific Discovery/Scan (in other words, a
specific state of the site at a given time), it wouldn't do to return
a few days after winning the project only to find that the news
section was expanded with two new items and you have 4500 new source
words to deal with - indelibly added to the project, but not part of
the original deal. 

You have the following options:

**Freeze pagelist**: Prevent new pages from being added to the
pagelist. If you turn this option on, you can use the various preview
modes without having to worry about new content.

**Handle unknown pages as externalized**: Pages that are not in the
pagelist will be _externalized_, that is, not translated _at
all_. Normally, if a page is not externalized, any content that is
already translated somewhere else will be _propagated_ to the new
page. By externalizing unknown pages, you let Easyling return
untranslated segments in their completely untranslated, original form.

**Freeze translation memory**: No new translatable segments will be
added to a project as long as this Freeze is turned on (automatically
enables Page Freeze).

### Translation memory

Easyling's translation memories (TM) are used to store existing
translations for segments. You can import translations from *.tmx
files or populate the translation memory with translations you have
added in the Workbench.

Type in the name of your Translation memory and click on Create. Your
TM will appear right above the input field, along with the "Add target
language" option. You can also use the dropdown menu to assign TMs
you've created previously.

Hovering over a translation memory reveals a menu, which allows you to
import/export *.tmx files or populate the TM with existing
translations. Use the "Remove" button to delete the TM.

The screen is furnished with a search field you can use to look up
segments in a TM.

### Pre-translate

By using the Pre-translate menu, you can initiate a process which
supplies untranslated segments with a preliminary translation in order
to mitigate bleedthrough on the proxied pages. You can use
pre-translate with a Translation Memory or a Machine Translation API
of your choice. Easyling supports Google Translate, iTranslate4eu,
Bing Translate and GeoFluent. 

In order to use Machine Translation, you need to go into your Account
and set up your MT account Ids/authorization keys in the "Machine
Translation" menu.

### Auto pre-translate

Auto pre-translate is self-explanatory in that it is the
automatization of pre-translate: here you can set up the project to
automatically execute a pre-translate process for any new content that
is found - you can hook it up with your TMs, or Machine Translation
services to add translations.

You can also generate Work packages from the new content at set
intervals, or send XLIFF files to external systems, such as your XTM,
XTRF, or Dropbox account. There are links at the bottom of the dialog
you can use to visit the settins screens of these accounts.

### Remove project

This is always displayed in red. By clicking on it, you remove
project. Be careful!
