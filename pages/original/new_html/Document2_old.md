---
GENERATOR: 'Mozilla/4.79C-SGI \[en\] (X11; U; IRIX64 6.5 IP30) \[Netscape\]'
Generator: Microsoft Word 97
title: 'Document2-1'
---

 

<div align="right">

**LA-UR-95-3608**

</div>

**I.  INTRODUCTION**

> A. [LaGriT](LaGriT.html)\
> B.  [Tutorial](Tutoria1.html)

### II.  LAGRIT COMMANDS

> A. [Conventions](conventions.html)\
> B.  Alphabetic listing of LaGriT commands

  ------------------------------------------------------------ ------------------------------------------------------------ -------------------------------------------------------------
  [ADDMESH](ADDMESH.html) (join meshes)                        [ASSIGN](ASSIGN.html) (set global variables)                 
  [BOUNDARY](BOUNDAR1.html) (set attributes on surfaces)       [BOUNDARY\_COMPONENTS](BOUNDARY_C.html) (count bc's)         [BUBBLE](bubble.html) (extrude to 3d and extract bndry)
  [CALC\_RDIST](calc_rdist.html) (calculate radial dist.)      [CMO](CMO2.html) (modify mesh object)                        [COLORMAP](COLORMAP.html) (build adjacency map)
  [CONNECT](CONNECT1.html) (make tetrahedral mesh)             [COPYPTS](COPYPTS.html) (copy points)                        [COORDSYS](COORDSY.HTML) (change coordinate system)
  [CREATEPTS](createpts.html) (create points)                  [CREATE\_GRAPH](create_graph.html)(create adjacency graph)   
  [DEFINE](DEFINE.html) (give a name to a number)              [DEREFINE](DEREFINE.html) (merge nodes away)                 [DOPING](DOPING1.html) (set an attribute)
  [DUMP](DUMP2.html) (write output files)                      [DUMP\_RECOLOR](DUMP_RECOLOR.html) (use adjacency map)       
  [EDIT](EDIT2.html) (prints some mesh info)                   [ELTSET](ELTSET2.html) (select, name a set of elements)      [EXTRACT](EXTRACT1.html) (extract a surface)
  [EXTRUDE](extrude.html) (extrude a surface)                                                                               
  [FIELD](FIELD.html) (manipulate a field attribute)           [FILTER](FILTER.html) (filter nodes)                         [FINISH](FINISH.html) (end processing)
  [GENIEE](GENIEE.html) (make element connectivity)            [GEOMETRY](geometry.html) (set the geometry name)            
  [HELP](HELP.html) (print global variable)                    [HEXTOTET](HEXTOTE.html) (convert element types)             
  [INFILE](INPUT.html) (read input from a file)                [INPUT](INPUT.html) (read input from a file)                 [INTERSECT\_ELEMENTS](intersectelements.html) ( ..2 meshes)
  [INTERSECT](INTERSECT.html) (..2 2d meshes to get line)      [INTERPOLATE](main_interpolate.html) (.. attribute values    
  [KDTREE](kdtree.html) (represent mesh as kd-tree)                                                                         
  [LOG](LOG.html) (turn log file off and on)                   [LOOP](loop.html) (execute command many times)               [LOWER\_D](lower_d.html) (create lower dimen. structs.)
  [MASSAGE](MASSAGE.html) (optimize the grid)                  [MATH](MATH.html) (do math on attributes)                    [MERGE](MERGE.html) (remove nodes)
  [METIS](metis.html) (create partition)                       [MODE](MODE.html) (set modes)                                [MREGION](MREGION.html) (define a material region)
  [NEGATIVE\_AIJ](NEGATIVE.html) (test bndry for neg. coef.)                                                                
  [OFFSETSURF](OFFSETSURF.html) (..triangulated surface)                                                                    
  [PSTATUS](PSTATUS.html) (operate on point set)               [PERTURB](PERTURB.html) (perturb node locations)             [PSET](PSET.html) (define, name sets of nodes)
  [QUADXY](QUADXY.html) (define a logical xy node set)         [QUADXYZ](QUADXYZ1.HTML) (define a logical xyz node set)     [QUALITY](QUALITY.html) (evaluate mesh quality)
  [RADAPT](RADAPT.html) (adaptive smoothing)                   [RANKVOLUME](rankvolume.html)(list small volume elements)    [READ](READ.html) (read data)
  [RECON](RECON.html) (swap edges/faces)                       [REFINE](REFINE.html) (refine elements, edges)               [REGION](REGION.html) (define a geometric region)
  [REGNPTS](REGNPTS.html) (distributes nodes in region)        [REORDER](REORDER.html) (reorder nodes in a mesh)            [RESETPTS](RESETPT.html) (reset node values)
  [RM](RM.html) (remove nodes in area)                         [RMMAT](RMMAT.html) (remove a material)                      [RMPOINT](RMPOINT.html) (remove nodes/elements)
  [RMREGION](RMREGION.html) (remove a geometric region)        [RMSPHERE](RMSPHERE.html) (remove nodes in a sphere)         [RMSURF](RMSURF.html) (remove nodes in /on a surface)
  [ROTATELN](ROTATELN.html) (rotate nodes about a line)        [ROTATEPT](ROTATEPT.html)  (rotate nodes about a point)      [RZ](RZ.html) (see createpts)
  [RZAMR](RZAMR.html) (see createpts)                          [RZBRICK](RZBRICK.html) (see createpts)                      [RZRAN](RZRAN.html) (see createpts)
  [RZS](RZS.html) (see createpts)                              [RZV](RZV_LG.html) (see createpts)                           
  [SCALE](SCALE.html) (scale node coordinates)                 [SETPTS](SETPTS.html) (set node type and material)           [SETSIZE](SETSIZE.html) (calc size of space)
  [SETTETS](SETTETS.html) (make child nodes, etc)              [SMOOTH](SMOOTH.html) (node smoothing)                       [SORT](SORT.html) (sort an attribute)
  [STACK](STACK.html) (read,merge surfaces)                    [SURFACE](SURFACE.html) (define a geometric surface)         [SURFPTS](SURFPTS.html) (make nodes on a surface)
  [TRANS](TRANS.html) (translate node coordinates)             [TRIANGULATE](TRIAGN.html) (make triangles)                  
  [UNG2AVS](UNG2AVS.html) (UNGenerate to AVS)                                                                               
  [ZQ](ZQ.html) (see [cmo/setatt](cmo_setatt.html))                                                                         
  ------------------------------------------------------------ ------------------------------------------------------------ -------------------------------------------------------------

> C.   LaGriT commands by category:
>
> > Geometry commands:\
> > [SURFACE](SURFACE.html) (define a geometric surface)\
> > [REGION](REGION.html) (define a geometric region)\
> > [MREGION](MREGION.html) (define a material region)\
> > [GEOMETRY](geometry.html) (set the geometry name)\
> > [OFFSETSURF](OFFSETSURF.html) (..triangulated surface)
> >
> > Point Placement:\
> > [CREATEPTS](createpts.html) (create points)\
> > [QUADXY](QUADXY.html) (define a logical xy node set)\
> > [QUADXYZ](QUADXYZ1.HTML) (define a logical xyz node set)\
> > [REGNPTS](REGNPTS.html) (distributes nodes in region)\
> > [SURFPTS](SURFPTS.html) (make nodes on a surface)\
> > [COPYPTS](COPYPTS.html) (copy existing points)
> >
> > Point Modification and Selection:\
> > [PSET](PSET.html) (define, name sets of nodes)\
> > [TRANS](TRANS.html) (translate node coordinates)\
> > [SCALE](SCALE.html) (scale node coordinates)\
> > [ROTATEPT](ROTATEPT.html)  (rotate nodes about a point)\
> > [ROTATELN](ROTATELN.html) (rotate nodes about a line)\
> > [RMPOINT](RMPOINT.html) (remove nodes/elements)\
> > [FILTER](FILTER.html) (filter nodes)\
> > [COORDSYS](COORDSY.HTML) (change coordinate system)\
> > [COPYPTS](COPYPTS.html) (copy existing points)\
> > [PERTURB](PERTURB.html) (perturb node locations)\
> > [RM](RM.html) (remove nodes in area)\
> > [RMMAT](RMMAT.html) (remove a material)\
> > [RMREGION](RMREGION.html) (remove a geometric region)\
> > [RMSPHERE](RMSPHERE.html) (remove nodes in a sphere)\
> > [RMSURF](RMSURF.html) (remove nodes in /on a surface
> >
> > Connecting the Mesh:\
> > [SETPTS](SETPTS.html) (set node type and material)\
> > [CONNECT](CONNECT1.html) (make tetrahedral mesh)\
> > [SETTETS](SETTETS.html) (make child nodes, set element material)\
> > [RZBRICK](RZBRICK.html) (create a brick, hex mesh)\
> > [TRIANGULATE](TRIAGN.html) (make triangles)\
> > [GENIEE](GENIEE.html) (make element connectivity)
> >
> > Element Modification and Selection:\
> > [ELTSET](ELTSET2.html) (select, name a set of elements)\
> > [RMPOINT](RMPOINT.html) (remove nodes/elements)
> >
> > Creating, modifying, assessing and deleting mesh objects and their
> > attributes:\
> > [CMO](CMO2.html) (modify mesh object)\
> > [COPYPTS](COPYPTS.html) (copy points)\
> > [EXTRUDE](extrude.html) (extrude a surface)\
> > [FIELD](FIELD.html) (manipulate a field attribute)\
> > [INTERPOLATE](main_interpolate.html) (interpolate attribute values
> > from nodes or elements )\
> > [INTERSECT](INTERSECT.html) (..2 2d meshes to get line)\
> > [INTERSECT\_ELEMENTS](intersectelements.html) ( ..2 meshes)\
> > [LOWER\_D](lower_d.html) (create lower dimen. structs.)\
> > [EXTRACT](EXTRACT1.html) (extract a surface)\
> > [MATH](MATH.html) (do math on attributes)\
> > [QUALITY](QUALITY.html) (evaluate mesh quality)\
> > [RANKVOLUME](rankvolume.html)(list small volume elements)\
> > [SORT](SORT.html) (sort an attribute)\
> > [KDTREE](kdtree.html) (represent mesh as kd-tree)\
> > [ADDMESH](ADDMESH.html) (join meshes)\
> > [BOUNDARY](BOUNDAR1.html) (set attributes on surfaces)
> >
> > Optimize or customize the mesh:\
> > [MASSAGE](MASSAGE.html)(optimize the grid)\
> > [REFINE](REFINE.html) (refine elements, edges)\
> > [DEREFINE](DEREFINE.html) (merge nodes away)\
> > [SMOOTH](SMOOTH.html) (node smoothing)\
> > [RADAPT](RADAPT.html) (adaptive smoothing)\
> > [MERGE](MERGE.html) (remove nodes)\
> > [HEXTOTET](HEXTOTE.html) (convert element types)\
> > [RECON](RECON.html) (swap edges/faces)\
> > [MODE](MODE.html) (set modes)
> >
> > Input/Output:\
> > [READ](READ.html) (read data)\
> > [DUMP](DUMP2.html) (write output files)\
> > [STACK](STACK.html) (read,merge surfaces)\
> > [UNG2AVS](UNG2AVS.html) (UNGenerate to AVS)\
> > [LOG](LOG.html) (turn log file off and on)\
> > [INPUT](INPUT.html) (read input from a file)\
> > [ASSIGN](ASSIGN.html) (set global variables)
> >
> > >  

### III. MESH OBJECTS

> A. [Mesh Object Definition](meshobject.html)\
> B.[Command Interface](commandi.html)\
> C. [Fortran Interface](fortran.html)\
> D. [Mesh Object Connectivity](meshobjcon.html)\
> E. [Geometries](geometries.html)

### IV.  INTERFACING USER ROUTINES TO LAGRIT

>  A. [Building an Executable and Running LaGriT](build.html)\
>  B. [Issuing Commands from a User Program](issuing.html)\
>  C. [Writing User Commands](writing.html)\
>  D. [Accessing the Mesh Object](accessing.html)\
>  E.  Utility Subroutines

> 1\. [Memory Manager](memmang.html)(mmgetblk,mmrelblk,mmrelprt,mmincblk,\
>      mmfindbk,mmgettyp,mmgetlen,mmgetnam,mmprint,mmverify,mmggetbk)\
> 2. [Mesh Objects](meshob.html) (cmo\_create, cmo\_get\_info,
> cmo\_set\_info, cmo\_get\_name,\
>       cmo\_set\_name, cmo\_get\_attribute\_name, cmo\_newlen,
> cmo\_get\_intinfo,\
>       cmo\_release, cmo\_get\_attinfo, cmo\_get\_length,
> cmo\_set\_attinfo,\
>       cmo\_get\_attparam)\
> 3. [Point Selection](pointsel.html) (getptyp, unpackpc, unpacktp)\
> 4. [Character Length](charlen.html)  (icharln, icharlnf, icharlnb,
> nulltoblank\_lg)\
> 5. [Retrieving Point Sets and Element Sets ](retpts.html) (eltlimc,
> pntlimc, pntlimn)\
> 6. [Array Compression](arrcomp.html) (kmprsm, kmprsn, kmprsnr,
> kmprsnrrr, kmprsp, kmprspr, kmprsz, kmprszr)\
> 7. [Array Sorting](arrsort.html) (hpsort, hpsort1, hpsorti, hpsortim,
> hpsortimp, hpsortip, hpsortrmp)\
> 8. [Miscellaneous](miscell.html)
> (setsize,set\_user\_bounds,inside,volume\_element, user\_interpolate)\
> 9.[Geometry Information](geom.html)(geom\_lg.h, get\_material\_number)

### V.  ERRORS

A. [Errors in parsing or executing commands](errors.html#parse).\
B.  [Out of memory errors.](errors.html#memory)\
C.  [Fatal memory management errors](errors.html#panic) (PANIC!)

>  

### [LAGRIT REFERENCES:](References.html)

> **LaGriT User's Manual**

**Text to Search For: **

**Boolean: **ANDOR

**Case **InsensitiveSensitive

------------------------------------------------------------------------

>  

> [Return to LaGriT Home Page](../index.html)

------------------------------------------------------------------------

> ***These pages are maintained by Denise George at
> <dgeorge@lanl.gov>***
