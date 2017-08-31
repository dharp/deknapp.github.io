---
GENERATOR: 'Mozilla/4.79C-SGI \[en\] (X11; U; IRIX64 6.5 IP30) \[Netscape\]'
Generator: Microsoft Word 98
title: 'QUALITY - compute and report mesh quality measures'
---

### Using various quality measures to characterize tets as type: sliver, wedge, cap or needle elements.

\

+-----------+-----------+-----------+-----------+-----------+-----------+
 \          **Equilat  **Sliver*  **Cap** -  **Needle*  **Wedge** 
            eral**\    *          Character  *          -Characte 
                       -          ize        -          rize      
                       Character  by large   Character  by small  
                       ize        maximum    ize        minimum   
                       by small   solid      by small   dihedral  
                       minimum    angle.\    min/max    angle and 
                       dihedral              edge       small     
                       angle and             length     min/max   
                       large                 ratio but  edge      
                       maximum               not small  length    
                       dihedral              minimum    ratio\    
                       angle but             dihedral             
                       not a                 angle.\              
                       large                                      
                       solid                                      
                       angle.\                                    
+-----------+-----------+-----------+-----------+-----------+-----------+
 \          ![Equilat  ![Sliver   ![Cap      ![Needle   ![Wedge   
            eral       Tetrahedr  Tetrahedr  Tetrahedr  Tetrahedr 
            Tetrahedr  a](../ima  a](../ima  a](../ima  a](../ima 
            a](../ima  ges/quali  ges/quali  ges/quali  ges/quali 
            ges/quali  ty_tet_sl  ty_tet_ca  ty_tet_ne  ty_tet_we 
            ty_tet_eq  iver.png)  p.png){wi  edle.png)  dge.png){ 
            uilateral  "2  dth="200"  "2  width="20 
            .png){wid  00"        height="2  00"        0"        
            th="200"   height="2  00"\      height="2  height="2 
            height="2  00"\                 00"\      00"\     
            00"\                                                 
+-----------+-----------+-----------+-----------+-----------+-----------+
 `Coordina      0 0 0       1  0      1   0       .1 -       1    
 tes            0 1 1    0.1         0       .1  0      0    0    
   `            1 0 1      -1  0      1   1       .1        -1    
                1 1 0    0.1         0       .1  0      0    0    
                            0  1      0   0      -.1         0    
                        -0.1         0        0  0      1    0.1  
                            0 -1      0.75         0         0    
                        -0.1      0.25 0.1    0  1      1   -0.1  
+-----------+-----------+-----------+-----------+-----------+-----------+
 `Aspect R  `1.0       `0.2927E+  `0.7448E-  `0.3429E+  `0.2617E+ 
 atio          `       00         01         00         00        
    `                   `          `          `          `        
+-----------+-----------+-----------+-----------+-----------+-----------+
 `Min Dihe  `7.05288E  `1.59424E  `1.57932E  `5.33585E  `1.14212E 
 dral Angl  +01        +01        +01        +01        +01       
 e            `          `          `          `          `       
 `                                                                
+-----------+-----------+-----------+-----------+-----------+-----------+
 `Max Dihe  `7.05288E  `1.57380E  `1.49550E  `8.74394E  `90.0     
 dral Angl  +01        +02        +02        +01            `     
 e            `          `          `          `                  
 `                                                                
+-----------+-----------+-----------+-----------+-----------+-----------+
 `Min Soli  `3.15863E  `9.26487E  `2.87535E  `1.13741E  `3.35189E 
 d Angle    +01        +00        +00        +00        +00       
       `      `          `          `          `          `       
+-----------+-----------+-----------+-----------+-----------+-----------+
 `Max Soli  `3.15863E  `9.26487E  `2.60111E  `5.56182E  `8.19307E 
 d Angle    +01        +00        +02        +01        +01       
       `      `          `          `          `          `       
+-----------+-----------+-----------+-----------+-----------+-----------+
 `Min/Max   `1.0       `7.14143E  `2.59808E  `1.98030E  `0.1      
 Edge Leng     `       -01        -01        -01           `      
 th Ratio                `          `          `                  
        `                                                         
+-----------+-----------+-----------+-----------+-----------+-----------+

\

------------------------------------------------------------------------

\
Example: LaGriT input file to identify sliver, cap, needle and wedge
type elements.\
\

    *--* ex_id_tet_types
    *--* Header Begin
    *--* LAGriT Example Identify Sliver, Cap, Needle, Wedge
    * Carl Gable
    * gable -at- lanl -dot- gov
    *
    *
    *--* Create a random point distribution
    *--* Connect them into a tet mesh
    *--*
    *--*----------------------------------------------------
    *--* Header End
    *--* ex_id_tet_types
    *--*
    cmo / create / cmo1 / / / tet
    surface / outer / reflect / box / 0,0,0 / 1,1,1
    region / r1 /  le outer  /
    mregion / m1 /  le outer  /
    createpts / random / xyz / 0.1 / 0,0,0 / 1,1,1
    setpts
    connect
    dump / gmv / output_tets.gmv
    *
    * Compute the various tet quality measures
    *
    * Minimum Dihedral Angle, (degree)
    cmo / addatt / cmo1 / ang_mind / ang_mind
    * Minimum Dihedral Angle, (radian)
    cmo / addatt / cmo1 / ang_minr / ang_minr
    * Maximum Dihedral Angle, (degree)
    cmo / addatt / cmo1 / ang_maxd / ang_maxd
    * Maximum Dihedral Angle, (radian)
    cmo / addatt / cmo1 / ang_maxr / ang_maxr
    * Minimum Solid Angle, (degree)
    cmo / addatt / cmo1 / ang_mind_solid / s_mind
    * Minimum Solid Angle, (radian)
    cmo / addatt / cmo1 / ang_minr_solid / s_minr
    * Maximum Solid Angle, (degree)
    cmo / addatt / cmo1 / ang_maxd_solid / s_maxd
    * Maximum Solid Angle, (radian)
    cmo / addatt / cmo1 / ang_maxr_solid / s_maxr
    * Aspect Ratio
    quality / aspect / y
    * ( minimum edge lenght ) / ( maximum edge length )
    quality / edge_ratio / y
    * Edge lenght minimum
    quality / edge_min / y
    * Edge length maximum
    quality / edge_max / y
    *
    * Identify Slivers
    *
    * Define adjustable parameters to determine cut-off values.
    *
    define / MIN_DIHEDRAL  /  10.0
    define / MAX_DIHEDRAL  / 170.0
    define / MAX_SOLID_ANG_BIG / 170.0
    define / MAX_SOLID_ANG_SMALL / 10.0
    define / EDGE_RATIO    /   0.1
    *
    eltset / e_dih_small / ang_mind / le / MIN_DIHEDRAL
    eltset / e_dih_big   / ang_maxd / ge / MAX_DIHEDRAL
    eltset / e_solid_big / s_maxd   / le / MAX_SOLID_ANG_SMALL
    eltset / e_tmp       / inter / e_dih_small e_dih_big
    eltset / e_sliver    / inter / &
             e_tmp e_solid_big
    *
    * Identify Cap elements
    *
    eltset / e_cap / s_maxd / ge / MAX_SOLID_ANG_BIG
    *
    * Identify Needle elements
    *
    eltset / e_edge_ratio / eratio   / le / EDGE_RATIO
    eltset / e_dih_small  / ang_mind / le / MIN_DIHEDRAL
    eltset / e_needle / not / e_edge_ratio e_dih_small
    *
    * Identify Wedge elements
    *
    eltset / e_wedge / inter / e_edge_ratio e_dih_small
    *
    * Set up some attributes to tag the elements.
    *
    cmo/addatt/cmo1/if_sliv/vint/scalar/nelements/-def-/-def-/-def-/1
    cmo/addatt/cmo1/if_cap/vint/scalar/nelements/-def-/-def-/-def-/1
    cmo/addatt/cmo1/if_ned/vint/scalar/nelements/-def-/-def-/-def-/1
    cmo/addatt/cmo1/if_wed/vint/scalar/nelements/-def-/-def-/-def-/1
    cmo/setatt/cmo1/if_sliv/eltset get e_sliver/ 2
    cmo/setatt/cmo1/if_cap /eltset get e_cap   / 2
    cmo/setatt/cmo1/if_ned /eltset get e_needle/ 2
    cmo/setatt/cmo1/if_wed /eltset get e_wedge / 2


    dump / gmv / tet_types.gmv / cmo1

    * begin compare here
    cmo / status
    cmo / printatt /  / -all- / minmax
    quality
    finish

  ------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------
  Tetrahedral mesh\                                                                                 Tet Mesh, Sliver Elements\                                                                 Tet Mesh, Cap Elements\                                                              Tet Mesh, Needle Elements\                                                                 Tet Mesh, Wedge Elements\
  ![Tet Mesh, Random Point Distribution](/images/quality_tets_all.png)"200" height="200"\   ![Tet Mesh, Sliver Elements](/images/quality_tets_sliver.png)"200" height="200"\   ![Tet Mesh, Cap Elements](/images/quality_tets_cap.png)"200" height="200"\   ![Tet Mesh, Needle Elements](/images/quality_tets_needle.png)"200" height="200"\   ![Tet Mesh, Wedge Elements](/images/quality_tets_wedge.png)"200" height="200"\
  ------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------

\
\
