---
Author: Jan Wills
GENERATOR: 'Mozilla/4.72 \[en\] (X11; U; Linux 2.2.14-5.0 i686) \[Netscape\]'
---

> **read/avs**

> > read in an AVS file.  This file format contains no geometry
> > information.  This command requires either cmo-name to be given in
> > the command or for a mesh object to have been created previously.
>
> SHORT FORMAT:
>
> > **read**/filename.\[inpavs\]/cmo\_name\
> > \
> > [Note that the filename is case-sensitive, though the extension
> > itself is not.]{style="font-family: Times New Roman,Times;"}\
>
> LONG FORMAT:
>
> > **read**/**avs**/filename/\[cmo-name\]/\[node\_flags/element\_flag/attribute\_flag\]\
> >  
> >   ----------------- ------------- -----------------------
> >   node\_flag        (default=1)   0 skip node data
> >   \                 \             1 read node data
> >   element\_flag     (default=1)   0 skip element data
> >   \                 \             1 read element data
> >   attribute\_flag   (default=1)   0 skip attribute data
> >   \                 \             1 read attribute data
> >   ----------------- ------------- -----------------------
> >
>  EXAMPLES:
>
> > **read**/**avs**/file1/cmo1\
> > **read/avs**[/file2//1/1/0]{style="font-family: monospace;"}   
> > (skip attribute data)\
> >                                       (mesh object must already
> > exist)

>
