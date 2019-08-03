# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
from textRepr import *
#import __main__
#execfile("e:/Downloads/abqPyCode/odbMax.py")
# abaqus cae noGUI=odbMax.py


def envelopeMax():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior

    o1 = session.openOdb(name='E:/Downloads/abqPyCode/blockpull.odb',readOnly=False)
    currentViewPortName=session.currentViewportName
    #print(currentViewPortName)
    currentViewPort=session.viewports[currentViewPortName]
    #currentViewPort.setValues(displayedObject=o1)
    #: ---- Creating Field Output From Frames ----
    sessionStep = o1.Step(name='Session_Step_max', description='Step for max fields', domain=TIME, timePeriod=1.0)
    reservedFrame = sessionStep.Frame(frameId=0, frameValue=0.0, 
        description='Session Frame')
    sessionFrame = sessionStep.Frame(frameId=1, frameValue=0.0, description='The maximum value over all selected frames')
    frames_in_step_0=o1.steps['Step-1'].frames
    num_frames=len(frames_in_step_0)
    print('num_frames={}'.format(num_frames))

    list_ACYIELD=[frames_in_step_0[i].fieldOutputs['AC YIELD'] for i in range(num_frames)]
    (tmpField_ACYIELD, tmpIndex_ACYIELD) = visualization.maxEnvelope(list_ACYIELD)

    list_CF=[frames_in_step_0[i].fieldOutputs['CF'] for i in range(num_frames)]
    (tmpField_CF, tmpIndex_CF) = visualization.maxEnvelope(list_CF, MAGNITUDE)

    list_LE=[frames_in_step_0[i].fieldOutputs['LE'] for i in range(num_frames)]
    (tmpField_LE, tmpIndex_LE) = visualization.maxEnvelope(list_LE, MAX_PRINCIPAL)

    list_PE=[frames_in_step_0[i].fieldOutputs['PE'] for i in range(num_frames)]
    (tmpField_PE, tmpIndex_PE) = visualization.maxEnvelope(list_PE, MAX_PRINCIPAL)

    list_PEEQ=[frames_in_step_0[i].fieldOutputs['PEEQ'] for i in range(num_frames)]
    (tmpField_PEEQ, tmpIndex_PEEQ) = visualization.maxEnvelope(list_PEEQ)

    list_PEMAG=[frames_in_step_0[i].fieldOutputs['PEMAG'] for i in range(num_frames)]
    (tmpField_PEMAG, tmpIndex_PEMAG) = visualization.maxEnvelope(list_PEMAG)

    list_RF=[frames_in_step_0[i].fieldOutputs['RF'] for i in range(num_frames)]
    (tmpField_RF, tmpIndex_RF) = visualization.maxEnvelope(list_RF, MAGNITUDE)

    list_S=[frames_in_step_0[i].fieldOutputs['S'] for i in range(num_frames)]
    (tmpField_S, tmpIndex_S) = visualization.maxEnvelope(list_S, MISES)

    list_U=[frames_in_step_0[i].fieldOutputs['U'] for i in range(num_frames)]
    (tmpField_U, tmpIndex_U) = visualization.maxEnvelope(list_U, MAGNITUDE)
    #print(type(tmpIndex_LE))
    #prettyPrint(tmpIndex_LE.values[1])
    #print('tmpIndex={}'.format(tmpIndex_LE))
#    currentOdb = session.odbs[odbFullPath]
#    scratchOdb = session.ScratchOdb(odb=currentOdb)

    sessionField = sessionFrame.FieldOutput(name='AC YIELD_max', description='Active yield flag (maximum envelope)', field=tmpField_ACYIELD)
    sessionField = sessionFrame.FieldOutput(name='AC YIELD_max_Index', description='Indices into list of AC YIELD fields selected for maximum envelope', field=tmpIndex_ACYIELD)
    sessionField = sessionFrame.FieldOutput(name='CF_max', description='Point loads (maximum envelope) using Magnitude', field=tmpField_CF)
    sessionField = sessionFrame.FieldOutput(name='CF_max_Index', description='Indices into list of CF fields selected for maximum envelope', field=tmpIndex_CF)
    sessionField = sessionFrame.FieldOutput(name='LE_max', description='Logarithmic strain components (maximum envelope) using Max. Principal', field=tmpField_LE)
    sessionField = sessionFrame.FieldOutput(name='LE_max_Index', description='Indices into list of LE fields selected for maximum envelope', field=tmpIndex_LE)
    sessionField = sessionFrame.FieldOutput(name='PE_max', description='Plastic strain components (maximum envelope) using Max. Principal', field=tmpField_PE)
    sessionField = sessionFrame.FieldOutput(name='PE_max_Index', description='Indices into list of PE fields selected for maximum envelope', field=tmpIndex_PE)
    sessionField = sessionFrame.FieldOutput(name='PEEQ_max', description='Equivalent plastic strain (maximum envelope)', field=tmpField_PEEQ)
    sessionField = sessionFrame.FieldOutput(name='PEEQ_max_Index', description='Indices into list of PEEQ fields selected for maximum envelope', field=tmpIndex_PEEQ)
    sessionField = sessionFrame.FieldOutput(name='PEMAG_max', description='Magnitude of plastic strain (maximum envelope)', field=tmpField_PEMAG)
    sessionField = sessionFrame.FieldOutput(name='PEMAG_max_Index', description='Indices into list of PEMAG fields selected for maximum envelope', field=tmpIndex_PEMAG)
    sessionField = sessionFrame.FieldOutput(name='RF_max', description='Reaction force (maximum envelope) using Magnitude', field=tmpField_RF)
    sessionField = sessionFrame.FieldOutput(name='RF_max_Index', description='Indices into list of RF fields selected for maximum envelope', field=tmpIndex_RF)
    sessionField = sessionFrame.FieldOutput(name='S_max', description='Stress components (maximum envelope) using Mises', field=tmpField_S)
    sessionField = sessionFrame.FieldOutput(name='S_max_Index', description='Indices into list of S fields selected for maximum envelope', field=tmpIndex_S)
    sessionField = sessionFrame.FieldOutput(name='U_max', description='Spatial displacement (maximum envelope) using Magnitude', field=tmpField_U)
    sessionField = sessionFrame.FieldOutput(name='U_max_Index', description='Indices into list of U fields selected for maximum envelope', field=tmpIndex_U)

    o1.save()
##    #: ---- End of Creating Field Output From Frames ----

#def prtest():
#    print('hello')
#
#print('hello world')
#prtest()
envelopeMax()
