---
GENERATOR: 'Mozilla/4.79 \[en\] (X11; U; Linux 2.4.18-3 i686) \[Netscape\]'
Generator: Microsoft Word 98
description: 'FSET - define a face set'
title: FSET
---

  [[\
[FSET]{style="text-decoration: underline;"}\
]{style="font-weight: bold;"}]{style="text-decoration: underline;"}

> This command  is used to  define a  set  of element faces. Defining
> face sets can be useful for either defining boundary conditions,
> material interfaces, or surface subsets for further mesh processing.\

> FORMAT:
>
> > [[fset ]{style="font-weight: bold;"}/ name / pset, get, pointsetname
> > /\
> > [\
> > ]{style="font-weight: bold;"}The fset name must be an integer or
> > character string. Currently, only 32 named face sets may exist.
> > However, any number of integer-numbered face sets (up to the total
> > number of faces in the problem) may be defined. Face sets may be
> > used in all of the usual ways that eltsets and psets may be used,
> > e.g :\
> > \
> > ]{style="font-family: times new roman,times;"}**cmo/setatt**/
> > 3dmesh/fluid\_structure[]{style="font-weight: bold;"}/**fset**,**get**,blue/\
> > \
> > \
> > where fluid\_structure is the name of a face set attribute.[    \
> > ]{style="font-family: times new roman,times;"}**\
> > **NOTE: All modules do not support use of fset.**\
> > **
>
> EXAMPLE:
>
> >  fset / fname / pset, get psetname\
> >  \

\
