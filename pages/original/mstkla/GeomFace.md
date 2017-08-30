---
GENERATOR: 'Mozilla/4.05C-SGI \[en\] (X11; I; IRIX64 6.5 IP28) \[Netscape\]'
---

[![](../images/arrow2.gif){width="30"
height="30"}](mstkla.html#MODEL%20FACE:) [![](../images/arrow3.gif){width="30"
height="30"}](GeomRegion.html) [![](../images/arrow4.gif){width="30"
height="30"}](GeomEdge.html)

![](../images/construction14.gif){width="169" height="131"}

------------------------------------------------------------------------

------------------------------------------------------------------------

   **MODEL FACE OPERATORS:**

------------------------------------------------------------------------

 *void* **GF\_Regions**(*PGeomFace* gf, *PGeomRegn* gr\[2\]);

Get the regions on either side of the face. gr\[0\] is the region on
the\
opposite side of the normal while gr\[1\] is the region on the same
side\
of the normal.  In principle (not in LaGriT), both entries of gr may\
be filled \_AND\_ gr\[0\] may be equal to gr\[1\]. Also in principle,
both\
entries of gr may be NULL.\
 

 

[![](../images/arrow2.gif){width="30"
height="30"}](mstkla.html#MODEL%20REGION:) [![](../images/arrow3.gif){width="30"
height="30"}](GeomRegion.html) [![](../images/arrow4.gif){width="30"
height="30"}](GeomEdge.html)
