---
Author: Jan Wills
GENERATOR: 'Mozilla/4.72 \[en\] (X11; U; Linux 2.2.14-5.0 i686) \[Netscape\]'
---

> **read/LaGriT**
>
> > read in a LaGriT restart file
>
> SHORT FORMAT:
>
> > **read**/filename.\[lglagritLaGriT\]/cmo\_name\
> > \
> > [Note that the filename is case-sensitive, though the extension
> > itself is not. When using the short format, the file will be read in
> > ascii mode.]{style="font-family: Times New Roman,Times;"}\
>
> LONG FORMAT:
>
> > **read**/**LaGriT**/file\_name/\[cmo-name\]/\[**ascii**
> > **binary**\]\
> >      cmo\_name    -    ignored all mesh objects are read from the
> > file\
> >     The default is **ascii**, but the code will determine file type
> > if nessary.
>
> EXAMPLES:
>
> > **read**[/]{style="font-family: monospace;"}**LaGriT**[/file1]{style="font-family: monospace;"}       
> > file1 will be read as ascii.  If the read fails to find the ascii
> > check string, the file will be closed and reopened for a binary
> > read.
> >
> > **read**/**LaGriT**/file2//**binary**
