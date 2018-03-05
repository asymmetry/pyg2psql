#!/usr/bin/env python

import datetime
from os.path import join, dirname, realpath
import sqlite3
import time

_con = sqlite3.connect(join(dirname(realpath(__file__)), 'g2p.db'))
_cur = _con.cursor()

def _search(field, run):
    table = 'AnaInfoR' if run > 20000 else 'AnaInfoL'
    _cur.execute('Select {} from {} where RunNumber = {}'.format(field, table, run))    # danger!!!
    r = _cur.fetchone()

    result = None
    if r == None:
        result = None
    else:
        result = r[0]
    return result

def _string_result(field, run):
    result = _search(field, run)
    try:
        result = str(result)
    except (TypeError, ValueError):
        result = 'NULL'
    return result  

def _int_result(field, run):
    result = _search(field, run)
    try:
        result = int(result)
    except (TypeError, ValueError):
        result = -999
    return result

def _float_result(field, run):
    result = _search(field, run)
    try:
        result = float(result)
    except (TypeError, ValueError):
        result = -999.0
    return result

def _time_result(field, run):
    result = _search(field, run)
    try:
        result = int(time.mktime(datetime.datetime.strptime(result, '%Y-%m-%d %H:%M:%S').timetuple()))
    except (TypeError, ValueError):
        result = -999
    return result

def get_my_run_quality(run):
    return _int_result('RunQuality', run)

def get_my_run_status(run):
    return _int_result('RunStatus', run)

def get_my_septa_status(run):
    return _int_result('SeptaStatus', run)

def get_my_hwp_status(run):
    return _int_result('Ihwp', run)

def get_my_hwpSTD(run):
    return _float_result('IhwpSTD', run)

def get_my_ps1(run):
    return _float_result('ps1', run)

def get_my_ps2(run):
    return _float_result('ps2', run)

def get_my_ps3(run):
    return _float_result('ps3', run)

def get_my_ps4(run):
    return _float_result('ps4', run)

def get_my_ps7(run):
    return _float_result('ps7', run)

def get_my_ps8(run):
    return _float_result('ps8', run)

def get_my_target_encoder(run):
    return _float_result('TargetEncoder', run)

def get_my_target_std(run):
    return _float_result('TargetSTD', run)

def get_my_Q1p(run):
    return _float_result('Q1p', run)

def get_my_Q1pSTD(run):
    return _float_result('Q1pSTD', run)

def get_my_Q2p(run):
    return _float_result('Q2p', run)

def get_my_Q2pSTD(run):
    return _float_result('Q2pSTD', run)

def get_my_Q3p(run):
    return _float_result('Q3p', run)

def get_my_Q3pSTD(run):
    return _float_result('Q3pSTD', run)

def get_my_D1p(run):
    return _float_result('D1p', run)

def get_my_D1pSTD(run):
    return _float_result('D1pSTD', run)

def get_my_septa_current(run):
    return _float_result('SeptaI', run)

def get_my_septa_currentSTD(run):
    return _float_result('SeptaSTD', run)

def get_my_beam_energy(run):
    return _float_result('Energy', run)

def get_my_beam_energySTD(run):
    return _float_result('EnergySTD', run)

def get_my_trigger_efficiency(run):
    return _float_result('TEff', run)

def get_my_deadtime(run):
    return _float_result('Deadtime', run)

def get_my_cercut(run):
    return _float_result('CerCut', run)

def get_my_pr1cut(run):
    return _float_result('PR1Cut', run)

def get_my_sumcut(run):
    return _float_result('SumCut', run)

def get_my_beampol(run):
    return _float_result('BeamPol', run)

def get_my_beampolstat(run):
    return _float_result('BeamPolStat', run)

def get_my_beampolsys(run):
    return _float_result('BeamPolSys', run)

def get_my_bleedthrough(run):
    return _float_result('Bleedthrough', run)

def get_my_onetrackeff(run):
    return _float_result('OneTrackEff', run)

def get_my_alltrackeff(run):
    return _float_result('AllTrackEff', run)

def get_my_alltrackeffl(run):
    return _float_result('AllTrackEffLow', run)

def get_my_alltrackeffh(run):
    return _float_result('AllTrackEffHigh', run)

def get_my_targetpol(run):
    return _float_result('TargetPol', run)

def get_my_targetpole(run):
    return _float_result('TargetPolError', run)

def get_my_targetpolstat(run):
    return _float_result('TargetPolStat', run)

def get_my_targetpolsys(run):
    return _float_result('TargetPolSys', run)

def get_my_dtplus(run):
    return _float_result('DTPlus', run)

def get_my_dtminus(run):
    return _float_result('DTMinus', run)

def get_my_ltasym(run):
    return _float_result('LTAsym', run)

def get_my_charge_asym(run):
    return _float_result('ChargeAsym', run)

def get_my_qplus(run):
    return _float_result('QPlus', run)

def get_my_qminus(run):
    return _float_result('QMinus', run)

def get_my_qtotal(run):
    return _float_result('QTotal', run)

def get_my_target_field(run):
    return _float_result('TargetField', run)

def get_my_target_orientation(run):
    return _int_result('TargetOrientation', run)

def get_my_materialID(run):
    return _int_result('MaterialID', run)

def get_my_expert_comment(run):
    return _string_result('ExpertC', run)

def get_my_target_cup(run):
    return _string_result('TargetCup', run)

def get_my_run_start_time(run):
    return _time_result('RunStartTime', run)

def get_my_entry_time(run):
    return _time_result('EntryTime', run)

def get_my_run_stop_time(run):
    return _time_result('RunStopTime', run)

def get_my_cer_eff(run):
    return _float_result('CerDetEff', run)

def get_my_pr_eff(run):
    return _float_result('PRDetEff', run)

def get_my_current(run):
    return _float_result('Current', run)

def get_my_thCutMin(run):
    return _float_result('thCutMin', run)

def get_my_thCutMax(run):
    return _float_result('thCutMax', run)

def get_my_phCutMin(run):
    return _float_result('phCutMin', run)

def get_my_phCutMax(run):
    return _float_result('phCutMax', run)

def get_my_xBeamCut(run):
    return _float_result('xBeam', run)

def get_my_yBeamCut(run):
    return _float_result('yBeam', run)

def get_my_rBeamCut(run):
    return _float_result('rBeam', run)

def get_my_xSRCut(run):
    return _float_result('xSR', run)

def get_my_ySRCut(run):
    return _float_result('ySR', run)

def get_my_rSRCut(run):
    return _float_result('rSR', run)

if __name__ == '__main__':
    print(get_my_beam_energy(5585))
