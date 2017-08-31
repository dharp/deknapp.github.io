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
LaGriT Commands by Category
===========================

#### Geometry Commands:

[GEOMETRY](docs/commands/geometry.html) (set the geometry name)\
[MREGION](docs/commands/MREGION.html) (define a material region)\
[OFFSETSURF](docs/commands/OFFSETSURF.html) (..triangulated surface)\
[REGION](docs/commands/REGION.html) (define a geometric region)\
[RZS](docs/commands/RZS.html) (depreciated, see createpts)\
[SURFACE](docs/commands/SURFACE.html) (define a geometric surface)\

#### Point Placement:

[COPYPTS](docs/commands/COPYPTS.html) (copy existing points)\
[CREATEPTS](docs/commands/createpts.html) (create points)\
[QUADXY](docs/commands/QUADXY.html) (define a logical xy node set)\
[QUADXYZ](docs/commands/QUADXYZ1.html) (define a logical xyz node set)\
[RZAMR](docs/commands/RZAMR.html) (depreciated, see createpts)\
[REGNPTS](docs/commands/REGNPTS.html) (distributes nodes in region)\
[REFINE2D](docs/commands/refine2d.html) (refine a triangle)\
[REORDER](docs/commands/REORDER.html) (reorder nodes in a mesh)\
[RZ](docs/commands/RZ.html) (depreciated, see createpts)\
[RZRAN](docs/commands/RZRAN.html) (depreciated, see createpts)\
[SURFPTS](docs/commands/SURFPTS.html) (make nodes on a surface)

#### Point Modification and Selection:

[COORDSYS](docs/commands/COORDSY.html) (change coordinate system)\
[COPYPTS](docs/commands/COPYPTS.html) (copy existing points)\
[FILTER](docs/commands/FILTER.html) (filter nodes)\
[PERTURB](docs/commands/PERTURB.html) (perturb node locations)\
[PSET](docs/commands/PSET.html) (define, name sets of nodes)\
[PSTATUS](docs/commands/PSTATUS.html) (operate on point set)\
[RESETPTS](docs/commands/RESETPT.html) (reset node values)\
[RM](docs/commands/RM.html) (remove nodes in area)\
[RMMAT](docs/commands/RMMAT.html) (remove a material)\
[RMPOINT](docs/commands/RMPOINT.html) (remove nodes/elements)\
[RMREGION](docs/commands/RMREGION.html) (remove a geometric region)\
[RMSPHERE](docs/commands/RMSPHERE.html) (remove nodes in a sphere)\
[RMSURF](docs/commands/RMSURF.html) (remove nodes in /on a surface\
[ROTATELN](docs/commands/ROTATELN.html) (rotate nodes about a line)\
[ROTATEPT](docs/commands/ROTATEPT.html)  (rotate nodes about a point)\
[SCALE](docs/commands/SCALE.html) (scale node coordinates)\
[TRANS](docs/commands/TRANS.html) (translate node coordinates)\
[ZQ](docs/commands/UNG2AVS.html) (depreciated, see cmo/setatt)

#### Connecting the Mesh:

[CONNECT](docs/commands/CONNECT1.html) (make tetrahedral mesh)\
[GENIEE](docs/commands/GENIEE.html) (make element connectivity)\
[RZBRICK](docs/commands/RZBRICK.html) (create a brick, hex mesh)\
[SETPTS](docs/commands/SETPTS.html) (set node type and material)\
[SETTETS](docs/commands/SETTETS.html) (make child nodes, set element
material)\
[TRIANGULATE](docs/commands/TRIAGN.html) (make triangles)\

#### Element Modification and Selection:

[ELTSET](docs/commands/ELTSET2.html) (select, name a set of elements)\
[FSET](docs/commands/FSET.html) (define a face set)\
[RMPOINT](docs/commands/RMPOINT.html) (remove nodes/elements)

#### Creating, modifying, assessing and deleting mesh objects and their attributes:

[ADDMESH](docs/commands/ADDMESH.html) (join meshes)\
[BOUNDARY](docs/commands/BOUNDAR1.html) (set attributes on surfaces)\
[BOUNDARY\_COMPONENTS](docs/commands/BOUNDARY_C.html) (count bc's)\
[CALC\_RDIST](docs/commands/calc_rdist.html) (calculate radial
distance)\
[CMO](docs/commands/CMO2.html) (modify mesh object)\
[COLORMAP](docs/commands/COLORMAP.html) (build adjacency map)\
[COMPUTE](docs/commands/COMPUTE.html) (compute a new mesh attribute)\
[COPYPTS](docs/commands/COPYPTS.html) (copy points)\
[CREATE\_GRAPH](docs/commands/create_graph.html) (create adjacency
graph)\
[DOPING](docs/commands/DOPING1.html) (set an attribute; depreciated, see
interpolate)\
[EXTRACT](docs/commands/EXTRACT1.html) (extract a surface)\
[EXTRUDE](docs/commands/extrude.html) (extrude a surface)\
[FIELD](docs/commands/FIELD.html) (manipulate a field attribute)\
[GRID2GRID](docs/commands/GRID2GRID.html) (element type conversion)\
[INTERPOLATE](docs/commands/main_interpolate.html) (interpolate
attribute values from nodes or elements )\
[INTERSECT](docs/commands/INTERSECT.html) (..2 2d meshes to get line)\
[INTERSECT\_ELEMENTS](docs/commands/intersectelements.html) ( ..2
meshes)\
[KDTREE](docs/commands/kdtree.html) (represent mesh as kd-tree)\
[LOWER\_D](docs/commands/lower_d.html) (create lower dimen. structs.)\
[MATH](docs/commands/MATH.html) (do math on attributes)\
[QUALITY](docs/commands/QUALITY.html) (evaluate mesh quality)\
[RANKVOLUME](docs/commands/rankvolume.html)(list small volume elements)\
[SORT](docs/commands/SORT.html) (sort an attribute)\
[UPSCALE](docs/commands/UPSCALE.html) (attribute from fine to coarse
grid)

#### Optimize or customize the mesh:

[BUBBLE](docs/commands/bubble.html) (extrude to 3d and extract bndry)\
[DEREFINE](docs/commands/DEREFINE.html) (merge nodes away)\
[HEXTOTET](docs/commands/HEXTOTE.html) (convert element types)\
[MASSAGE](docs/commands/MASSAGE.html)(optimize the grid)\
[MASSAGE2](docs/commands/MASSAGE.html)(optimize the grid)\
[MERGE](docs/commands/MERGE.html) (remove nodes)\
[METIS](docs/commands/MERGE.html) (graph partition algorithms)\
[MODE](docs/commands/MODE.html) (set modes)\
[RADAPT](docs/commands/RADAPT.html) (adaptive smoothing)\
[RECON](docs/commands/RECON.html) (swap edges/faces)\
[REFINE](docs/commands/REFINE.html) (refine elements, edges)\
[SETSIZE](docs/commands/SETSIZE.html) (calc size of space, set epsilon)\
[SMOOTH](docs/commands/SMOOTH.html) (node smoothing)

#### Input/Output:

[DEFINE](docs/commands/DEFINE.html) (give a name to a number)\
[DUMP](docs/commands/DUMP2.html) (write output files)\
[DUMP\_RECOLOR](docs/commands/DUMP_RECOLOR.html) (use adjacency map)\
[EDIT](docs/commands/EDIT2.html) (prints some mesh info)\
[HELP](docs/commands/HELP.html) (print global variable)\
[INFILE](docs/commands/INPUT.html) (read input from a file)\
[INPUT](docs/commands/INPUT.html) (read input from a file)\
[LOG](docs/commands/LOG.html) (turn log file off and on)\
[MEMORY](docs/commands/memory.html) (query state of memory)\
[READ](docs/commands/READ.html) (read data)\
[STACK](docs/commands/STACK.html) (read,merge surfaces)\
[UNG2AVS](docs/commands/UNG2AVS.html) (UNGenerate to AVS)\

#### Validation, Manipulation:

[ASSIGN](docs/commands/ASSIGN.html) (set global variables)\
[ELMTEST](docs/commands/elmtest.html) (validate connectivity)\
[FINISH](docs/commands/FINISH.html) (end processing, EXIT)\
[LOOP](docs/commands/loop.html) (execute command multiple times)\
[NEGATIVE\_AIJ](docs/commands/NEGATIVE.html) (test bndry for neg.
coef.)\
[RZV](docs/commands/RZV_LG.html) (depreciated, see createpts)\


