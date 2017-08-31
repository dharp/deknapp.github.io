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


 ![](http://www.lanl.gov/images/tr  <div class="wide_tbl">            
 ansparent.gif){.strut                                                
 width="160" height="1"}            ### Table of LaGriT Commands      

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     A                [ADDMESH](doc 
                                    s/  [ASSIGN](docs/c             

                                                      commands/ADDM 
                                    ES  ommands/ASSIGN.             

                                                      H.html)       
                                        html)                       

                                                      (add one mesh 
                                        (set global                 

                                                      to another)   
                                        variables)                  

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     B                [BOUNDARY](do 
                                    cs  [BOUNDARY\_COMP  [BUBBLE](d 
                                    ocs/c                            
                                                      /commands/BOU 
                                    ND  ONENTS](docs/co  ommands/bu 
                                    bble.                            
                                                      AR1.html)     
                                        mmands/BOUNDARY  html)      

                                                      (set attribut 
                                    es  _C.html)         (extrude t 
                                    o 3d                             
                                                      on surfaces)  
                                        (count bc's)     and extrac 
                                    t                                

                                                         bndry)     

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     C                [CALC\_RDIST] 
                                    (d  [CMO](docs/comm  [COLORMAP] 
                                    (docs                            
                                                      ocs/commands/ 
                                    ca  ands/CMO2.html)  /commands/ 
                                    COLOR                            
                                                      lc_rdist.html 
                                    )   (modify mesh     MAP.html)  

                                                      (calculate    
                                        object)          (build     

                                                      radial        
                                                         adjacency  
                                    map)                             
                                                      distance)     


                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [COMPUTE](doc 
                                    s/  [CONNECT](docs/  [COORDSYS] 
                                    (docs                            
                                                      commands/COMP 
                                    UT  commands/CONNEC  /commands/ 
                                    COORD                            
                                                      E.html)       
                                        T1.html)         SY.html)   

                                                      (compute a ne 
                                    w   (2D and 3D       (change    

                                                      mesh attribut 
                                    e)  Delaunay         coordinate 


                                        algorithm)       system)    

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [COPYPTS](doc 
                                    s/  [CREATEPTS](doc  [CREATE\_G 
                                    RAPH]                            
                                                      commands/COPY 
                                    PT  s/commands/crea  (docs/comm 
                                    ands/                            
                                                      S.html)(copy  
                                        tepts.html)      create_gra 
                                    ph.ht                            
                                                      points)       
                                        (create points)  ml)(create 


                                                         adjacency  


                                                         graph)     

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     D                [DEFINE](docs 
                                    /c  [DEREFINE](docs  [DOPING](d 
                                    ocs/c                            
                                                      ommands/DEFIN 
                                    E.  /commands/DEREF  ommands/DO 
                                    PING1                            
                                                      html)         
                                        INE.html)        .html)     

                                                      (give a name  
                                    to  (merge nodes     (depreciat 
                                    ed,                              
                                                      a number)     
                                        away)            see        


                                                         interpolat 
                                    e)                               
                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [DUMP](docs/c 
                                    om  [DUMP\_RECOLOR]             

                                                      mands/DUMP2.h 
                                    tm  (docs/commands/             

                                                      l)            
                                        DUMP_RECOLOR.ht             

                                                      (write output 
                                        ml)                         

                                                      files)        
                                        (use adjacency              


                                        map)                        

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     E                [EDIT](docs/c 
                                    om  [ELMTEST](docs/  [ELTSET](d 
                                    ocs/c                            
                                                      mands/EDIT2.h 
                                    tm  commands/elmtes  ommands/EL 
                                    TSET2                            
                                                      l)            
                                        t.html)          .html)     

                                                      (prints some  
                                        (validate        (select, n 
                                    ame a                            
                                                      mesh info)    
                                        connectivity)    set of     


                                                         elements)  

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [EXTRACT](doc 
                                    s/  [EXTRUDE](docs/             

                                                      commands/EXTR 
                                    AC  commands/extrud             

                                                      T1.html)      
                                        e.html)                     

                                                      (extract a    
                                        (extrude a                  

                                                      surface)      
                                        surface)                    

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     F                [FIELD](docs/ 
                                    co  [FILTER](docs/c  [FINISH](d 
                                    ocs/c                            
                                                      mmands/FIELD. 
                                    ht  ommands/FILTER.  ommands/FI 
                                    NISH.                            
                                                      ml)           
                                        html)            html)      

                                                      (manipulate a 
                                        (detect and      (end       

                                                      field         
                                        remove           processing 
                                    ,                                
                                                      attribute)    
                                        duplicate        EXIT)      


                                        nodes)                      

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [FSET](docs/c 
                                    om                              

                                                      mands/FSET.ht 
                                    ml                              

                                                      )             


                                                      (define a fac 
                                    e                               

                                                      set)          


                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     G                [GENIEE](docs 
                                    /c  [GEOMETRY](docs  [GRID2GRID 
                                    ](doc                            
                                                      ommands/GENIE 
                                    E.  /commands/geome  s/commands 
                                    /GRID                            
                                                      html)         
                                        try.html)        2GRID.html 
                                    )                                
                                                      (make/update  
                                        (set the         (element t 
                                    ype                              
                                                      element       
                                        geometry name)   covnversio 
                                    n)                               
                                                      connectivity) 


                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     H                [HELP](docs/c 
                                    om  [HEXTOTET](docs             

                                                      mands/HELP.ht 
                                    ml  /commands/HEXTO             

                                                      )             
                                        TE.html)                    

                                                      (print global 
                                        (convert                    

                                                      variable)     
                                        element types)              

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     I                [INFILE](docs 
                                    /c  [INPUT](docs/co  [INTERSECT 
                                    ](doc                            
                                                      ommands/INPUT 
                                    .h  mmands/INPUT.ht  s/commands 
                                    /INTE                            
                                                      tml)          
                                        ml)              RSECT.html 
                                    )                                
                                                      (read input   
                                        (read input      (..2 2d me 
                                    shes                             
                                                      from a file)  
                                        from a file)     to get lin 
                                    e)                               
                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [INTERSECT\_E 
                                    LE  [INTERPOLATE](d             

                                                      MENTS](docs/c 
                                    om  ocs/commands/ma             

                                                      mands/interse 
                                    ct  in_interpolate.             

                                                      elements.html 
                                    )   html)                       

                                                      ( .. of 2     
                                        (.. attribute               

                                                      meshes)       
                                        values)                     

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     K                [KDTREE](docs 
                                    /c                              

                                                      ommands/kdtre 
                                    e.                              

                                                      html)         


                                                      (represent me 
                                    sh                              

                                                      as kd-tree)   


                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     L                [LOG](docs/co 
                                    mm  [LOOP](docs/com  [LOWER\_D] 
                                    (docs                            
                                                      ands/LOG.html 
                                    )   mands/loop.html  /commands/ 
                                    lower                            
                                                      (turn log fil 
                                    e   )                _d.html)   

                                                      off and on)   
                                        (execute         (create lo 
                                    wer                              

                                        command          dimen.     


                                        multiple times)  structs.)  

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     M                [MASSAGE](doc 
                                    s/  [MASSAGE2](docs  [MATH](doc 
                                    s/com                            
                                                      commands/MASS 
                                    AG  /commands/MASSA  mands/MATH 
                                    .html                            
                                                      E.html)       
                                        GE2.html)        )          

                                                      (optimize the 
                                        (optimize the    (do math o 
                                    n                                
                                                      grid)         
                                        grid)            attributes 
                                    )                                
                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [MEMORY](docs 
                                    /c  [MERGE](docs/co  [METIS](do 
                                    cs/co                            
                                                      ommands/memor 
                                    y.  mmands/MERGE.ht  mmands/met 
                                    is.ht                            
                                                      html)         
                                        ml)              ml)        

                                                      (query state  
                                    of  (remove nodes)   (graph     

                                                      memory )      
                                                         partition  


                                                         algorithms 
                                    )                                
                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [MODE](docs/c 
                                    om  [MREGION](docs/             

                                                      mands/MODE.ht 
                                    ml  commands/MREGIO             

                                                      )             
                                        N.html)                     

                                                      (set modes)   
                                        (define a                   


                                        material                    


                                        region)                     

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     N                [NEGATIVE\_AI 
                                    J]                              

                                                      (docs/command 
                                    s/                              

                                                      NEGATIVE.html 
                                    )                               

                                                      (test bndry f 
                                    or                              

                                                      neg. coef.)   


                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     O                [OFFSETSURF]( 
                                    do                              

                                                      cs/commands/O 
                                    FF                              

                                                      SETSURF.html) 


                                                      (..triangulat 
                                    ed                              

                                                      surface)      


                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     P                [PERTURB](doc 
                                    s/  [PSET](docs/com  [PSTATUS]( 
                                    docs/                            
                                                      commands/PERT 
                                    UR  mands/PSET.html  commands/P 
                                    STATU                            
                                                      B.html)       
                                        )                S.html)    

                                                      (perturb node 
                                        (define, name    (operate o 
                                    n                                
                                                      locations)    
                                        sets of nodes)   point set) 

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     Q                [QUADXY](docs 
                                    /c  [QUADXYZ](docs/  [QUALITY]( 
                                    docs/                            
                                                      ommands/QUADX 
                                    Y.  commands/QUADXY  commands/Q 
                                    UALIT                            
                                                      html)         
                                        Z1.html)         Y.html)    

                                                      (define a     
                                        (define a        (evaluate  
                                    mesh                             
                                                      logical xy no 
                                    de  logical xyz      quality)   

                                                      set)          
                                        node set)                   

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     R                [RADAPT](docs 
                                    /c  [RANKVOLUME](do  [READ](doc 
                                    s/com                            
                                                      ommands/RADAP 
                                    T.  cs/commands/ran  mands/READ 
                                    .html                            
                                                      html)         
                                        kvolume.html)    )          

                                                      (adaptive     
                                        (list small      (read data 
                                    )                                
                                                      smoothing)    
                                        volume                      


                                        elements)                   

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [RECON](docs/ 
                                    co  [REFINE](docs/c  [REFINE2D] 
                                    (docs                            
                                                      mmands/RECON. 
                                    ht  ommands/REFINE.  /commands/ 
                                    refin                            
                                                      ml)           
                                        html)            e2d.html)  

                                                      (swap         
                                        (refine          (refine a  

                                                      edges/faces)  
                                        elements,        triangle)  


                                        edges)                      

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [REGION](docs 
                                    /c  [REGNPTS](docs/  [REORDER]( 
                                    docs/                            
                                                      ommands/REGIO 
                                    N.  commands/REGNPT  commands/R 
                                    EORDE                            
                                                      html)         
                                        S.html)          R.html)    

                                                      (define a     
                                        (distributes     (reorder n 
                                    odes                             
                                                      geometric     
                                        nodes in         in a mesh) 

                                                      region)       
                                        region)                     

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [RESETPTS](do 
                                    cs  [RM](docs/comma  [RMMAT](do 
                                    cs/co                            
                                                      /commands/RES 
                                    ET  nds/RM.html)     mmands/RMM 
                                    AT.ht                            
                                                      PT.html)      
                                        (remove nodes    ml)        

                                                      (reset node   
                                        in area)         (remove a  

                                                      values)       
                                                         material)  

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [RMPOINT](doc 
                                    s/  [RMREGION](docs  [RMSPHERE] 
                                    (docs                            
                                                      commands/RMPO 
                                    IN  /commands/RMREG  /commands/ 
                                    RMSPH                            
                                                      T.html)       
                                        ION.html)        ERE.html)  

                                                      (remove       
                                        (remove a        (remove no 
                                    des                              
                                                      nodes/element 
                                    s)  geometric        in a spher 
                                    e)                               

                                        region)                     

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [RMSURF](docs 
                                    /c  [ROTATELN](docs  [ROTATEPT] 
                                    (docs                            
                                                      ommands/RMSUR 
                                    F.  /commands/ROTAT  /commands/ 
                                    ROTAT                            
                                                      html)         
                                        ELN.html)        EPT.html)( 
                                    rotat                            
                                                      (remove nodes 
                                        (rotate nodes    e          

                                                      in /on a      
                                        about a line)    nodes abou 
                                    t a                              
                                                      surface)      
                                                         point)     

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [RZ](docs/com 
                                    ma  [RZAMR](docs/co  [RZBRICK]( 
                                    docs/                            
                                                      nds/RZ.html)  
                                        mmands/RZAMR.ht  commands/R 
                                    ZBRIC                            
                                                      (depreciated, 
                                        ml)              K.html)    

                                                      see createpts 
                                    )   (depreciated,    (depreciat 
                                    ed,                              

                                        see createpts)   see create 
                                    pts)                             
                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [RZRAN](docs/ 
                                    co  [RZS](docs/comm  [RZV](docs 
                                    /comm                            
                                                      mmands/RZRAN. 
                                    ht  ands/RZS.html)   ands/RZV_L 
                                    G.htm                            
                                                      ml)           
                                        (depreciated,    l)         

                                                      (depreciated, 
                                        see createpts)   (depreciat 
                                    ed,                              
                                                      see createpts 
                                    )                    see create 
                                    pts)                             
                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     S                [SCALE](docs/ 
                                    co  [SETPTS](docs/c  [SETSIZE]( 
                                    docs/                            
                                                      mmands/SCALE. 
                                    ht  ommands/SETPTS.  commands/S 
                                    ETSIZ                            
                                                      ml)           
                                        html)            E.html)    

                                                      (scale node   
                                        (set node type,  (calc size 
                                     of                              
                                                      coordinates)  
                                        itp, and         space, set 


                                        material, imt)   epsilon)   

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [SETTETS](doc 
                                    s/  [SMOOTH](docs/c  [SORT](doc 
                                    s/com                            
                                                      commands/SETT 
                                    ET  ommands/SMOOTH.  mands/SORT 
                                    .html                            
                                                      S.html)       
                                        html)            )          

                                                      (make child   
                                        (node            (sort an   

                                                      nodes, etc)   
                                        smoothing)       attribute) 

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                                      [STACK](docs/ 
                                    co  [SURFACE](docs/  [SURFPTS]( 
                                    docs/                            
                                                      mmands/STACK. 
                                    ht  commands/SURFAC  commands/S 
                                    URFPT                            
                                                      ml)           
                                        E.html)          S.html)    

                                                      (read,merge,s 
                                    ta  (define a        (make node 
                                    s on                             
                                                      ck,surfaces)  
                                        geometric        a surface) 


                                        surface)                    

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     T                [TRANS](docs/ 
                                    co  [TRIANGULATE](d             

                                                      mmands/TRANS. 
                                    ht  ocs/commands/TR             

                                                      ml)           
                                        IAGN.html)                  

                                                      (translate no 
                                    de  ( ..a polygon)              

                                                      coordinates)  


                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     U                [UNG2AVS](doc 
                                    s/  [UPSCALE](docs/             

                                                      commands/UNG2 
                                    AV  commands/UPSCAL             

                                                      S.html)       
                                        E.html)                     

                                                      (UNGenerate t 
                                    o   (attribute from             

                                                      AVS)          
                                        fine to coarse              


                                        grid)                       

                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           
                                     Z                [ZQ](docs/com 
                                    ma                              

                                                      nds/ZQ.html)  


                                                      (depreciated, 


                                                      see           


                                                      [cmo/setatt]( 
                                    do                              

                                                      cs/commands/c 
                                    mo                              

                                                      /cmo_setatt.h 
                                    tm                              

                                                      l))           


                                    +-----------------+-------------- 
                                    ---+-----------------+----------- 
                                    ------+                           

                                                                

                                    ![](http://www.lanl.gov/images/tr 
                                    ansparent.gif){.strut             
                                    width="420" height="1"}           

