---
GENERATOR: 'Mozilla/4.05C-SGI \[en\] (X11; I; IRIX64 6.5 IP28) \[Netscape\]'
title: MSTKLA Online Manual
---

![](../images/construction24.gif){width="249"
height="87"}![](../images/construc6.gif){width="248" height="166"}

------------------------------------------------------------------------

**MSTKLA - Mesh ToolKit interface to [LAgrit](http://lagrit.lanl.gov)**

(LA-UR-99-6711)

------------------------------------------------------------------------

**DIRECT LINKS**

[![](../images/model.gif){width="142"
height="24"}](Geom.html) [![](../images/mesh.gif){width="143"
height="26"}](Mesh.html) [![](../images/utilities.gif){width="143"
height="25"}](utilities.html) [![](../images/attributes.gif){width="145"
height="26"}](MeshAttributes.html)

[![](../images/modelenty.gif){width="144"
height="24"}](GeomEntity.html) [![](../images/modelregn.gif){width="141"
height="25"}](GeomRegion.html) [![](../images/modelface.gif){width="143"
height="26"}](GeomFace.html) [![](../images/modeledge.gif){width="143"
height="25"}](GeomEdge.html) [![](../images/modelvert.gif){width="142"
height="24"}](GeomVertex.html)

[![](../images/genregn.gif){width="145"
height="25"}](GenRegion.html) [![](../images/meshregn.gif){width="143"
height="25"}](MeshRegion.html) [![](../images/meshface.gif){width="143"
height="26"}](MeshFace.html) [![](../images/meshedge.gif){width="143"
height="25"}](MeshEdge.html) [![](../images/meshvert.gif){width="143"
height="25"}](MeshVertex.html)

[![](../images/trivia.gif){width="144" height="25"}](trivia.html)

------------------------------------------------------------------------

------------------------------------------------------------------------

Questions, Comments, Suggestions? Contact:

                Rao V Garimella,
PostDoc                                                                      
Tel: (505) 665-4636\
                EES-5, MS D450                                       
'\\      '\\                                   FAX: (505) 665-6459\
                Los Alamos National Lab                              ( 
)-(  )                                Email: <rao@lanl.gov>\
                Los Alamos, NM 87545\

------------------------------------------------------------------------

\
 

**MSTKLA** is a C interface to the **LaGriT** code which is designed to
make it easier to use the LaGriT functionality. It tries to hide some of
the internals of LaGriT and provides an API that works in a somewhat
object oriented way. It does not attempt to provide or enhance
interactive commands that exist in LaGriT. Rather, it is designed more
with writing automated mesh generation procedures and complex meshing
algorithms within LaGriT in mind.

MSTKLA has one or more *mesh objects*, which have mesh ***regions***,
mesh ***faces,*** mesh ***edges*** and mesh ***vertices*** (nodes).
*Mesh faces and mesh edges are objects defined on the fly in terms of
their vertices.* One can ask these objects various questions or modify
their info through operators. In addition there is a ***geometric
model*** and ***geometric model objects*** (In the spirit of consistent
naming, I am labeling this set of functions **GMTKLA**). Since LaGriT
does not really store curves or points in the database, these are also
faked on the fly.

The mesh and model entities are related through the concept of
***CLASSIFICATION***.

***"A mesh entity is classified on a model entity if it forms all or
part of that model entity's discretization (grid) but not its
boundary's".***

So mesh regions can be classified only on a model region.  Mesh faces
can be classified on a model face or a model region. Mesh vertices can
be classified on a model vertex, model edge, model face or model region.

Classification information can be queried from MSTKLA if it is
available. In particular, in LaGriT, only ***external faces*** (what
LaGriT calls ***"reflective" boundaries***) and ***internal faces or
interfaces*** created with the option ***"intrcons"*** in the
***[surface](http://www.t12.lanl.gov/~lagrit/new_html/SURFACE.html)***
command have the information required to retrieve full classification
information. Full classification information includes the ***type*** of
geometric model entity the mesh entity is classified on, the ***ID of
that geometric model entity*** and ***a pointer to the geometric model
object*** (which can be further queried). Interface surfaces created
with the surface command option "***intrface***" **do not** have the
necessary information to relate the mesh and the model fully. (In the
future, I may put in code to take the "intrface" type surfaces and add
the info needed to find out the classification information).

Note that the current interface works for querying an existing mesh but
not **yet** for modifying it. The operators for this are on the way.
Operators for calling the actual meshing operators (connect, refine,
smooth, etc) will also be added in the near future.

Finally, the basic interface (low level query and modification
operators) are expected to retain the same format regardless of what the
underlying database is (LaGriT or something else). So, for example, I am
hoping that an operator to retrieve the nodes of an element will retain
the same form shown below regardless of how it functions internally:

*void* **MR\_Vertices**(*PMeshObj* mesh, *PMeshRegn* reg, *int \**nv,
*PMeshVert \**rverts);

I will try hard to maintain this API constant but cannot absolutely
guarantee it.\
 

[]{#parent-child}Also see **[Parent-Child Node (Vertex)
Issues](http://www.ees.lanl.gov/staff/rao/mstkla/parent-child.html)**\

------------------------------------------------------------------------

------------------------------------------------------------------------

\
[]{#typedefs}[TYPEDEFS](http://www.ees.lanl.gov/staff/rao/mstkla/prelim.html) 

------------------------------------------------------------------------

------------------------------------------------------------------------

[]{#MSTKLA_Init}**MSTKLA Interface Operators**\

------------------------------------------------------------------------

\

------------------------------------------------------------------------

\
**MESH INITIALIZATION:**\
 \
*void* **MSTKLA\_Init**(*void*);

Initialize the mesh toolkit.

------------------------------------------------------------------------

\
**MESH OPERATORS:**\
 \
 []{#MESH OBJECT:}[MESH
OBJECT:](http://www.ees.lanl.gov/staff/rao/mstkla/Mesh.html)

 []{#MESH REGION:}[MESH
REGION:](http://www.ees.lanl.gov/staff/rao/mstkla/MeshRegion.html)

 []{#MESH FACE:}[MESH
FACE:](http://www.ees.lanl.gov/staff/rao/mstkla/MeshFace.html)

 []{#MESH EDGE:}[MESH
EDGE:](http://www.ees.lanl.gov/staff/rao/mstkla/MeshEdge.html)

 []{#MESH VERTEX:}[MESH
VERTEX:](http://www.ees.lanl.gov/staff/rao/mstkla/MeshVertex.html)\
 \
 []{#GENERIC MESH REGION QUERIES:}[GENERIC MESH REGION
QUERIES:](http://www.ees.lanl.gov/staff/rao/mstkla/GenRegion.html)\

------------------------------------------------------------------------

\

------------------------------------------------------------------------

\
[]{#GMTKLA_Init}**GEOMETRIC MODEL INITIALIZATION:**

*void* **GMTKLA\_Init**(*void*);

Initialize the geometric model interface.

------------------------------------------------------------------------

\
**MODEL OPERATORS:**

 []{#GEOMETRIC MODEL:}[GEOMETRIC
MODEL:](http://www.ees.lanl.gov/staff/rao/mstkla/Geom.html)

 []{#MODEL ENTITY:}[MODEL
ENTITY:](http://www.ees.lanl.gov/staff/rao/mstkla/GeomEntity.html)

 []{#MODEL REGION:}[MODEL
REGION:](http://www.ees.lanl.gov/staff/rao/mstkla/GeomRegion.html)

 []{#MODEL FACE:}[MODEL
FACE:](http://www.ees.lanl.gov/staff/rao/mstkla/GeomFace.html)

 []{#MODEL EDGE:}[MODEL
EDGE:](http://www.ees.lanl.gov/staff/rao/mstkla/GeomEdge.html)

 []{#MODEL VERTEX}[MODEL
VERTEX](http://www.ees.lanl.gov/staff/rao/mstkla/GeomVertex.html)
---&gt; Not implemented fully\
 

------------------------------------------------------------------------

\

------------------------------------------------------------------------

\
[]{#UTILITIES:}**[UTILITIES:](http://www.ees.lanl.gov/staff/rao/mstkla/utilities.html)**

------------------------------------------------------------------------

------------------------------------------------------------------------

[]{#EXAMPLE}**[EXAMPLE OF PROGRAMMING WITH
MSTKLA](http://www.ees.lanl.gov/staff/rao/mstkla/example.html)**\
 

------------------------------------------------------------------------

------------------------------------------------------------------------

[]{#EXECUTABLE}**[LIBRARIES, INCLUDE FILES AND CREATING AN
EXECUTABLE](http://www.ees.lanl.gov/staff/rao/mstkla/linking.html)**
