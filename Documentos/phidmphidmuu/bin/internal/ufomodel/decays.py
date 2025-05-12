# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.2.0 for Mac OS X ARM (64-bit) (December 26, 2024)
# Date: Wed 7 May 2025 13:31:47


from object_library import all_decays, Decay
import particles as P


Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.phidm,P.phidm):'(lsh**2*vev**2*cmath.sqrt(MH**4 - 4*MH**2*msdm**2))/(8.*cmath.pi*abs(MH)**3)'})

Decay_phidm = Decay(name = 'Decay_phidm',
                    particle = P.phidm,
                    partial_widths = {(P.d,P.d__tilde__):'((-24*gq**2*MD**2 + 6*gq**2*msdm**2)*cmath.sqrt(-4*MD**2*msdm**2 + msdm**4))/(16.*cmath.pi*abs(msdm)**3)',
                                      (P.s,P.s__tilde__):'((-24*gq**2*MS**2 + 6*gq**2*msdm**2)*cmath.sqrt(-4*MS**2*msdm**2 + msdm**4))/(16.*cmath.pi*abs(msdm)**3)',
                                      (P.b,P.b__tilde__):'((-24*gq**2*MB**2 + 6*gq**2*msdm**2)*cmath.sqrt(-4*MB**2*msdm**2 + msdm**4))/(16.*cmath.pi*abs(msdm)**3)',
                                      (P.u,P.u__tilde__):'((6*gq**2*msdm**2 - 24*gq**2*MU**2)*cmath.sqrt(msdm**4 - 4*msdm**2*MU**2))/(16.*cmath.pi*abs(msdm)**3)',
                                      (P.c,P.c__tilde__):'((-24*gq**2*MC**2 + 6*gq**2*msdm**2)*cmath.sqrt(-4*MC**2*msdm**2 + msdm**4))/(16.*cmath.pi*abs(msdm)**3)',
                                      (P.t,P.t__tilde__):'((6*gq**2*msdm**2 - 24*gq**2*MT**2)*cmath.sqrt(msdm**4 - 4*msdm**2*MT**2))/(16.*cmath.pi*abs(msdm)**3)'})



import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(1.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            '36:all = on',  # Habilitar la producción de Higgs
            '36:m0 = 125.0',  # Masa del Higgs
            '35:all = on',  # Habilitar la producción de la partícula phi
            '35:m0 = 500.0',  # Masa de phi, ajusta según tu modelo
            '35:decay = on',  # Decaimientos de phi a partículas H
        ),
	parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CUEP8M1Settings',
            'processParameters',
        )
    )
)

ProductionFilterSequence = cms.Sequence(generator)
