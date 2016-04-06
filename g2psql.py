#!/usr/bin/env python

import time, datetime, sqlite3
from os.path import join, dirname, realpath

def _search(field, run):
    con = sqlite3.connect(join(dirname(realpath(__file__)), 'g2p.db'))
    cur = con.cursor()

    table = None
    if run > 20000:
        table = 'AnaInfoR'
    else:
        table = 'AnaInfoL'

    cur.execute('Select {} from {} where RunNumber = {}'.format(field, table, run)) # danger!!!
    result, = cur.fetchone()

    if isinstance(result, unicode):
        if result == None:
            result = 'NULL'
        else:
            try:
                result = int(time.mktime(datetime.datetime.strptime(result, "%Y-%m-%d %H:%M:%S").timetuple()))
            except ValueError:
                pass
    elif isinstance(result, int):
        if result == None:
            result = -999
    elif isinstance(result, float):
        if result == None:
            result = -999.0

    return result

def get_my_run_quality(run):
    return _search('RunQuality', run)

def get_my_run_status(run):
    return _search('RunStatus', run)

def get_my_septa_status(run):
    return _search('SeptaStatus', run)

def get_my_hwp_status(run):
    return _search('Ihwp', run)

def get_my_hwpSTD(run):
    return _search('IhwpSTD', run)

def get_my_ps1(run):
    return _search('ps1', run)

def get_my_ps2(run):
    return _search('ps2', run)

def get_my_ps3(run):
    return _search('ps3', run)

def get_my_ps4(run):
    return _search('ps4', run)

def get_my_ps7(run):
    return _search('ps7', run)

def get_my_ps8(run):
    return _search('ps8', run)

def get_my_target_encoder(run):
    return _search('TargetEncoder', run)

def get_my_target_std(run):
    return _search('TargetSTD', run)

def get_my_Q1p(run):
    return _search('Q1p', run)

def get_my_Q1pSTD(run):
    return _search('Q1pSTD', run)

def get_my_Q2p(run):
    return _search('Q2p', run)

def get_my_Q2pSTD(run):
    return _search('Q2pSTD', run)

def get_my_Q3p(run):
    return _search('Q3p', run)

def get_my_Q3pSTD(run):
    return _search('Q3pSTD', run)

def get_my_D1p(run):
    return _search('D1p', run)

def get_my_D1pSTD(run):
    return _search('D1pSTD', run)

def get_my_septa_current(run):
    return _search('SeptaI', run)

def get_my_septa_currentSTD(run):
    return _search('SeptaSTD', run)

def get_my_beam_energy(run):
    return _search('Energy', run)

def get_my_beam_energySTD(run):
    return _search('EnergySTD', run)

def get_my_trigger_efficiency(run):
    return _search('TEff', run)

def get_my_deadtime(run):
    return _search('Deadtime', run)

def get_my_cercut(run):
    return _search('CerCut', run)

def get_my_pr1cut(run):
    return _search('PR1Cut', run)

def get_my_sumcut(run):
    return _search('SumCut', run)

def get_my_beampol(run):
    return _search('BeamPol', run)

def get_my_beampolstat(run):
    return _search('BeamPolStat', run)

def get_my_beampolsys(run):
    return _search('BeamPolSys', run)

def get_my_bleedthrough(run):
    return _search('Bleedthrough', run)

def get_my_onetrackeff(run):
    return _search('OneTrackEff', run)

def get_my_alltracakeff(run):
    return _search('AllTrackEff', run)

def get_my_alltrackeffl(run):
    return _search('AllTrackEffLow', run)

def get_my_alltrackeffh(run):
    return _search('AllTrackEffHigh', run)

def get_my_targetpol(run):
    return _search('TargetPol', run)

def get_my_targetpole(run):
    return _search('TargetPolError', run)

def get_my_dtplus(run):
    return _search('DTPlus', run)

def get_my_dtminus(run):
    return _search('DTMinus', run)

def get_my_ltasym(run):
    return _search('LTAsym', run)

def get_my_charge_asym(run):
    return _search('ChargeAsym', run)

def get_my_qplus(run):
    return _search('QPlus', run)

def get_my_qminus(run):
    return _search('QMinus', run)

def get_my_qtotal(run):
    return _search('QTotal', run)

def get_my_target_field(run):
    return _search('TargetField', run)

def get_my_target_orientation(run):
    return _search('TargetOrientation', run)

def get_my_materialID(run):
    return _search('MaterialID', run)

def get_my_expert_comment(run):
    return _search('ExpertC', run)

def get_my_target_cup(run):
    return _search('TargetCup', run)

def get_my_run_start_time(run):
    return _search('RunStartTime', run)

def get_my_entry_time(run):
    return _search('EntryTime', run)

def get_my_run_stop_time(run):
    return _search('RunStopTime', run)

def get_my_cer_eff(run):
    return _search('CerDetEff', run)

def get_my_pr_eff(run):
    return _search('PRDetEff', run)
