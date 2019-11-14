# Content-Type Mapping

## Overview

Override the Content-Type HTTP header for a given path or prefix. Frequently used with template URLs or JS resources with mischaracterized Content-Types, it is sometimes useful to avoid encoding or character escaping troubles.

**Multiple** `Content-Type` overrides can be added on each path or prefix, but no two such fields may match.

## Parameters

+ _From_ and _To_: the content types definind the mapping.
