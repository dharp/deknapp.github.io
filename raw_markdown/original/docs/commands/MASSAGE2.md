---
GENERATOR: 'Mozilla/4.8 \[en\] (X11; U; SunOS 5.8 sun4u) \[Netscape\]'
Generator: Microsoft Word 98
Template: |
    Macintosh HD:Applications:Microsoft Office 98:Word Custom
    Install:Microsoft Office 98:Templates:Web Pages:Blank Web Page
title: MASSAGE2
---

 

> **MASSAGE2**
>
> **MASSAGE2** iteratively calls MASSAGE to refine adaptively according
> to a gradient field. Thus, the **bisection\_length** option must be a
> field.
>
> FORMAT:
>
> **massage2** / file\_name / min\_scale / bisection\_length /
> merge\_length / toldamage /
> \[[tolroughness]{style="font-family: monospace;"}\] /
> \[ifirst,ilast,istride\]/\
>    
> \[**nosmooth**\]/\[**norecon**\]\[**strictmergelength**\]/\[**ignoremats**\]/\[**lite\]**/\[**checkaxy**\]/\[**semiexclusive**\]/**\[exclusive**\]
>
> \
> \
> **file\_name** is a file which contains a set of LaGriT commands that
> calculates the gradient field based on the distance field. In other
> words, the gradient field is a function of the distance field. It is
> necessary to have this file when using this routine, as the field must
> be updated after each refinement iteration.\
> \
> **Creating user function file for MASSAGE2 routine**
>
> This file contains a set of LaGriT commands which calculate the
> gradient field for refinement based on the distance field.
>
> A file could be written like this:
>
> \#user\_function.mlgi\
> \#An example of calculating the gradient field **F** as a linear
> function of the distance field **D**\
> \#Define some coefficients for the function\
> define / COEF\_A /\
> define / COEF\_B /\
> \
> \#Formula **F** = COEF\_A \* **D** + COEF\_B\
> \#First remove any distance field that exists and recompute the
> distance field\
> cmo / DELATT / mo\_sink / dfield\
> compute / distance\_field / mo\_sink / mo\_src / dfield\
> \
> \#Calculate **F**\
> math / multiply / mo\_sink / ref\_field / 1,0,0 / mo\_sink / dfield /
> COEF\_A\
> math / add / mo\_sink / ref\_field / 1,0,0 / mo\_sink / ref\_field /
> COEF\_B\
> \
> finish
>
> The user does not have to put a floor value for the gradient field in
> this case (unlike in MASSAGE), as MASSAGE2 will calculate the floor
> value automatically. However, the minimum length scale 'min\_scale'
> must be specified.\
> \
> The user must also create a node-based attribute for the gradient
> field before calling MASSAGE2. In the example above, attribute
> 'ref\_field' must already exist in the mesh object. The name of the
> field must also match the 'field\_name' argument in the MASSAGE2
> command.\
> \
> **min\_scale** is the minimum length scale of the mesh (the minimum
> desired edge length).\
> \
> See [**MASSAGE**](MASSAGE.html "MASSAGE") for other arguments.\
>
> EXAMPLE:
>
> **massage2** / user\_function.mlgi / 0.1 / ref\_field / 1.e-5 / 1.e-5
> / strictmergelength

\
