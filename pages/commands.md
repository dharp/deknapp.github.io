---
Keywords: 
    Mesh generation focused on Delaunay triangle and tetrahedral meshing.
    Mesh generation for geological applications. Mesh smoothing
    (optimization), reconnection, hybrid meshing (quadrilateral, prism,
    pyramid, line elements). Constructive solid geometry, Voronoi control
    volume area volume coefficient calculation.
description: 
    LaGriT is a library of user callable tools that provide mesh generation,
    mesh optimization and dynamic mesh maintenance in two and three
    dimensions for a variety of applications.
title: LANL  LaGriT 
---



![](images/lagrit2.jpg)"180" height="120"
#### Alphabetic Listing of LaGriT Commands

[A](#A)  [B](#B)  [C](#C)  [D](#D)  [E](#E)  [F](#F)  [G](#G) 
[H](#H)  [I](#I)  [K](#K)  [L](#L)  [M](#M)  [N](#N)  [O](#O) 
[P](#P)  [Q](#Q)  [R](#R)  [S](#S)  [T](#T)  [U](#U)  [Z](#Z)

[]{#A [ADDMESH](docs/commands/ADDMESH.html) (join meshes)\
[ASSIGN](docs/commands/ASSIGN.html) (set global variables)

[]{#B [BOUNDARY](docs/commands/BOUNDAR1.html) (set attributes on
surfaces)\
[BOUNDARY\_COMPONENTS](docs/commands/BOUNDARY_C.html) (count bc's)\
[BUBBLE](docs/commands/bubble.html) (extrude to 3d and extract bndry)\

[]{#C [CALC\_RDIST](docs/commands/calc_rdist.html) (calculate radial
distance)\
[CMO](docs/commands/CMO2.html) (modify mesh object)\
[COLORMAP](docs/commands/COLORMAP.html) (build adjacency map)\
[COMPUTE](docs/commands/COMPUTE.html) (compute a new mesh attribte
value)\
[CONNECT](docs/commands/CONNECT1.html) (make tetrahedral mesh)\
[COORDSYS](docs/commands/COORDSY.html) (change coordinate system)\
[COPYPTS](docs/commands/COPYPTS.html) (copy existing points)\
[CREATEPTS](docs/commands/createpts.html) (create points)\
[CREATE\_GRAPH](docs/commands/create_graph.html) (create adjacency
graph)\

[]{#D [DEFINE](docs/commands/DEFINE.html) (give a name to a number)\
[DEREFINE](docs/commands/DEREFINE.html) (merge nodes away)\
[DOPING](docs/commands/DOPING1.html) (set an attribute, depreciated, see
interpolate)\
[DUMP](docs/commands/DUMP2.html) (write output files)\
[DUMP\_RECOLOR](docs/commands/DUMP_RECOLOR.html) (use adjacency map)\

[]{#E [EDIT](docs/commands/EDIT2.html) (prints some mesh info)\
[ELMTEST](docs/commands/elmtest.html) (validate connectivity)\
[ELTSET](docs/commands/ELTSET2.html) (select, name a set of elements)\
[EXTRACT](docs/commands/EXTRACT1.html) (extract a surface)\
[EXTRUDE](docs/commands/extrude.html) (extrude a surface)\

[]{#F[FIELD](docs/commands/FIELD.html) (manipulate a field attribute)\
[FILTER](docs/commands/FILTER.html) (filter nodes)\
[FINISH](docs/commands/FINISH.html) (end processing, EXIT)\
[FSET](docs/commands/FSET.html) (define a face set)\

[]{#G[GENIEE](docs/commands/GENIEE.html) (make element connectivity)\
[GEOMETRY](docs/commands/geometry.html) (set the geometry name)\
[GRID2GRID](docs/commands/GRID2GRID.html) (element type conversion)\

[]{#H[HELP](docs/commands/HELP.html) (print global variable)\
[HEXTOTET](docs/commands/HEXTOTE.html) (convert element types)\

[]{#I[INFILE](docs/commands/INPUT.html) (read input from a file)\
[INPUT](docs/commands/INPUT.html) (read input from a file)\
[INTERSECT](docs/commands/INTERSECT.html) (..2 2d meshes to get line)\
[INTERSECT\_ELEMENTS](docs/commands/intersectelements.html) ( ..2
meshes)\
[INTERPOLATE](docs/commands/main_interpolate.html)(values from nodes or
elements)\

[]{#K[KDTREE](docs/commands/kdtree.html) (represent mesh as kd-tree)\

[]{#L[LOG](docs/commands/LOG.html) (turn log file off and on)\
[LOOP](docs/commands/loop.html) (execute command multiple times)\
[LOWER\_D](docs/commands/lower_d.html) (create lower dimen. structs.)\

[]{#M[MASSAGE](docs/commands/MASSAGE.html)(optimize the grid)\
[MASSAGE2](docs/commands/MASSAGE2.html) (optimize the grid)\
[MATH](docs/commands/MATH.html) (do math on attributes)\
[MEMORY](docs/commands/memory.html) (query state of memory)\
[MERGE](docs/commands/MERGE.html) (remove nodes)\
[METIS](docs/commands/MERGE.html) (graph partition algorithms)\
[MODE](docs/commands/MODE.html) (set modes)\
[MREGION](docs/commands/MREGION.html) (define a material region)\

[]{#N [NEGATIVE\_AIJ](docs/commands/NEGATIVE.html) (test bndry for neg.
coef.)\

[]{#O [OFFSETSURF](docs/commands/OFFSETSURF.html) (..triangulated
surface)\

[]{#P [PERTURB](docs/commands/PERTURB.html) (perturb node locations)\
[PSET](docs/commands/PSET.html) (define, name sets of nodes)\
[PSTATUS](docs/commands/PSTATUS.html) (operate on point set)\

[]{#Q[QUADXY](docs/commands/QUADXY.html) (define a logical xy node
set)\
[QUADXYZ](docs/commands/QUADXYZ1.html) (define a logical xyz node set)\
[QUALITY](docs/commands/QUALITY.html) (evaluate mesh quality)\

[]{#R [RADAPT](docs/commands/RADAPT.html) (adaptive smoothing)\
[RANKVOLUME](docs/commands/rankvolume.html)(list small volume elements)\
[READ](docs/commands/READ.html) (read data)\
[RECON](docs/commands/RECON.html) (swap edges/faces)\
[REFINE](docs/commands/REFINE.html) (refine elements, edges)\
[REFINE2D](docs/commands/refine2d.html) (refine a triangle)\
[REGION](docs/commands/REGION.html) (define a geometric region)\
[REGNPTS](docs/commands/REGNPTS.html) (distributes nodes in region)\
[REORDER](docs/commands/REORDER.html) (reorder nodes in a mesh)\
[RESETPTS](docs/commands/RESETPT.html) (reset node values)\
[RM](docs/commands/RM.html) (remove nodes in area)\
[RMMAT](docs/commands/RMMAT.html) (remove a material)\
[RMPOINT](docs/commands/RMPOINT.html) (remove nodes/elements)\
[RMREGION](docs/commands/RMREGION.html) (remove a geometric region)\
[RMSPHERE](docs/commands/RMSPHERE.html) (remove nodes in a sphere)\
[RMSURF](docs/commands/RMSURF.html) (remove nodes in /on a surface)\
[ROTATELN](docs/commands/ROTATELN.html) (rotate nodes about a line)\
[ROTATEPT](docs/commands/ROTATEPT.html)  (rotate nodes about a point)\
[RZ](docs/commands/RZ.html) (depreciated, see createpts)\
[RZAMR](docs/commands/RZAMR.html) (depreciated, see createpts)\
[RZBRICK](docs/commands/RZBRICK.html) (create a brick, hex mesh)\
[RZRAN](docs/commands/RZRAN.html) (depreciated, see createpts)\
[RZS](docs/commands/RZS.html) (depreciated, see createpts)\
[RZV](docs/commands/RZV_LG.html) (depreciated, see createpts)\

[]{#S [SCALE](docs/commands/SCALE.html) (scale node coordinates)\
[SETPTS](docs/commands/SETPTS.html) (set node type and material)\
[SETSIZE](docs/commands/SETSIZE.html) (calc size of space, set epsilon)\
[SETTETS](docs/commands/SETTETS.html) (make child nodes, set element
material)\
[SMOOTH](docs/commands/SMOOTH.html) (node smoothing)\
[SORT](docs/commands/SORT.html) (sort an attribute)\
[STACK](docs/commands/STACK.html) (read,merge surfaces)\
[SURFACE](docs/commands/SURFACE.html) (define a geometric surface)\
[SURFPTS](docs/commands/SURFPTS.html) (make nodes on a surface)\

[]{#T [TRANS](docs/commands/TRANS.html) (translate node coordinates)\
[TRIANGULATE](docs/commands/TRIAGN.html) (make triangles)\

[]{#U [UNG2AVS](docs/commands/UNG2AVS.html) (UNGenerate to AVS)\
[UPSCALE](docs/commands/UPSCALE.html) (attributes from a fine grid to a
coarse grid)\

[]{#Z [ZQ](docs/commands/UNG2AVS.html) (depreciated, see cmo/setatt)\


