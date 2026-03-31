---
date: 2024-01-13
tag: note, dataview
---
```dataview
TABLE date AS Date, tag as Tag
FROM "1.areas/Scuola"
WHERE date>date(2023-09-15)AND date<date(2024-06-06)
SORT date desc
```