---
GENERATOR: 'Mozilla/4.72 \[en\] (X11; U; Linux 2.2.14-5.0 i686) \[Netscape\]'
Generator: Microsoft Word 98
title: READ
---

 

> **READ**
>
> > This command reads in data into the active Mesh Object, replacing
> > whatever data might have been previously contained in the active
> > Mesh Object.

> FORMAT:
>
> > avs, LaGriT, and gmv formats are supported.  The other formats may
> > be used, but no guarantees are made about their capabilities. goCad
> > format is supported only for reading TSURF files.\
> >
> > **[read/avs](../read_avs.md)**\
> > **[read/LaGriT](../read_lagrit.md)**\
> > **[read/gmv](../read_gmv.md)**\
> > **[read/gocad](../read_gocad.md)**\
> > **[read/iges\_grid](../read_iges_grid.md)**\
> > **[read/ngp](../read_ngp.md)**\
> > **[read/vrml](../read_vrml.md)**\
> > **[read/datex](../read_datex.md)**\
> > **[read sheetij](../read_sheetij.md)**\
> > **[read/gmvfreeformat](../read_freeformat.md)**\
> > **[read/zonezonn\
> > ](../read_fehm_zone.md)**
> >
> > Note: To read tabular data (spreadsheet style x,y,z nodes or
> > attributes) see: [cmo/readatt/...](cmo/cmo_readatt.md)
>
> EXAMPLES:
>
> > **read** / gmv / myfile / mesh\_object\_name\
> > **read** / LaGriT / myfile\
> > \
> > Short form syntax does not require file type as the second token.
> > This is supported for the suffixes listed below. Suffix may be upper
> > or lower case.\
> > \
> > []{style="font-weight: bold;"**read** /
> > example.\[inpavsgmvtslglagrit\] / mesh\_object\_name\
> > \
> > See links to various formats for more detailed explanations and
> > examples.\

\
\
[\
](../read_fehm_zone.md)
