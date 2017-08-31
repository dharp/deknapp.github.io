---
GENERATOR: 'Mozilla/4.05C-SGI \[en\] (X11; I; IRIX 6.5 IP32) \[Netscape\]'
Generator: Microsoft Word 98
---

 

> **5. Assign material types to the regions**

Assign materials to regions using
the[**mregion**](commands/MREGION.md) command. This command has
similar syntax to the **[region](commands/REGION.md)** command except
that the interface should not be assigned to any material region. To
assign two materials, *mattop* and *matbot,* to the regions *top* and
*bottom:*\
 

**mregion/**mattop**/ le** cube **and gt** cutplane **/**\
**mregion/**matbot/ **le** cube **and lt** cutplan**e /**

![](new_md/Image225.gif)"317" "239"
