# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.2.0 for Mac OS X ARM (64-bit) (December 26, 2024)
# Date: Wed 7 May 2025 13:31:47


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.chi, P.chi, P.phidm, P.phidm ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_3})

V_2 = Vertex(name = 'V_2',
             particles = [ P.G0, P.G0, P.phidm, P.phidm ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_4})

V_3 = Vertex(name = 'V_3',
             particles = [ P.G__minus__, P.G__plus__, P.phidm, P.phidm ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_4})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.phidm, P.phidm ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_4})

V_5 = Vertex(name = 'V_5',
             particles = [ P.phidm, P.phidm, P.phidm, P.phidm ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_2})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.phidm, P.phidm ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_5})

V_7 = Vertex(name = 'V_7',
             particles = [ P.d__tilde__, P.d, P.phidm ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1})

V_8 = Vertex(name = 'V_8',
             particles = [ P.s__tilde__, P.s, P.phidm ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1})

V_9 = Vertex(name = 'V_9',
             particles = [ P.b__tilde__, P.b, P.phidm ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_1})

V_10 = Vertex(name = 'V_10',
              particles = [ P.u__tilde__, P.u, P.phidm ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_1})

V_11 = Vertex(name = 'V_11',
              particles = [ P.c__tilde__, P.c, P.phidm ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_1})

V_12 = Vertex(name = 'V_12',
              particles = [ P.t__tilde__, P.t, P.phidm ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_1})

