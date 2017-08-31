---
GENERATOR: 'Mozilla/4.79C-SGI \[en\] (X11; U; IRIX64 6.5 IP30) \[Netscape\]'
Generator: Microsoft Word 97
Keywords:  
LaGriT command DUMP output format: 
    Description metadata should be 25-30 words and written from the specific
    to the general. Put your top keywords first but don't repeat title
    information.
title: DUMP
---

\

> **DUMP**

This command produces an output file from a Mesh Object. Some of the
standard graphics packages are supported including AVS, GMV and TECPLOT.
See below for full list of file types that can be written. The list is
in alphabetic order and describes each valid file\_type with syntax and
usage.\
\

GENERAL SYNTAX:\

**dump**/file\_type/file\_name/\[cmo\_name\]/

The dump command is followed by a word indicating file type. Valid file
type kewords are: **gmv, avs, avs2, chad, coord, datex, elem\_adj\_node,
elem\_adj\_elem, fehm, geofest, geom, gmv, gocad, lagrit, recolor, stl,
stor, tecplot, zone, zone\_imt,** and **zone\_outside** .\
The file\_type is followed by a string to be used as whole or part of
file name as described below.

\
SHORT SYNTAX:\

**dump**/ file\_name.\[**inp  avs  gmv  lg  lagrit  ts  exo** \] /
\[cmo\_name\]\
\
For common file types, a short form syntax can be used which skips the
file type designation. The file\_type is asssumed from the file\_name
suffix. The following are recognized; AVS (.inp or .avs), Exodus (.exo),
GMV (.gmv), LaGriT (.lagrit or .lg), and .ts (gocad).\
\

\
\
FILE TYPES:\
\
**dump** / **avs** /file\_name/\[cmo\_name\]
/\[iopt\_points,iopt\_elements,iopt\_node\_attributes,iopt\_element\_attributes\]\
\

Output in AVS UCD (Unstructured Cell Data) format. One can turn on or
off the output of node coordinates (iopt\_points), element connectivity
(iopt\_elements), node attributes (iopt\_node\_attributes) and element
attributes (iopt\_element\_attributes). 1 (default) is on, 2 is on but
the first column will not include the node number or element number, 0
turns off output of that part of the file. For instance,
dump/avs/file.inp/cmo\_name/1,1,0,0 will write the node coordinates and
element connectivity, but will not write node attributes or element
attributes.\
**Use the =2 option with caution** since the output will really not be
AVS format files. This is fine as long as you do not expect read/avs or
the AVS graphics program to read the file.\
For file format specification see
<http://help.avs.com/Express/doc/help/reference/dvmac/UCD_Form.htm>\

\
**dump / avs2 /**
file\_name/\[cmo\_name\]/\[iopt\_points,iopt\_elements,iopt\_node\_attributes,iopt\_element\_attributes\]\
\

This option will output integers as integers instead of floating point.
The other avs option converts integers to reals on output. The /avs/
option above outputs all attributes as real numbers. This option is
slower but the files are smaller if there are integers in the node or
element attributes.\

\
**dump** **** / **chad** **** /file\_name/\[cmo\_name\]/\
\

Will output a file nodes, faces, and connectivity for tet, hex, pyr, or
pri in CHAD format. Writes attributes imt and itp.

\
**dump** **** / **coord** **** /file\_name/\[cmo\_name\]/ (See also
**dump/fehm** )\
\

Will output a single file with node list x,y,z values and element
connectivity list in FEHM format. Files are written in FEHM format and
are described [by clicking here for details.](dump/DUMP3.html)\
The **coord** file is one of a set of files written when the **fehm**
file type is called.\

\
**dump** **** / **datex  simul** **** /file\_name/\[cmo\_name\]/\
\

Will output a file with Geometry, Element, Region, Location, and Dataset
in DATEX format.

\
**dump / elem\_adj\_elem** / file\_name/mo\_name \[delatt  keepatt 
attonly\]\
\

Option: **delatt** - Write adjacency information to an ascii file. Write
list of all elements adjacent to each element.\
File format: elem\_number ean\_num e1 e2 ... en\
Option: **keepatt** - write file and add node attribute **ean\_num**
(number of elements adjacent to each node)\
Option: **attonly** - do not write file, add node attribute ean\_num, a
dummy argument is still required in the file\_name field\

\
**dump / elem\_adj\_node** /file\_name/mo\_name\
\

Write adjacency information to an ascii file. Write list of all elements
adjacent to each node.\
File format:\
node\_number number\_of\_adjacent\_elem e1 e2 ... en  \

\
\
**dump / exo  exodusii** / file\_name/ mo\_name \[ **psets** \] / \[
**eltsets**\] / \[ **facesets** file1 file2 ... filen \]\
\

Write a mesh object to a file in the Exodus II format. The keyword psets
as token 5 will cause all psets (lists of vertex numbers) associated
with the mesh object to be written to the ExodusII output file. The
keyword eltsets as token 6 will cause all eltsets (lists of cell
numbers) associated with the mesh object to be written to the ExodusII
output file. If face set information is being provided from files (file1
file2 ... filen) the format of the file is written in AVS UCD cell
attribute format. The first column is the global cell number, the second
column is the local face number.\
[Click here for more details on options and files that are
written.](EXODUS.html)\

\
\
**dump / fehm** / file\_name\_root / cmo\_name / [ \[**delatt 
keepatt**\]   \[**keepatt\_voronoi  keepatt\_median**\]   \
        / \[ **ascii  binary** \] / \[**scalar  vector  both 
area\_scalar  area\_vector  area\_both**\]\
        / \[**all  graph  coefs  none**\] / \[**hybrid  nohybrid**
\] ]{style="font-family: monospace;"}\
\

Write out a series of files for the FEHM flow and transport code. The
tokens after the cmo name are all optional. The default options will\
delete the outside node attributes and will not add attributes for the
outside voronoi or median areas.\
The stor file will be written in ASCII format with scalar coefficient
values with compression of area coefficient list and indices.\
[Click here for more details on the files and
options.](dump/DUMP3.html) \
\
The file\_name is used to form the names of the following 7 files:\

[file\_name]{style="font-style: italic;"}.fehm - coordinates and
geometry ( see dump/coord/... command)\
[file\_name]{style="font-style: italic;"}\_material.zone - node imt
(material) zone lists ( see dump/zone\_imt/... command)\
[file\_name]{style="font-style: italic;"}\_outside.zone - node external
boundary zone lists (see dump/zone\_outside/... command)\
[file\_name]{style="font-style: italic;"}\_outside\_vor.area - node
external boundary area lists (see dump/zone\_outside/... command)\
[file\_name]{style="font-style: italic;"}\_interface.zone - zone lists
for nodes along material interfaces\
[file\_name]{style="font-style: italic;"}\_multi\_mat.zone - lists of
node pairs connected across material interfaces\
[file\_name]{style="font-style: italic;"}.stor - FEHM format file giving
the voronoi (control volume) associated with each node and the sparce
matrix structure

\
**dump / geofest**/file\_name\
\

Write a file to be read by the [GeoFEST, Geophysical Finite Element
Simulation Tool](http://www.openchannelfoundation.org/projects/GeoFEST/)
.  The output file is ascii.\

\
**dump / geom**/file\_name\
\

will write an ascii file containing the geometry information for the
current run. This information includes the region and mregion
definitions and surface, names, types and definitions.\

\
**dump/gmv**/file-name/\[mesh-object\]/\[**ascii** 
**binary**[\]]{style="font-family: monospace;"}\
\

Write a file to be read by the graphics program
[GMV](http://laws.lanl.gov/XCM/gmv/GMVHome.html).  The defaults are
binary and current mesh object.  NOTE:  For LaGriT versions dated after
October 1999, use    **cmo**/**setatt**//**ipolydat**/**no**   to reduce
file size. This command will keep the polygon data from being written to
GMV files.\
\

**dump / gocad** /file\_name\
\

Write a gocad TSURF file. See [GOCAD
TSURF](http://www.connectflow.com/geovisage/User/Formats/GocadTsurf.html). \

**dump / lagrit** /file\_name/\[cmo\_name\]/ \[**ascii**  **binary**[\]
]{style="font-family: monospace;"}\
\

Write a LaGriT restart file that contains geometry and mesh object
information.  cmo\_name can be '**-all-**' in which case all mesh
objects are written to the file or it can specify a list of mesh objects
to be written. A subsequent **read/lagrit** command will restart the
code at the state at which the dump command was issued. The default file
type is binary.\
 

**dump / recolor**/file\_name\
\

This command writes the existing **colormap** to the specified file. 
(See **[colormap](COLORMAP.html)** command)\

\
**dump / stl** /file\_name\
\

Output in STL, stereo lithography format. This is only supported for
triangle mesh objects.\

\
**dump / stor** / file\_name\_root / cmo\_name / [ \[ **ascii  binary**
\] /\
        / \[**scalar  vector  both  area\_scalar  area\_vector 
area\_both**\]\
        / \[**all  graph  coefs  none**\] / \[**hybrid  nohybrid**
\] ]{style="font-family: monospace;"}\
\

Same syntax as **dump/fehm** except the only output is the FEHM sparse
matrix coefficient STOR file
[file\_name]{style="font-style: italic;"}.stor.\
File can be written in ascii or binary (fortran unformatted platform
dependent). The area coefficient values can be written as scalar or
vector.\
The compression default is [all]{style="font-weight: bold;"} which will
compress both the list of area coefficients and the indices. The
[coefs]{style="font-weight: bold;"} compression, or
[none]{style="font-weight: bold;"} compression both use and older
algorithm and will result in larger files and may take longer to run.\
The **stor** file is one of a set of files written when the **fehm**
file type is called.\
\
[Click here for further explanation of options.](dump/DUMP3.html)\
[Click here for the STOR file format.](../STOR_Form.html)\
\

\
**dump / tecplot** /file\_name\
\

Write a file to be read by the Tecplot graphics package.  The output
file is ascii. Only node attributes are output, element attributes are
ignored and not output. Tecplot does not support prism or pyramid
element types so they are written as eight node, degenerate hex
elements. The ioflag parameter is used to control if the node attributes
are output or not is the AVS ioflag. The expected suffix for the file
name is '.plt'. If a name is given without the .plt suffix, a suffix,
.plt is added. Output is ascii. This output format does not support
output of a mesh with nodes but zero elements. If there are zero
elements, a header is written but node coordinate information is not
output.

\
\
**dump**[ / ]{style="font-family: monospace;"}**zone**[
/file\_name/\[cmo\_name\] / ]{style="font-family: monospace;"}
\[**delatt  keepatt**\]   \[**keepatt\_voronoi  keepatt\_median**\]\
\

Write out a set of fehm format zone files for the mesh object nodes.
These include zones for mesh materials and the external faces of the
mesh as described below. The **keepatt** option will keep node
attributes that tag nodes on external mesh boundaries (see
zone\_outside). The **delatt** option will delete the outside attributes
if they exist (the are removed by default). The area attributes for
outside nodes can be created with the **keepatt\_voronoi** or
**keepatt\_median** options (see zone\_outside).\
\
Files are written in FEHM format and are described in the
[dump/fehm]{style="font-weight: bold;"} command [by clicking here for
details.](dump/DUMP3.html)\
\
The file\_name is used to create names for the following 5 files:\
[file\_name]{style="font-style: italic;"}\_material.zone - node imt
(material) zone lists ( see dump/zone\_imt/... command)\
[file\_name]{style="font-style: italic;"}\_outside.zone - node external
boundary zone lists (see dump/zone\_outside/... command)\
[file\_name]{style="font-style: italic; text-decoration: underline;"}[\_outside\_vor.area]{style="text-decoration: underline;"}
or [file\_name]{style="font-style: italic;"}\_outside\_med.area - node
external boundary area lists (see dump/zone\_outside/... command)\
[file\_name]{style="font-style: italic;"}\_interface.zone - zone lists
for nodes along material interfaces, 0 length file if mesh is single
material\
[file\_name]{style="font-style: italic;"}\_multi\_mat.zone - lists of
node pairs connected across material interfaces, 0 length file if mesh
is single material\

\
\
**dump**[ / ]{style="font-family: monospace;"}**zone\_imt**[
/file\_name/\[cmo\_name\] / ]{style="font-family: monospace;"} \[
imt\_value \]  \
\

Will output only one file with name
[file\_name]{style="font-style: italic;"}\_material.zone. It is written
in FEHM zone format and are described [by clicking here for
details.](dump/DUMP3.html)\
file\_name\_**material**.**zone** is node list for each integer material
(imt) value. If the optional fifth argument is specified as an integer,
then a node list file is written only listing the nodes with the value
specified by imt\_value.\
([For options to output PSET's as ZONE/ZONN files see:
pset/zone](PSET.html))\
The **zone\_imt** file is one of a set of files written when the
**fehm** file type is called.\

\
**dump**[ / ]{style="font-family: monospace;"}**zone\_outside** 
**zone\_outside\_minmax**[ /file\_name/\[cmo\_name\] /
]{style="font-family: monospace;"}\
     \[**delatt  keepatt**\]  \[**keepatt\_voronoi 
keepatt\_median**\]\
\

Write fehm zone format files that list the outside node list and the
associated outside area list.\
\
There are two files written:\
\
1. [file\_name]{style="font-style: italic;"}\_outside.zone is a node
list for each of 6 possible external boundaries.\
If [keepatt]{style="font-weight: bold;"} is specified, then 6 node based
attributes are added to the mesh object with the names top, bottom,
left\_w, right\_e, back\_n, and front\_s. A node can occur in multiple
zones. For instance, a node located on a top corner of the mesh can be
found in zones for top, front\_s, and left\_w.

<div style="margin-left: 40px;">

1 = top = top = positive z direction (0,0,1)\
2 = bottom = bottom = negative z direction (0,0,-1)\
3 = left\_w = left or west = negative x direction (-1,0,0)\
4 = front\_s = front or south = negative y direction (0,-1,0)\
5 = right\_e = right or east = positive x direction (1,0,0)\
6 = back\_n = back or north = positive y direction (0,1,0)\

</div>

\
2.
[file\_name]{style="font-style: italic; text-decoration: underline;"}[\_outside\_vor.area]{style="text-decoration: underline;"}
[]{style="font-style: italic;"} is a list of Voronoi area vectors
(Ax\_i,Ay\_i,Az\_i) associated with each external node. It is written to
match the node lists as written in the outside.zone file. Along with
each outside zone tag (such as top), there is a sum of each vector for
that zone. For applications such as infiltration, the z component (each
3rd value) would be used from the top zone list.\

    00001  top   Sum VORONOI vectors:  0.5000000E+00 0.5000000E+00 0.5000000E+00
    nnum
       3
      -2.500000000000E-01  -2.500000000000E-01   2.500000000000E-01   2.500000000000E-01   0.000000000000E+00   1.250000000000E-01
       0.000000000000E+00   2.500000000000E-01   1.250000000000E-01

\
If the keyword [keepatt\_voronoi]{style="font-weight: bold;"} is
specified, three node attributes (xn\_varea, yn\_varea, zn\_varea)
representing the voronoi area are added.\
If the keyword [keepatt\_median]{style="font-weight: bold;"} is
specified, three node attributes (xn\_marea, yn\_marea, zn\_marea)
representing the median area are added and the file name will be
[file\_name]{style="font-style: italic;"}\_outside\_med.area. Note that
the old version file name
[file\_name]{style="font-style: italic;"}\_outside.area has area vectors
computed with the median strategy.\
\
The option **zone\_outside\_minmax** is used to find the min and max
external node along each row and column of the regular grid. [Click here
for image](../../images/zone_outside.png) showing difference between the
default and the minmax options for outside nodes.\
\
These **zone\_outside** files are part of a set of files written when
the **zone** or **fehm** file type is called. The fehm zone format and
descriptions are  [in the **dump/fehm** command
details.](dump/DUMP3.html)\

\
\
EXAMPLES:\

**dump** / gmv /file\_name.gmv/cmo\_name/\
**dump** / gmv /file\_name.gmv/cmo\_name/ascii\
\
**dump** / file\_name.gmv / cmo\_name\
\
**dump** / tecplot /file\_name.plt/cmo\_name\
\
**dump** / lagrit /file\_name.lg/-all-/binary\
\
**dump**/file\_name.inp/cmo\_name\
**dump** / avs /file\_name.inp/cmo\_name\
**dump** / avs /file\_name.inp/cmo\_name/1 0 0 0 (output only node
coordinates)\
**dump** / avs /file\_name.inp/cmo\_name/1 1 0 0 (output node
coordinates and element connectivity)\
**dump** / avs /file\_name.inp/cmo\_name/0 0 0 1 (output element
attributes)\
**dump** / avs /file\_name.inp/cmo\_name/0 0 2 2 (output node and
element attributes without node numbers as first column of output)\
**dump** / avs2 /file\_name.inp/cmo\_name/1 1 1 0 (output node
coordinates, element connectivity and node attributes)\
\
**dump** / fehm /file\_root/cmo\_name/ (write ascii compressed STOR file
and full set of fehm input files)\
**dump** / stor /file\_root/cmo\_name/ (write ascii compressed STOR
file)\
**dump** / stor /file\_root/cmo\_name/ binary (write unformatted
compressed STOR file - platform dependent)\
**dump** / stor /file\_name/cmo\_name/ascii/area\_scalar\
\
**dump** / zone\_outside /file\_root/cmo\_name/keepatt (write outside
node zones and voronoi areas, keep outside attributes)\
**dump** / zone\_outside /file\_root/cmo\_name/keepatt\_voronoi (write
outside node zones and keep Voronoi area attributes)\
**dump** / zone\_outside\_minmax /file\_root/cmo\_name (write outside
nodes at minmax extent of each column)\
\
**dump** / zone /file\_root/cmo\_name/ delatt keepatt\_voronoi (write
all FEHM zone and area files, delete the outside attributes and keep the
voronoi area attributes)\
\
**dump**/ exo / file\_name / cmo\_name\
Write generic exodus output without any sets.\
**dump**/ exo / file\_name / cmo\_name / psets\
Write exodus output with point sets only.\
**dump**/ exo / file\_name / cmo\_name / / eltsets\
Write exodus output with element sets only.\
**dump**/ exo / file\_name / cmo\_name / / / facesets\
Write exodus output with face sets only. The facesets are internally
calculated and defined. Note that the algorithm is computationally
expensive and can take a long time to finish.\
**dump**/ exo / file\_name / cmo\_name / / / facesets
file1,file2,...,filen\
Write exodus output with face sets only. The face sets are imported from
file1, file2, ..., filen.\
**dump**/ exo / file\_name / cmo\_name / psets / eltsets / facesets
file1,file2,...,filen\
Write exodus output with all psets, element sets, and face sets. The
face sets are imported from file1, file2, ..., filen.\
\

\
[Click here for demos](../main_dump.html)

\

\
\

\
\
\
