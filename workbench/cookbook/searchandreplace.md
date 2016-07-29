# Seach & Replace

## Tutorial 1: Fix Spelling (String Replacement)

A simple use case of the *search & replace* feature is the old chestnut: the differences between British and American spelling rules.

This could come up whenever you are working on both the `en-US` and `en-GB` locales, or if two translators, each on a different side of the pond, forgot to coordinate their spelling.

Let's say you have the following targets with German as a source language:

```
The world's No.1 donut
Vanilla donut
Chocolate-chip donut
Doughnut miss it!
```

and so on. Replace all instances of the word `donut` with the `doughnut` variant by following the steps below.

1. Click on the Search & Replace icon

![Search & Replace](/img/workbench/search_and_replace_icon.png)

2. Fill in the `Filter by source` field to work exclusively on those entries that contain the given string in the source language. This example is about the spelling of "donut", so you would enter the German original, `Krapfen`, to limit the search. Rest assured: source entries are **never** changed.

3. Enter the word that you'd like to replace in the `Search in target` field, in this case, `donut`.

4. Enter the replacement, `doughnut`, in the `Replace in target` field.

That's all there is to setting things up, the rest is about making sure your changes will not cause any problems.

![Settings Before Preview](/img/workbench/cookbook/search_and_replace_settings.png)

5. Click on **Preview!** to see your changes applied to a subset of segments.

6. If contents of the Preview area look good, uncheck the Preview checkbox. 

7. (_Optionally_)do a Test run by clicking on "Go!" 

8. Uncheck the `Test run` checkbox and click on "Go!" to really apply the replacement.


Depending on the number of segments, the process can take some time to finish. You will receive an e-mail for  both the Test and Live modes, containing a list of proposed (Test) or applied (Live) changes.

## Tutorial 2: to-do (Regex Replace)

