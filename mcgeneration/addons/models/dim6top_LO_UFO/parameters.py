# This file was automatically created by FeynRules 2.3.27
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Sun 20 Aug 2017 21:26:04



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
Lambda = Parameter(name = 'Lambda',
                   nature = 'external',
                   type = 'real',
                   value = 1000,
                   texname = '\\text{Lambda}',
                   lhablock = 'DIM6',
                   lhacode = [ 1 ])

ctp = Parameter(name = 'ctp',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{ctp}',
                lhablock = 'DIM6',
                lhacode = [ 2 ])

ctpI = Parameter(name = 'ctpI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctpI}',
                 lhablock = 'DIM6',
                 lhacode = [ 3 ])

cpQM = Parameter(name = 'cpQM',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cpQM}',
                 lhablock = 'DIM6',
                 lhacode = [ 4 ])

cpQ3 = Parameter(name = 'cpQ3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cpQ3}',
                 lhablock = 'DIM6',
                 lhacode = [ 5 ])

cpt = Parameter(name = 'cpt',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cpt}',
                lhablock = 'DIM6',
                lhacode = [ 6 ])

cpb = Parameter(name = 'cpb',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cpb}',
                lhablock = 'DIM6',
                lhacode = [ 7 ])

cptb = Parameter(name = 'cptb',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cptb}',
                 lhablock = 'DIM6',
                 lhacode = [ 8 ])

cptbI = Parameter(name = 'cptbI',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cptbI}',
                  lhablock = 'DIM6',
                  lhacode = [ 9 ])

ctW = Parameter(name = 'ctW',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{ctW}',
                lhablock = 'DIM6',
                lhacode = [ 10 ])

ctZ = Parameter(name = 'ctZ',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{ctZ}',
                lhablock = 'DIM6',
                lhacode = [ 11 ])

ctWI = Parameter(name = 'ctWI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctWI}',
                 lhablock = 'DIM6',
                 lhacode = [ 12 ])

ctZI = Parameter(name = 'ctZI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctZI}',
                 lhablock = 'DIM6',
                 lhacode = [ 13 ])

cbW = Parameter(name = 'cbW',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{cbW}',
                lhablock = 'DIM6',
                lhacode = [ 14 ])

cbWI = Parameter(name = 'cbWI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cbWI}',
                 lhablock = 'DIM6',
                 lhacode = [ 15 ])

ctG = Parameter(name = 'ctG',
                nature = 'external',
                type = 'real',
                value = 0.,
                texname = '\\text{ctG}',
                lhablock = 'DIM6',
                lhacode = [ 16 ])

ctGI = Parameter(name = 'ctGI',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctGI}',
                 lhablock = 'DIM6',
                 lhacode = [ 17 ])

cQlM1 = Parameter(name = 'cQlM1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQlM1}',
                  lhablock = 'DIM6',
                  lhacode = [ 18 ])

cQlM2 = Parameter(name = 'cQlM2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQlM2}',
                  lhablock = 'DIM6',
                  lhacode = [ 19 ])

cQlM3 = Parameter(name = 'cQlM3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQlM3}',
                  lhablock = 'DIM6',
                  lhacode = [ 20 ])

cQl31 = Parameter(name = 'cQl31',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQl31}',
                  lhablock = 'DIM6',
                  lhacode = [ 21 ])

cQl32 = Parameter(name = 'cQl32',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQl32}',
                  lhablock = 'DIM6',
                  lhacode = [ 22 ])

cQl33 = Parameter(name = 'cQl33',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQl33}',
                  lhablock = 'DIM6',
                  lhacode = [ 23 ])

cQe1 = Parameter(name = 'cQe1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQe1}',
                 lhablock = 'DIM6',
                 lhacode = [ 24 ])

cQe2 = Parameter(name = 'cQe2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQe2}',
                 lhablock = 'DIM6',
                 lhacode = [ 25 ])

cQe3 = Parameter(name = 'cQe3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQe3}',
                 lhablock = 'DIM6',
                 lhacode = [ 26 ])

ctl1 = Parameter(name = 'ctl1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctl1}',
                 lhablock = 'DIM6',
                 lhacode = [ 27 ])

ctl2 = Parameter(name = 'ctl2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctl2}',
                 lhablock = 'DIM6',
                 lhacode = [ 28 ])

ctl3 = Parameter(name = 'ctl3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctl3}',
                 lhablock = 'DIM6',
                 lhacode = [ 29 ])

cte1 = Parameter(name = 'cte1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cte1}',
                 lhablock = 'DIM6',
                 lhacode = [ 30 ])

cte2 = Parameter(name = 'cte2',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cte2}',
                 lhablock = 'DIM6',
                 lhacode = [ 31 ])

cte3 = Parameter(name = 'cte3',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cte3}',
                 lhablock = 'DIM6',
                 lhacode = [ 32 ])

ctlS1 = Parameter(name = 'ctlS1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlS1}',
                  lhablock = 'DIM6',
                  lhacode = [ 33 ])

ctlSI1 = Parameter(name = 'ctlSI1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlSI1}',
                   lhablock = 'DIM6',
                   lhacode = [ 34 ])

ctlS2 = Parameter(name = 'ctlS2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlS2}',
                  lhablock = 'DIM6',
                  lhacode = [ 35 ])

ctlSI2 = Parameter(name = 'ctlSI2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlSI2}',
                   lhablock = 'DIM6',
                   lhacode = [ 36 ])

ctlS3 = Parameter(name = 'ctlS3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlS3}',
                  lhablock = 'DIM6',
                  lhacode = [ 37 ])

ctlSI3 = Parameter(name = 'ctlSI3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlSI3}',
                   lhablock = 'DIM6',
                   lhacode = [ 38 ])

ctlT1 = Parameter(name = 'ctlT1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlT1}',
                  lhablock = 'DIM6',
                  lhacode = [ 39 ])

ctlTI1 = Parameter(name = 'ctlTI1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlTI1}',
                   lhablock = 'DIM6',
                   lhacode = [ 40 ])

ctlT2 = Parameter(name = 'ctlT2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlT2}',
                  lhablock = 'DIM6',
                  lhacode = [ 41 ])

ctlTI2 = Parameter(name = 'ctlTI2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlTI2}',
                   lhablock = 'DIM6',
                   lhacode = [ 42 ])

ctlT3 = Parameter(name = 'ctlT3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{ctlT3}',
                  lhablock = 'DIM6',
                  lhacode = [ 43 ])

ctlTI3 = Parameter(name = 'ctlTI3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{ctlTI3}',
                   lhablock = 'DIM6',
                   lhacode = [ 44 ])

cblS1 = Parameter(name = 'cblS1',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cblS1}',
                  lhablock = 'DIM6',
                  lhacode = [ 45 ])

cblSI1 = Parameter(name = 'cblSI1',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cblSI1}',
                   lhablock = 'DIM6',
                   lhacode = [ 46 ])

cblS2 = Parameter(name = 'cblS2',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cblS2}',
                  lhablock = 'DIM6',
                  lhacode = [ 47 ])

cblSI2 = Parameter(name = 'cblSI2',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cblSI2}',
                   lhablock = 'DIM6',
                   lhacode = [ 48 ])

cblS3 = Parameter(name = 'cblS3',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cblS3}',
                  lhablock = 'DIM6',
                  lhacode = [ 49 ])

cblSI3 = Parameter(name = 'cblSI3',
                   nature = 'external',
                   type = 'real',
                   value = 0.,
                   texname = '\\text{cblSI3}',
                   lhablock = 'DIM6',
                   lhacode = [ 50 ])

cQq83 = Parameter(name = 'cQq83',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQq83}',
                  lhablock = 'DIM6',
                  lhacode = [ 51 ])

cQq81 = Parameter(name = 'cQq81',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQq81}',
                  lhablock = 'DIM6',
                  lhacode = [ 52 ])

cQu8 = Parameter(name = 'cQu8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQu8}',
                 lhablock = 'DIM6',
                 lhacode = [ 53 ])

cQd8 = Parameter(name = 'cQd8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQd8}',
                 lhablock = 'DIM6',
                 lhacode = [ 54 ])

ctq8 = Parameter(name = 'ctq8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctq8}',
                 lhablock = 'DIM6',
                 lhacode = [ 55 ])

ctu8 = Parameter(name = 'ctu8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctu8}',
                 lhablock = 'DIM6',
                 lhacode = [ 56 ])

ctd8 = Parameter(name = 'ctd8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctd8}',
                 lhablock = 'DIM6',
                 lhacode = [ 57 ])

cQq13 = Parameter(name = 'cQq13',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQq13}',
                  lhablock = 'DIM6',
                  lhacode = [ 58 ])

cQq11 = Parameter(name = 'cQq11',
                  nature = 'external',
                  type = 'real',
                  value = 0.,
                  texname = '\\text{cQq11}',
                  lhablock = 'DIM6',
                  lhacode = [ 59 ])

cQu1 = Parameter(name = 'cQu1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQu1}',
                 lhablock = 'DIM6',
                 lhacode = [ 60 ])

cQd1 = Parameter(name = 'cQd1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQd1}',
                 lhablock = 'DIM6',
                 lhacode = [ 61 ])

ctq1 = Parameter(name = 'ctq1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctq1}',
                 lhablock = 'DIM6',
                 lhacode = [ 62 ])

ctu1 = Parameter(name = 'ctu1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctu1}',
                 lhablock = 'DIM6',
                 lhacode = [ 63 ])

ctd1 = Parameter(name = 'ctd1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctd1}',
                 lhablock = 'DIM6',
                 lhacode = [ 64 ])

cQQ1 = Parameter(name = 'cQQ1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQQ1}',
                 lhablock = 'DIM6',
                 lhacode = [ 65 ])

cQQ8 = Parameter(name = 'cQQ8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQQ8}',
                 lhablock = 'DIM6',
                 lhacode = [ 66 ])

cQt1 = Parameter(name = 'cQt1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQt1}',
                 lhablock = 'DIM6',
                 lhacode = [ 67 ])

cQb1 = Parameter(name = 'cQb1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQb1}',
                 lhablock = 'DIM6',
                 lhacode = [ 68 ])

ctt1 = Parameter(name = 'ctt1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctt1}',
                 lhablock = 'DIM6',
                 lhacode = [ 69 ])

ctb1 = Parameter(name = 'ctb1',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctb1}',
                 lhablock = 'DIM6',
                 lhacode = [ 70 ])

cQt8 = Parameter(name = 'cQt8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQt8}',
                 lhablock = 'DIM6',
                 lhacode = [ 71 ])

cQb8 = Parameter(name = 'cQb8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{cQb8}',
                 lhablock = 'DIM6',
                 lhacode = [ 72 ])

ctb8 = Parameter(name = 'ctb8',
                 nature = 'external',
                 type = 'real',
                 value = 0.,
                 texname = '\\text{ctb8}',
                 lhablock = 'DIM6',
                 lhacode = [ 73 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

cQQplus = Parameter(name = 'cQQplus',
                    nature = 'internal',
                    type = 'real',
                    value = 'cQQ1/2+cQQ8/6',
                    texname = '\\text{cQQplus}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

ctA = Parameter(name = 'ctA',
                nature = 'internal',
                type = 'real',
                value = '(ctW-cw*ctZ)/sw',
                texname = '\\text{ctA}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

