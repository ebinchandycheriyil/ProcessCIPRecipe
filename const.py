
class tagDetails:
    def __init__(self,desc,datatype,dbAddr,PLCAddr, unit = "°C"):
        # self.id = id
        self.description = desc
        self.datatype = datatype
        self.dbAddr = dbAddr
        self.PLCAddr = PLCAddr
        self.unit = unit



variableList={'HWSA_1' : tagDetails('FlowRate For PreRinse', 'INT', 'SP_1', 'Program:CktA.PreRinseProcessPara.FlowSetValue'),
'HWSA_2' : tagDetails('Return Conductivity 1 For PreRinse', 'INT', 'SP_2', 'Program:CktA.PreRinseProcessPara.ReturnConductSetValue1'),
'HWSA_3' : tagDetails('Tank Set Temp for Hot water Circulation', 'INT', 'SP_3', 'Program:CktA.HWCirProcessPara.TankTempSetValue'),
'HWSA_4' : tagDetails('Flow Rate for Hot water Circulation', 'INT', 'SP_4', 'Program:CktA.HWCirProcessPara.FlowSetValue'),
'HWSA_5' : tagDetails('Return Temp for Hot water Circulation', 'INT', 'SP_5', 'Program:CktA.HWCirProcessPara.ReturnTempSetValue'),
'HWSA_6' : tagDetails('Return Conductivity Hot water Circulation', 'INT', 'SP_6', 'Program:CktA.HWCirProcessPara.ReturnConductSetValue1'),
'HWSA_7' : tagDetails('PrepTempSetValue', 'INT', 'SP_7', 'Program:CktA.HWCirProcessPara.PrepTempSetValue'),
'HWTA_1' : tagDetails('PreRinse Cycle Time', 'Time', 'T_1', 'Program:CktA.PreRinseTimerPara.PreRinseCycleTime'),
'HWTA_2' : tagDetails('Return Pump On Time For PreRinse', 'Time', 'T_2', 'Program:CktA.PreRinseTimerPara.ReturnPumpOnTime'),
'HWTA_3' : tagDetails('Supply Pump On Time For PreRinse', 'Time', 'T_3', 'Program:CktA.PreRinseTimerPara.SupplyPumpOnTime'),
'HWTA_4' : tagDetails('Intermediate stop time For PreRinse', 'Time', 'T_4', 'Program:CktA.PreRinseTimerPara.InterMediateStopTime'),
'HWTA_5' : tagDetails('Pushing Time For PreRinse', 'Time', 'T_5', 'Program:CktA.PreRinseTimerPara.PushingTime'),
'HWTA_6' : tagDetails('Drain Time For PreRinse', 'Time', 'T_6', 'Program:CktA.PreRinseTimerPara.DrainTime'),
'HWTA_7' : tagDetails('Hot Water Circulation Time Hot water Circulation', 'Time', 'T_7', 'Program:CktA.HWCirTimePara.HwCircCycleTime'),
'HWTA_8' : tagDetails('Return Pump On Time Hot water Circulation', 'Time', 'T_8', 'Program:CktA.HWCirTimePara.ReturnPumpOnTime'),
'HWTA_9' : tagDetails('Supply Pump On Time Hot water Circulation', 'Time', 'T_9', 'Program:CktA.HWCirTimePara.SupplyPumpOnTime'),
'HWTA_10' : tagDetails('Intermediate stop time Hot water Circulation', 'Time', 'T_10', 'Program:CktA.HWCirTimePara.InterMediateStopTime'),
'HWTA_11' : tagDetails('Pushing Time Hot water Circulation', 'Time', 'T_11', 'Program:CktA.HWCirTimePara.PushingTime'),
'HWTA_12' : tagDetails('Return Pump On TimeFlow for Hot Water Circulation', 'Time', 'T_12', 'Program:CktA.HWCirTimePara.ReturnPumpOnTimeFlow'),
'HWTA_13' : tagDetails('Return Pump On TimeFlow for Prerinse Circulation', 'Time', 'T_13', 'Program:CktA.PreRinseTimerPara.ReturnPumpOnTimeFlow'),
'HWSB_1' : tagDetails('FlowRate For PreRinse', 'INT', 'SP_1', 'Program:CktB.PreRinseProcessPara.FlowSetValue'),
'HWSB_2' : tagDetails('Return Conductivity 1 For PreRinse', 'INT', 'SP_2', 'Program:CktB.PreRinseProcessPara.ReturnConductSetValue1'),
'HWSB_3' : tagDetails('Tank Set Temp for Hot water Circulation', 'INT', 'SP_3', 'Program:CktB.HWCirProcessPara.TankTempSetValue'),
'HWSB_4' : tagDetails('Flow Rate for Hot water Circulation', 'INT', 'SP_4', 'Program:CktB.HWCirProcessPara.FlowSetValue'),
'HWSB_5' : tagDetails('Return Temp for Hot water Circulation', 'INT', 'SP_5', 'Program:CktB.HWCirProcessPara.ReturnTempSetValue'),
'HWSB_6' : tagDetails('Return Conductivity Hot water Circulation', 'INT', 'SP_6', 'Program:CktB.HWCirProcessPara.ReturnConductSetValue1'),
'HWSB_7' : tagDetails('PrepTempSetValue', 'INT', 'SP_7', 'Program:CktB.HWCirProcessPara.PrepTempSetValue'),
'HWTB_1' : tagDetails('PreRinse Cycle Time', 'Time', 'T_1', 'Program:CktB.PreRinseTimerPara.PreRinseCycleTime'),
'HWTB_2' : tagDetails('Return Pump On Time For PreRinse', 'Time', 'T_2', 'Program:CktB.PreRinseTimerPara.ReturnPumpOnTime'),
'HWTB_3' : tagDetails('Supply Pump On Time For PreRinse', 'Time', 'T_3', 'Program:CktB.PreRinseTimerPara.SupplyPumpOnTime'),
'HWTB_4' : tagDetails('Intermediate stop time For PreRinse', 'Time', 'T_4', 'Program:CktB.PreRinseTimerPara.InterMediateStopTime'),
'HWTB_5' : tagDetails('Pushing Time For PreRinse', 'Time', 'T_5', 'Program:CktB.PreRinseTimerPara.PushingTime'),
'HWTB_6' : tagDetails('Drain Time For PreRinse', 'Time', 'T_6', 'Program:CktB.PreRinseTimerPara.DrainTime'),
'HWTB_7' : tagDetails('Hot Water Circulation Time Hot water Circulation', 'Time', 'T_7', 'Program:CktB.HWCirTimePara.HwCircCycleTime'),
'HWTB_8' : tagDetails('Return Pump On Time Hot water Circulation', 'Time', 'T_8', 'Program:CktB.HWCirTimePara.ReturnPumpOnTime'),
'HWTB_9' : tagDetails('Supply Pump On Time Hot water Circulation', 'Time', 'T_9', 'Program:CktB.HWCirTimePara.SupplyPumpOnTime'),
'HWTB_10' : tagDetails('Intermediate stop time Hot water Circulation', 'Time', 'T_10', 'Program:CktB.HWCirTimePara.InterMediateStopTime'),
'HWTB_11' : tagDetails('Pushing Time Hot water Circulation', 'Time', 'T_11', 'Program:CktB.HWCirTimePara.PushingTime'),
'HWTB_12' : tagDetails('Return Pump On TimeFlow for Hot Water Circulation', 'Time', 'T_12', 'Program:CktA.HWCirTimePara.ReturnPumpOnTimeFlow'),
'HWTB_13' : tagDetails('Return Pump On TimeFlow for Prerinse Circulation', 'Time', 'T_13', 'Program:CktA.PreRinseTimerPara.ReturnPumpOnTimeFlow'),
'LYSA_1' : tagDetails('FlowRate For PreRinse', 'INT', 'SP_1', 'Program:CktA.PreRinseProcessPara.FlowSetValue'),
'LYSA_2' : tagDetails('Return Conductivity 1 For PreRinse', 'INT', 'SP_2', 'Program:CktA.PreRinseProcessPara.ReturnConductSetValue1'),
'LYSA_3' : tagDetails('Tank Set Temp for Hot water Circulation', 'INT', 'SP_3', 'Program:CktA.HWCirProcessPara.TankTempSetValue'),
'LYSA_4' : tagDetails('Flow Rate for Hot water Circulation', 'INT', 'SP_4', 'Program:CktA.HWCirProcessPara.FlowSetValue'),
'LYSA_5' : tagDetails('Return Temp for Hot water Circulation', 'INT', 'SP_5', 'Program:CktA.HWCirProcessPara.ReturnTempSetValue'),
'LYSA_6' : tagDetails('Return Conductivity Hot water Circulation', 'INT', 'SP_6', 'Program:CktA.HWCirProcessPara.ReturnConductSetValue1'),
'LYSA_7' : tagDetails('Tank Temp Set Value for Caustic Circulation', 'INT', 'SP_7', 'Program:CktA.CausticCirProcessPara.TankTempSetValue'),
'LYSA_8' : tagDetails('Flow Rate for Caustic Circulation', 'INT', 'SP_8', 'Program:CktA.CausticCirProcessPara.FlowSetValue'),
'LYSA_9' : tagDetails('Return Temp for Caustic Circulation', 'INT', 'SP_9', 'Program:CktA.CausticCirProcessPara.ReturnTempSetValue'),
'LYSA_10' : tagDetails('Dosing SetValue for Caustic Circulation', 'INT', 'SP_10', 'Program:CktA.CausticCirProcessPara.DosingSetValue'),
'LYSA_11' : tagDetails('Return Conductivity 1 for Caustic Circulation', 'INT', 'SP_11', 'Program:CktA.CausticCirProcessPara.ReturnConductSetValue1'),
'LYSA_12' : tagDetails('Return Conductivity 2 for Caustic Circulation', 'INT', 'SP_12', 'Program:CktA.CausticCirProcessPara.ReturnConductSetValue2'),
'LYSA_13' : tagDetails('Dosing RetSetValue for Caustic Circulation', 'INT', 'SP_13', 'Program:CktA.CausticCirProcessPara.DosingResetValue'),
'LYSA_14' : tagDetails('Hold SetValue for Caustic Circulation', 'INT', 'SP_14', 'Program:CktA.CausticCirProcessPara.HoldSetValue'),
'LYSA_15' : tagDetails('Tank Temp Set Value for Intermediate', 'INT', 'SP_15', 'Program:CktA.IntermediateRinseProcessPara.TankTempSetValue'),
'LYSA_16' : tagDetails('Flow Rate  for Intermediate', 'INT', 'SP_16', 'Program:CktA.IntermediateRinseProcessPara.FlowSetValue'),
'LYSA_17' : tagDetails('Return Temp for Intermediate', 'INT', 'SP_17', 'Program:CktA.IntermediateRinseProcessPara.ReturnTempSetValue'),
'LYSA_18' : tagDetails('Return Conductivity 1 for Intermediate', 'INT', 'SP_18', 'Program:CktA.IntermediateRinseProcessPara.ReturnConductSetValue1'),
'LYSA_19' : tagDetails('Return Conductivity 2  for Intermediate', 'INT', 'SP_19', 'Program:CktA.IntermediateRinseProcessPara.ReturnConductSetValue2'),
'LYSA_20' : tagDetails('Return Conductivity 3  for Intermediate', 'INT', 'SP_20', 'Program:CktA.IntermediateRinseProcessPara.ReturnConductSetValue3'),
'LYTA_1' : tagDetails('PreRinse Cycle Time', 'Time', 'T_1', 'Program:CktA.PreRinseTimerPara.PreRinseCycleTime'),
'LYTA_2' : tagDetails('Return Pump On Time For PreRinse', 'Time', 'T_2', 'Program:CktA.PreRinseTimerPara.ReturnPumpOnTime'),
'LYTA_3' : tagDetails('Supply Pump On Time For PreRinse', 'Time', 'T_3', 'Program:CktA.PreRinseTimerPara.SupplyPumpOnTime'),
'LYTA_4' : tagDetails('Intermediate stop time For PreRinse', 'Time', 'T_4', 'Program:CktA.PreRinseTimerPara.InterMediateStopTime'),
'LYTA_5' : tagDetails('Pushing Time For PreRinse', 'Time', 'T_5', 'Program:CktA.PreRinseTimerPara.PushingTime'),
'LYTA_6' : tagDetails('Drain Time For PreRinse', 'Time', 'T_6', 'Program:CktA.PreRinseTimerPara.DrainTime'),
'LYTA_7' : tagDetails('Hot Water Circulation Time Hot water Circulation', 'Time', 'T_7', 'Program:CktA.HWCirTimePara.HwCircCycleTime'),
'LYTA_8' : tagDetails('Return Pump On Time Hot water Circulation', 'Time', 'T_8', 'Program:CktA.HWCirTimePara.ReturnPumpOnTime'),
'LYTA_9' : tagDetails('Supply Pump On Time Hot water Circulation', 'Time', 'T_9', 'Program:CktA.HWCirTimePara.SupplyPumpOnTime'),
'LYTA_10' : tagDetails('Intermediate stop time Hot water Circulation', 'Time', 'T_10', 'Program:CktA.HWCirTimePara.InterMediateStopTime'),
'LYTA_11' : tagDetails('Pushing Time Hot water Circulation', 'Time', 'T_11', 'Program:CktA.HWCirTimePara.PushingTime'),
'LYTA_12' : tagDetails('Return Pump On Time for Caustic Circulation', 'Time', 'T_12', 'Program:CktA.CausticCirTimerPara.ReturnPumpOnTime'),
'LYTA_13' : tagDetails('Supply Pump On Time for Caustic Circulation', 'Time', 'T_13', 'Program:CktA.CausticCirTimerPara.SupplyPumpOnTime'),
'LYTA_14' : tagDetails('Intermediate stop time for Caustic Circulation', 'Time', 'T_14', 'Program:CktA.CausticCirTimerPara.InterMediateStopTime'),
'LYTA_15' : tagDetails('Pushing Time for Caustic Circulation', 'Time', 'T_15', 'Program:CktA.CausticCirTimerPara.PushingTime'),
'LYTA_16' : tagDetails('Return Pump Off Time  for Caustic Circulation', 'Time', 'T_16', 'Program:CktA.CausticCirTimerPara.RPumpOffTime'),
'LYTA_17' : tagDetails('Drain Time for Caustic Circulation', 'Time', 'T_17', 'Program:CktA.CausticCirTimerPara.DrainTime'),
'LYTA_18' : tagDetails('Caustic Cycle Time for Caustic Circulation', 'Time', 'T_18', 'Program:CktA.CausticCirTimerPara.LyeCircCycleTime'),
'LYTA_19' : tagDetails('InterMediate CIP Time for Intermediate', 'Time', 'T_19', 'Program:CktA.IntermediateRinseTimerPara.InterMediateCycleTime'),
'LYTA_20' : tagDetails('Return Pump On Time for Intermediate', 'Time', 'T_20', 'Program:CktA.IntermediateRinseTimerPara.ReturnPumpOnTime'),
'LYTA_21' : tagDetails('Supply Pump On Time for Intermediate', 'Time', 'T_21', 'Program:CktA.IntermediateRinseTimerPara.SupplyPumpOnTime'),
'LYTA_22' : tagDetails('Intermediate stop time for Intermediate', 'Time', 'T_22', 'Program:CktA.IntermediateRinseTimerPara.InterMediateStopTime'),
'LYTA_23' : tagDetails('Pushing Time for Intermediate', 'Time', 'T_23', 'Program:CktA.IntermediateRinseTimerPara.PushingTime'),
'LYTA_24' : tagDetails('Drain Time for Intermediate', 'Time', 'T_24', 'Program:CktA.IntermediateRinseTimerPara.DrainTime'),
'LYTA_25' : tagDetails('Return Pump On TimeFlow for Hot Water Circulation', 'Time', 'T_25', 'Program:CktA.HWCirTimePara.ReturnPumpOnTimeFlow'),
'LYTA_26' : tagDetails('Return Pump On TimeFlow for Prerinse Circulation', 'Time', 'T_26', 'Program:CktA.PreRinseTimerPara.ReturnPumpOnTimeFlow'),
'LYTA_27' : tagDetails('Return Pump On TimeFlow for Castic Circulation', 'Time', 'T_27', 'Program:CktA.CausticCirTimerPara.ReturnPumpOnTimeFlow'),
'LYTA_28' : tagDetails('Return Pump On TimeFlow for Intermediate Circulation', 'Time', 'T_28', 'Program:CktA.IntermediateRinseTimerPara.ReturnPumpOnTimeFlow'),
'LYSB_1' : tagDetails('FlowRate For PreRinse', 'INT', 'SP_1', 'Program:CktB.PreRinseProcessPara.FlowSetValue'),
'LYSB_2' : tagDetails('Return Conductivity 1 For PreRinse', 'INT', 'SP_2', 'Program:CktB.PreRinseProcessPara.ReturnConductSetValue1'),
'LYSB_3' : tagDetails('Tank Set Temp for Hot water Circulation', 'INT', 'SP_3', 'Program:CktB.HWCirProcessPara.TankTempSetValue'),
'LYSB_4' : tagDetails('Flow Rate for Hot water Circulation', 'INT', 'SP_4', 'Program:CktB.HWCirProcessPara.FlowSetValue'),
'LYSB_5' : tagDetails('Return Temp for Hot water Circulation', 'INT', 'SP_5', 'Program:CktB.HWCirProcessPara.ReturnTempSetValue'),
'LYSB_6' : tagDetails('Return Conductivity Hot water Circulation', 'INT', 'SP_6', 'Program:CktB.HWCirProcessPara.ReturnConductSetValue1'),
'LYSB_7' : tagDetails('Tank Temp Set Value for Caustic Circulation', 'INT', 'SP_7', 'Program:CktB.CausticCirProcessPara.TankTempSetValue'),
'LYSB_8' : tagDetails('Flow Rate for Caustic Circulation', 'INT', 'SP_8', 'Program:CktB.CausticCirProcessPara.FlowSetValue'),
'LYSB_9' : tagDetails('Return Temp for Caustic Circulation', 'INT', 'SP_9', 'Program:CktB.CausticCirProcessPara.ReturnTempSetValue'),
'LYSB_10' : tagDetails('Dosing SetValue for Caustic Circulation', 'INT', 'SP_10', 'Program:CktB.CausticCirProcessPara.DosingSetValue'),
'LYSB_11' : tagDetails('Return Conductivity 1 for Caustic Circulation', 'INT', 'SP_11', 'Program:CktB.CausticCirProcessPara.ReturnConductSetValue1'),
'LYSB_12' : tagDetails('Return Conductivity 2 for Caustic Circulation', 'INT', 'SP_12', 'Program:CktB.CausticCirProcessPara.ReturnConductSetValue2'),
'LYSB_13' : tagDetails('Dosing RetSetValue for Caustic Circulation', 'INT', 'SP_13', 'Program:CktB.CausticCirProcessPara.DosingResetValue'),
'LYSB_14' : tagDetails('Hold SetValue for Caustic Circulation', 'INT', 'SP_14', 'Program:CktB.CausticCirProcessPara.HoldSetValue'),
'LYSB_15' : tagDetails('Tank Temp Set Value for Intermediate', 'INT', 'SP_15', 'Program:CktB.IntermediateRinseProcessPara.TankTempSetValue'),
'LYSB_16' : tagDetails('Flow Rate  for Intermediate', 'INT', 'SP_16', 'Program:CktB.IntermediateRinseProcessPara.FlowSetValue'),
'LYSB_17' : tagDetails('Return Temp for Intermediate', 'INT', 'SP_17', 'Program:CktB.IntermediateRinseProcessPara.ReturnTempSetValue'),
'LYSB_18' : tagDetails('Return Conductivity 1 for Intermediate', 'INT', 'SP_18', 'Program:CktB.IntermediateRinseProcessPara.ReturnConductSetValue1'),
'LYSB_19' : tagDetails('Return Conductivity 2  for Intermediate', 'INT', 'SP_19', 'Program:CktB.IntermediateRinseProcessPara.ReturnConductSetValue2'),
'LYSB_20' : tagDetails('Return Conductivity 3  for Intermediate', 'INT', 'SP_20', 'Program:CktB.IntermediateRinseProcessPara.ReturnConductSetValue3'),
'LYTB_1' : tagDetails('PreRinse Cycle Time', 'Time', 'T_1', 'Program:CktB.PreRinseTimerPara.PreRinseCycleTime'),
'LYTB_2' : tagDetails('Return Pump On Time For PreRinse', 'Time', 'T_2', 'Program:CktB.PreRinseTimerPara.ReturnPumpOnTime'),
'LYTB_3' : tagDetails('Supply Pump On Time For PreRinse', 'Time', 'T_3', 'Program:CktB.PreRinseTimerPara.SupplyPumpOnTime'),
'LYTB_4' : tagDetails('Intermediate stop time For PreRinse', 'Time', 'T_4', 'Program:CktB.PreRinseTimerPara.InterMediateStopTime'),
'LYTB_5' : tagDetails('Pushing Time For PreRinse', 'Time', 'T_5', 'Program:CktB.PreRinseTimerPara.PushingTime'),
'LYTB_6' : tagDetails('Drain Time For PreRinse', 'Time', 'T_6', 'Program:CktB.PreRinseTimerPara.DrainTime'),
'LYTB_7' : tagDetails('Hot Water Circulation Time Hot water Circulation', 'Time', 'T_7', 'Program:CktB.HWCirTimePara.HwCircCycleTime'),
'LYTB_8' : tagDetails('Return Pump On Time Hot water Circulation', 'Time', 'T_8', 'Program:CktB.HWCirTimePara.ReturnPumpOnTime'),
'LYTB_9' : tagDetails('Supply Pump On Time Hot water Circulation', 'Time', 'T_9', 'Program:CktB.HWCirTimePara.SupplyPumpOnTime'),
'LYTB_10' : tagDetails('Intermediate stop time Hot water Circulation', 'Time', 'T_10', 'Program:CktB.HWCirTimePara.InterMediateStopTime'),
'LYTB_11' : tagDetails('Pushing Time Hot water Circulation', 'Time', 'T_11', 'Program:CktB.HWCirTimePara.PushingTime'),
'LYTB_12' : tagDetails('Return Pump On Time for Caustic Circulation', 'Time', 'T_12', 'Program:CktB.CausticCirTimerPara.ReturnPumpOnTime'),
'LYTB_13' : tagDetails('Supply Pump On Time for Caustic Circulation', 'Time', 'T_13', 'Program:CktB.CausticCirTimerPara.SupplyPumpOnTime'),
'LYTB_14' : tagDetails('Intermediate stop time for Caustic Circulation', 'Time', 'T_14', 'Program:CktB.CausticCirTimerPara.InterMediateStopTime'),
'LYTB_15' : tagDetails('Pushing Time for Caustic Circulation', 'Time', 'T_15', 'Program:CktB.CausticCirTimerPara.PushingTime'),
'LYTB_16' : tagDetails('Return Pump Off Time  for Caustic Circulation', 'Time', 'T_16', 'Program:CktB.CausticCirTimerPara.RPumpOffTime'),
'LYTB_17' : tagDetails('Drain Time for Caustic Circulation', 'Time', 'T_17', 'Program:CktB.CausticCirTimerPara.DrainTime'),
'LYTB_18' : tagDetails('Caustic Cycle Time for Caustic Circulation', 'Time', 'T_18', 'Program:CktB.CausticCirTimerPara.LyeCircCycleTime'),
'LYTB_19' : tagDetails('InterMediate CIP Time for Intermediate', 'Time', 'T_19', 'Program:CktB.IntermediateRinseTimerPara.InterMediateCycleTime'),
'LYTB_20' : tagDetails('Return Pump On Time for Intermediate', 'Time', 'T_20', 'Program:CktB.IntermediateRinseTimerPara.ReturnPumpOnTime'),
'LYTB_21' : tagDetails('Supply Pump On Time for Intermediate', 'Time', 'T_21', 'Program:CktB.IntermediateRinseTimerPara.SupplyPumpOnTime'),
'LYTB_22' : tagDetails('Intermediate stop time for Intermediate', 'Time', 'T_22', 'Program:CktB.IntermediateRinseTimerPara.InterMediateStopTime'),
'LYTB_23' : tagDetails('Pushing Time for Intermediate', 'Time', 'T_23', 'Program:CktB.IntermediateRinseTimerPara.PushingTime'),
'LYTB_24' : tagDetails('Drain Time for Intermediate', 'Time', 'T_24', 'Program:CktB.IntermediateRinseTimerPara.DrainTime'),
'LYTB_25' : tagDetails('Return Pump On TimeFlow for Hot Water Circulation', 'Time', 'T_25', 'Program:CktA.HWCirTimePara.ReturnPumpOnTimeFlow'),
'LYTB_26' : tagDetails('Return Pump On TimeFlow for Prerinse Circulation', 'Time', 'T_26', 'Program:CktA.PreRinseTimerPara.ReturnPumpOnTimeFlow'),
'LYTB_27' : tagDetails('Return Pump On TimeFlow for Castic Circulation', 'Time', 'T_27', 'Program:CktA.CausticCirTimerPara.ReturnPumpOnTimeFlow'),
'LYTB_28' : tagDetails('Return Pump On TimeFlow for Intermediate Circulation', 'Time', 'T_28', 'Program:CktA.IntermediateRinseTimerPara.ReturnPumpOnTimeFlow'),
'ACSA_1' : tagDetails('FlowRate For PreRinse', 'INT', 'SP_1', 'Program:CktA.PreRinseProcessPara.FlowSetValue'),
'ACSA_2' : tagDetails('Return Conductivity 1 For PreRinse', 'INT', 'SP_2', 'Program:CktA.PreRinseProcessPara.ReturnConductSetValue1'),
'ACSA_3' : tagDetails('Tank Set Temp for Hot water Circulation', 'INT', 'SP_3', 'Program:CktA.HWCirProcessPara.TankTempSetValue'),
'ACSA_4' : tagDetails('Flow Rate for Hot water Circulation', 'INT', 'SP_4', 'Program:CktA.HWCirProcessPara.FlowSetValue'),
'ACSA_5' : tagDetails('Return Temp for Hot water Circulation', 'INT', 'SP_5', 'Program:CktA.HWCirProcessPara.ReturnTempSetValue'),
'ACSA_6' : tagDetails('Return Conductivity Hot water Circulation', 'INT', 'SP_6', 'Program:CktA.HWCirProcessPara.ReturnConductSetValue1'),
'ACSA_7' : tagDetails('Tank Temp Set Value for Caustic Circulation', 'INT', 'SP_7', 'Program:CktA.CausticCirProcessPara.TankTempSetValue'),
'ACSA_8' : tagDetails('Flow Rate for Caustic Circulation', 'INT', 'SP_8', 'Program:CktA.CausticCirProcessPara.FlowSetValue'),
'ACSA_9' : tagDetails('Return Temp for Caustic Circulation', 'INT', 'SP_9', 'Program:CktA.CausticCirProcessPara.ReturnTempSetValue'),
'ACSA_10' : tagDetails('Dosing SetValue for Caustic Circulation', 'INT', 'SP_10', 'Program:CktA.CausticCirProcessPara.DosingSetValue'),
'ACSA_11' : tagDetails('Return Conductivity 1 for Caustic Circulation', 'INT', 'SP_11', 'Program:CktA.CausticCirProcessPara.ReturnConductSetValue1'),
'ACSA_12' : tagDetails('Return Conductivity 2 for Caustic Circulation', 'INT', 'SP_12', 'Program:CktA.CausticCirProcessPara.ReturnConductSetValue2'),
'ACSA_13' : tagDetails('Dosing RetSetValue for Caustic Circulation', 'INT', 'SP_13', 'Program:CktA.CausticCirProcessPara.DosingResetValue'),
'ACSA_14' : tagDetails('Hold SetValue for Caustic Circulation', 'INT', 'SP_14', 'Program:CktA.CausticCirProcessPara.HoldSetValue'),
'ACSA_15' : tagDetails('Tank Temp Set Value for Intermediate', 'INT', 'SP_15', 'Program:CktA.IntermediateRinseProcessPara.TankTempSetValue'),
'ACSA_16' : tagDetails('Flow Rate  for Intermediate', 'INT', 'SP_16', 'Program:CktA.IntermediateRinseProcessPara.FlowSetValue'),
'ACSA_17' : tagDetails('Return Temp for Intermediate', 'INT', 'SP_17', 'Program:CktA.IntermediateRinseProcessPara.ReturnTempSetValue'),
'ACSA_18' : tagDetails('Return Conductivity 1 for Intermediate', 'INT', 'SP_18', 'Program:CktA.IntermediateRinseProcessPara.ReturnConductSetValue1'),
'ACSA_19' : tagDetails('Return Conductivity 2  for Intermediate', 'INT', 'SP_19', 'Program:CktA.IntermediateRinseProcessPara.ReturnConductSetValue2'),
'ACSA_20' : tagDetails('Return Conductivity 3  for Intermediate', 'INT', 'SP_20', 'Program:CktA.IntermediateRinseProcessPara.ReturnConductSetValue3'),
'ACSA_21' : tagDetails('Tank Temp for Acid Circulation', 'INT', 'SP_21', 'Program:CktA.AcidTankProcessPara.TankTempSetValue'),
'ACSA_22' : tagDetails('Flow Rate for Acid Circulation', 'INT', 'SP_22', 'Program:CktA.AcidTankProcessPara.FlowSetValue'),
'ACSA_23' : tagDetails('Return Temp for Acid Circulation', 'INT', 'SP_23', 'Program:CktA.AcidTankProcessPara.ReturnTempSetValue'),
'ACSA_24' : tagDetails('Dosing SetValue for Acid Circulation', 'INT', 'SP_24', 'Program:CktA.AcidTankProcessPara.DosingSetValue'),
'ACSA_25' : tagDetails('Return Conductivity 1 for Acid Circulation', 'INT', 'SP_25', 'Program:CktA.AcidTankProcessPara.ReturnConductSetValue1'),
'ACSA_26' : tagDetails('Return Conductivity 2 for Acid Circulation', 'INT', 'SP_26', 'Program:CktA.AcidTankProcessPara.ReturnConductSetValue2'),
'ACSA_27' : tagDetails('Dosing RetSetValue for Acid Circulation', 'INT', 'SP_27', 'Program:CktA.AcidTankProcessPara.DosingResetValue'),
'ACSA_28' : tagDetails('Hold SetValue for Acid Circulation', 'INT', 'SP_28', 'Program:CktA.AcidTankProcessPara.HoldSetValue'),
'ACTA_1' : tagDetails('PreRinse Cycle Time', 'Time', 'T_1', 'Program:CktA.PreRinseTimerPara.PreRinseCycleTime'),
'ACTA_2' : tagDetails('Return Pump On Time For PreRinse', 'Time', 'T_2', 'Program:CktA.PreRinseTimerPara.ReturnPumpOnTime'),
'ACTA_3' : tagDetails('Supply Pump On Time For PreRinse', 'Time', 'T_3', 'Program:CktA.PreRinseTimerPara.SupplyPumpOnTime'),
'ACTA_4' : tagDetails('Intermediate stop time For PreRinse', 'Time', 'T_4', 'Program:CktA.PreRinseTimerPara.InterMediateStopTime'),
'ACTA_5' : tagDetails('Pushing Time For PreRinse', 'Time', 'T_5', 'Program:CktA.PreRinseTimerPara.PushingTime'),
'ACTA_6' : tagDetails('Drain Time For PreRinse', 'Time', 'T_6', 'Program:CktA.PreRinseTimerPara.DrainTime'),
'ACTA_7' : tagDetails('Hot Water Circulation Time Hot water Circulation', 'Time', 'T_7', 'Program:CktA.HWCirTimePara.HwCircCycleTime'),
'ACTA_8' : tagDetails('Return Pump On Time Hot water Circulation', 'Time', 'T_8', 'Program:CktA.HWCirTimePara.ReturnPumpOnTime'),
'ACTA_9' : tagDetails('Supply Pump On Time Hot water Circulation', 'Time', 'T_9', 'Program:CktA.HWCirTimePara.SupplyPumpOnTime'),
'ACTA_10' : tagDetails('Intermediate stop time Hot water Circulation', 'Time', 'T_10', 'Program:CktA.HWCirTimePara.InterMediateStopTime'),
'ACTA_11' : tagDetails('Pushing Time Hot water Circulation', 'Time', 'T_11', 'Program:CktA.HWCirTimePara.PushingTime'),
'ACTA_12' : tagDetails('Return Pump On Time for Caustic Circulation', 'Time', 'T_12', 'Program:CktA.CausticCirTimerPara.ReturnPumpOnTime'),
'ACTA_13' : tagDetails('Supply Pump On Time for Caustic Circulation', 'Time', 'T_13', 'Program:CktA.CausticCirTimerPara.SupplyPumpOnTime'),
'ACTA_14' : tagDetails('Intermediate stop time for Caustic Circulation', 'Time', 'T_14', 'Program:CktA.CausticCirTimerPara.InterMediateStopTime'),
'ACTA_15' : tagDetails('Pushing Time for Caustic Circulation', 'Time', 'T_15', 'Program:CktA.CausticCirTimerPara.PushingTime'),
'ACTA_16' : tagDetails('Return Pump Off Time  for Caustic Circulation', 'Time', 'T_16', 'Program:CktA.CausticCirTimerPara.RPumpOffTime'),
'ACTA_17' : tagDetails('Drain Time for Caustic Circulation', 'Time', 'T_17', 'Program:CktA.CausticCirTimerPara.DrainTime'),
'ACTA_18' : tagDetails('Caustic Cycle Time for Caustic Circulation', 'Time', 'T_18', 'Program:CktA.CausticCirTimerPara.LyeCircCycleTime'),
'ACTA_19' : tagDetails('InterMediate CIP Time for Intermediate', 'Time', 'T_19', 'Program:CktA.IntermediateRinseTimerPara.InterMediateCycleTime'),
'ACTA_20' : tagDetails('Return Pump On Time for Intermediate', 'Time', 'T_20', 'Program:CktA.IntermediateRinseTimerPara.ReturnPumpOnTime'),
'ACTA_21' : tagDetails('Supply Pump On Time for Intermediate', 'Time', 'T_21', 'Program:CktA.IntermediateRinseTimerPara.SupplyPumpOnTime'),
'ACTA_22' : tagDetails('Intermediate stop time for Intermediate', 'Time', 'T_22', 'Program:CktA.IntermediateRinseTimerPara.InterMediateStopTime'),
'ACTA_23' : tagDetails('Pushing Time for Intermediate', 'Time', 'T_23', 'Program:CktA.IntermediateRinseTimerPara.PushingTime'),
'ACTA_24' : tagDetails('Drain Time for Intermediate', 'Time', 'T_24', 'Program:CktA.IntermediateRinseTimerPara.DrainTime'),
'ACTA_25' : tagDetails('Return Pump On Time for Acid Circulation', 'Time', 'T_25', 'Program:CktA.AcidTankTimerPara.ReturnPumpOnTime'),
'ACTA_26' : tagDetails('Supply Pump On Time for Acid Circulation', 'Time', 'T_26', 'Program:CktA.AcidTankTimerPara.SupplyPumpOnTime'),
'ACTA_27' : tagDetails('Intermediate stop time for Acid Circulation', 'Time', 'T_27', 'Program:CktA.AcidTankTimerPara.InterMediateStopTime'),
'ACTA_28' : tagDetails('Pushing Time for Acid Circulation', 'Time', 'T_28', 'Program:CktA.AcidTankTimerPara.PushingTime'),
'ACTA_29' : tagDetails('Return Pump Off Time for Acid Circulation', 'Time', 'T_29', 'Program:CktA.AcidTankTimerPara.RPumpOffTime'),
'ACTA_30' : tagDetails('Drain Time for Acid Circulation', 'Time', 'T_30', 'Program:CktA.AcidTankTimerPara.DrainTime'),
'ACTA_31' : tagDetails('Acid Cycle Time for Acid Circulation', 'Time', 'T_31', 'Program:CktA.AcidTankTimerPara.AcidCircCycleTime'),
'ACTA_32' : tagDetails('Return Pump On TimeFlow for Hot Water Circulation', 'Time', 'T_32', 'Program:CktA.HWCirTimePara.ReturnPumpOnTimeFlow'),
'ACTA_33' : tagDetails('Return Pump On TimeFlow for Prerinse Circulation', 'Time', 'T_33', 'Program:CktA.PreRinseTimerPara.ReturnPumpOnTimeFlow'),
'ACTA_34' : tagDetails('Return Pump On TimeFlow for Castic Circulation', 'Time', 'T_34', 'Program:CktA.CausticCirTimerPara.ReturnPumpOnTimeFlow'),
'ACTA_35' : tagDetails('Return Pump On TimeFlow for Intermediate Circulation', 'Time', 'T_35', 'Program:CktA.IntermediateRinseTimerPara.ReturnPumpOnTimeFlow'),
'ACTA_36' : tagDetails('Return Pump On TimeFlow forAcid Circulation', 'Time', 'T_36', 'Program:CktA.AcidTankTimerPara.ReturnPumpOnTimeFlow'),
'ACSB_1' : tagDetails('FlowRate For PreRinse', 'INT', 'SP_1', 'Program:CktB.PreRinseProcessPara.FlowSetValue'),
'ACSB_2' : tagDetails('Return Conductivity 1 For PreRinse', 'INT', 'SP_2', 'Program:CktB.PreRinseProcessPara.ReturnConductSetValue1'),
'ACSB_3' : tagDetails('Tank Set Temp for Hot water Circulation', 'INT', 'SP_3', 'Program:CktB.HWCirProcessPara.TankTempSetValue'),
'ACSB_4' : tagDetails('Flow Rate for Hot water Circulation', 'INT', 'SP_4', 'Program:CktB.HWCirProcessPara.FlowSetValue'),
'ACSB_5' : tagDetails('Return Temp for Hot water Circulation', 'INT', 'SP_5', 'Program:CktB.HWCirProcessPara.ReturnTempSetValue'),
'ACSB_6' : tagDetails('Return Conductivity Hot water Circulation', 'INT', 'SP_6', 'Program:CktB.HWCirProcessPara.ReturnConductSetValue1'),
'ACSB_7' : tagDetails('Tank Temp Set Value for Caustic Circulation', 'INT', 'SP_7', 'Program:CktB.CausticCirProcessPara.TankTempSetValue'),
'ACSB_8' : tagDetails('Flow Rate for Caustic Circulation', 'INT', 'SP_8', 'Program:CktB.CausticCirProcessPara.FlowSetValue'),
'ACSB_9' : tagDetails('Return Temp for Caustic Circulation', 'INT', 'SP_9', 'Program:CktB.CausticCirProcessPara.ReturnTempSetValue'),
'ACSB_10' : tagDetails('Dosing SetValue for Caustic Circulation', 'INT', 'SP_10', 'Program:CktB.CausticCirProcessPara.DosingSetValue'),
'ACSB_11' : tagDetails('Return Conductivity 1 for Caustic Circulation', 'INT', 'SP_11', 'Program:CktB.CausticCirProcessPara.ReturnConductSetValue1'),
'ACSB_12' : tagDetails('Return Conductivity 2 for Caustic Circulation', 'INT', 'SP_12', 'Program:CktB.CausticCirProcessPara.ReturnConductSetValue2'),
'ACSB_13' : tagDetails('Dosing RetSetValue for Caustic Circulation', 'INT', 'SP_13', 'Program:CktB.CausticCirProcessPara.DosingResetValue'),
'ACSB_14' : tagDetails('Hold SetValue for Caustic Circulation', 'INT', 'SP_14', 'Program:CktB.CausticCirProcessPara.HoldSetValue'),
'ACSB_15' : tagDetails('Tank Temp Set Value for Intermediate', 'INT', 'SP_15', 'Program:CktB.IntermediateRinseProcessPara.TankTempSetValue'),
'ACSB_16' : tagDetails('Flow Rate  for Intermediate', 'INT', 'SP_16', 'Program:CktB.IntermediateRinseProcessPara.FlowSetValue'),
'ACSB_17' : tagDetails('Return Temp for Intermediate', 'INT', 'SP_17', 'Program:CktB.IntermediateRinseProcessPara.ReturnTempSetValue'),
'ACSB_18' : tagDetails('Return Conductivity 1 for Intermediate', 'INT', 'SP_18', 'Program:CktB.IntermediateRinseProcessPara.ReturnConductSetValue1'),
'ACSB_19' : tagDetails('Return Conductivity 2  for Intermediate', 'INT', 'SP_19', 'Program:CktB.IntermediateRinseProcessPara.ReturnConductSetValue2'),
'ACSB_20' : tagDetails('Return Conductivity 3  for Intermediate', 'INT', 'SP_20', 'Program:CktB.IntermediateRinseProcessPara.ReturnConductSetValue3'),
'ACSB_21' : tagDetails('Tank Temp for Acid Circulation', 'INT', 'SP_21', 'Program:CktB.AcidTankProcessPara.TankTempSetValue'),
'ACSB_22' : tagDetails('Flow Rate for Acid Circulation', 'INT', 'SP_22', 'Program:CktB.AcidTankProcessPara.FlowSetValue'),
'ACSB_23' : tagDetails('Return Temp for Acid Circulation', 'INT', 'SP_23', 'Program:CktB.AcidTankProcessPara.ReturnTempSetValue'),
'ACSB_24' : tagDetails('Dosing SetValue for Acid Circulation', 'INT', 'SP_24', 'Program:CktB.AcidTankProcessPara.DosingSetValue'),
'ACSB_25' : tagDetails('Return Conductivity 1 for Acid Circulation', 'INT', 'SP_25', 'Program:CktB.AcidTankProcessPara.ReturnConductSetValue1'),
'ACSB_26' : tagDetails('Return Conductivity 2 for Acid Circulation', 'INT', 'SP_26', 'Program:CktB.AcidTankProcessPara.ReturnConductSetValue2'),
'ACSB_27' : tagDetails('Dosing RetSetValue for Acid Circulation', 'INT', 'SP_27', 'Program:CktB.AcidTankProcessPara.DosingResetValue'),
'ACSB_28' : tagDetails('Hold SetValue for Acid Circulation', 'INT', 'SP_28', 'Program:CktB.AcidTankProcessPara.HoldSetValue'),
'ACTB_1' : tagDetails('PreRinse Cycle Time', 'Time', 'T_1', 'Program:CktB.PreRinseTimerPara.PreRinseCycleTime'),
'ACTB_2' : tagDetails('Return Pump On Time For PreRinse', 'Time', 'T_2', 'Program:CktB.PreRinseTimerPara.ReturnPumpOnTime'),
'ACTB_3' : tagDetails('Supply Pump On Time For PreRinse', 'Time', 'T_3', 'Program:CktB.PreRinseTimerPara.SupplyPumpOnTime'),
'ACTB_4' : tagDetails('Intermediate stop time For PreRinse', 'Time', 'T_4', 'Program:CktB.PreRinseTimerPara.InterMediateStopTime'),
'ACTB_5' : tagDetails('Pushing Time For PreRinse', 'Time', 'T_5', 'Program:CktB.PreRinseTimerPara.PushingTime'),
'ACTB_6' : tagDetails('Drain Time For PreRinse', 'Time', 'T_6', 'Program:CktB.PreRinseTimerPara.DrainTime'),
'ACTB_7' : tagDetails('Hot Water Circulation Time Hot water Circulation', 'Time', 'T_7', 'Program:CktB.HWCirTimePara.HwCircCycleTime'),
'ACTB_8' : tagDetails('Return Pump On Time Hot water Circulation', 'Time', 'T_8', 'Program:CktB.HWCirTimePara.ReturnPumpOnTime'),
'ACTB_9' : tagDetails('Supply Pump On Time Hot water Circulation', 'Time', 'T_9', 'Program:CktB.HWCirTimePara.SupplyPumpOnTime'),
'ACTB_10' : tagDetails('Intermediate stop time Hot water Circulation', 'Time', 'T_10', 'Program:CktB.HWCirTimePara.InterMediateStopTime'),
'ACTB_11' : tagDetails('Pushing Time Hot water Circulation', 'Time', 'T_11', 'Program:CktB.HWCirTimePara.PushingTime'),
'ACTB_12' : tagDetails('Return Pump On Time for Caustic Circulation', 'Time', 'T_12', 'Program:CktB.CausticCirTimerPara.ReturnPumpOnTime'),
'ACTB_13' : tagDetails('Supply Pump On Time for Caustic Circulation', 'Time', 'T_13', 'Program:CktB.CausticCirTimerPara.SupplyPumpOnTime'),
'ACTB_14' : tagDetails('Intermediate stop time for Caustic Circulation', 'Time', 'T_14', 'Program:CktB.CausticCirTimerPara.InterMediateStopTime'),
'ACTB_15' : tagDetails('Pushing Time for Caustic Circulation', 'Time', 'T_15', 'Program:CktB.CausticCirTimerPara.PushingTime'),
'ACTB_16' : tagDetails('Return Pump Off Time  for Caustic Circulation', 'Time', 'T_16', 'Program:CktB.CausticCirTimerPara.RPumpOffTime'),
'ACTB_17' : tagDetails('Drain Time for Caustic Circulation', 'Time', 'T_17', 'Program:CktB.CausticCirTimerPara.DrainTime'),
'ACTB_18' : tagDetails('Caustic Cycle Time for Caustic Circulation', 'Time', 'T_18', 'Program:CktB.CausticCirTimerPara.LyeCircCycleTime'),
'ACTB_19' : tagDetails('InterMediate CIP Time for Intermediate', 'Time', 'T_19', 'Program:CktB.IntermediateRinseTimerPara.InterMediateCycleTime'),
'ACTB_20' : tagDetails('Return Pump On Time for Intermediate', 'Time', 'T_20', 'Program:CktB.IntermediateRinseTimerPara.ReturnPumpOnTime'),
'ACTB_21' : tagDetails('Supply Pump On Time for Intermediate', 'Time', 'T_21', 'Program:CktB.IntermediateRinseTimerPara.SupplyPumpOnTime'),
'ACTB_22' : tagDetails('Intermediate stop time for Intermediate', 'Time', 'T_22', 'Program:CktB.IntermediateRinseTimerPara.InterMediateStopTime'),
'ACTB_23' : tagDetails('Pushing Time for Intermediate', 'Time', 'T_23', 'Program:CktB.IntermediateRinseTimerPara.PushingTime'),
'ACTB_24' : tagDetails('Drain Time for Intermediate', 'Time', 'T_24', 'Program:CktB.IntermediateRinseTimerPara.DrainTime'),
'ACTB_25' : tagDetails('Return Pump On Time for Acid Circulation', 'Time', 'T_25', 'Program:CktB.AcidTankTimerPara.ReturnPumpOnTime'),
'ACTB_26' : tagDetails('Supply Pump On Time for Acid Circulation', 'Time', 'T_26', 'Program:CktB.AcidTankTimerPara.SupplyPumpOnTime'),
'ACTB_27' : tagDetails('Intermediate stop time for Acid Circulation', 'Time', 'T_27', 'Program:CktB.AcidTankTimerPara.InterMediateStopTime'),
'ACTB_28' : tagDetails('Pushing Time for Acid Circulation', 'Time', 'T_28', 'Program:CktB.AcidTankTimerPara.PushingTime'),
'ACTB_29' : tagDetails('Return Pump Off Time for Acid Circulation', 'Time', 'T_29', 'Program:CktB.AcidTankTimerPara.RPumpOffTime'),
'ACTB_30' : tagDetails('Drain Time for Acid Circulation', 'Time', 'T_30', 'Program:CktB.AcidTankTimerPara.DrainTime'),
'ACTB_31' : tagDetails('Acid Cycle Time for Acid Circulation', 'Time', 'T_31', 'Program:CktB.AcidTankTimerPara.AcidCircCycleTime'),
'ACTB_32' : tagDetails('Return Pump On TimeFlow for Hot Water Circulation', 'Time', 'T_32', 'Program:CktA.HWCirTimePara.ReturnPumpOnTimeFlow'),
'ACTB_33' : tagDetails('Return Pump On TimeFlow for Prerinse Circulation', 'Time', 'T_33', 'Program:CktA.PreRinseTimerPara.ReturnPumpOnTimeFlow'),
'ACTB_34' : tagDetails('Return Pump On TimeFlow for Castic Circulation', 'Time', 'T_34', 'Program:CktA.CausticCirTimerPara.ReturnPumpOnTimeFlow'),
'ACTB_35' : tagDetails('Return Pump On TimeFlow for Intermediate Circulation', 'Time', 'T_35', 'Program:CktA.IntermediateRinseTimerPara.ReturnPumpOnTimeFlow'),

 }
