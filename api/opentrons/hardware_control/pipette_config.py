
def key_map_pipette_functions(model, ul, func):
    function_map = {
        'p10_single_v1': lambda: _p10_single_piecewise(ul, func),
        'p10_single_v1.3': lambda: _p10_single_piecewise(ul, func),
        'p10_multi_v1': lambda: _p10_multi_piecewise(ul, func),
        'p10_multi_v1.3': lambda: _p10_multi_piecewise(ul, func),
        'p50_single_v1': lambda:_p50_single_piecewise(ul, func),
        'p50_single_v1.3': lambda: _p50_single_piecewise(ul, func),
        'p50_multi_v1': lambda: _p50_multi_piecewise(ul, func),
        'p50_multi_v1.3': lambda: _p50_multi_piecewise(ul, func),
        'p300_single_v1': lambda: _p300_single_piecewise(ul, func),
        'p300_single_v1.3': lambda: _p300_single_piecewise(ul, func),
        'p300_multi_v1': lambda: _p300_multi_piecewise(ul, func),
        'p300_multi_v1.3': lambda: _p300_multi_piecewise(ul, func),
        'p1000_single_v1': lambda: _p1000_piecewise(ul, func),
        'p1000_single_v1.3': lambda: _p1000_piecewise(ul, func)
    }

    return function_map[model]


def _p10_single_piecewise(ul, func):
    # Piecewise function that calculates ul_per_mm for a p10 single
    # pipette model given a particular ul value
    if func == 'aspirate':
        if (ul > 0) and (ul < 1.8263):
            return -0.0958 * ul + 1.088
        elif (ul >= 1.8263) and (ul < 2.5222):
            return -0.104 * ul + 1.1031
        elif (ul >= 2.5222) and (ul < 3.2354):
            return -0.0447 * ul + 0.9536
        elif (ul >= 3.2354) and (ul < 3.9984):
            return -0.012 * ul + 0.8477
        elif (ul >= 3.9984) and (ul <= 12.5135):
            return -0.0021 * ul + 0.8079
    else:
        # Constant function for dispense
        return 0 * ul + 0.7945


def _p10_multi_piecewise(ul, func):
    # Piecewise function that calculates ul_per_mm for a p10 multi
    # pipette model given a particular ul value
    if func == 'aspirate':
        if (ul > 0) and (ul < 1.893415617):
            return -1.1069 * ul + 3.042593193
        elif (ul >= 1.893415617) and (ul < 2.497849452):
            return -0.1888 * ul + 1.30410391
        elif (ul >= 2.497849452) and (ul < 5.649462387):
            return -0.0081 * ul + 0.8528667891
        elif (ul >= 5.649462387) and (ul <= 12.74444519):
            return -0.0018 * ul + 0.8170558891
    else:
        # Constant function for dispense
        return 0 * ul + 0.8058688085


def _p50_single_piecewise(ul, func):
    # Piecewise function that calculates ul_per_mm for a p50 single
    # pipette model given a particular ul value
    if func == 'aspirate':
        if (ul > 0) and (ul < 11.79687499):
            return -0.0098 * ul + 3.064988953
        elif (ul >= 11.79687499) and (ul <= 50):
            return -0.0004 * ul + 2.954068131
    else:
        return 0 * ul + 2.931601299


def _p50_multi_piecewise(ul, func):
    # Piecewise function that calculates ul_per_mm for a p50 multi
    # pipette model given a particular ul value
    if func == 'aspirate':
        if (ul > 0) and (ul < 12.29687531):
            return -0.0049 * ul + 3.134703694
        elif (ul >= 12.29687531) and (ul <= 50):
            return -0.0002 * ul + 3.077116024
    else:
        # Constant function for dispense
        return 0 * ul + 3.06368702


def _p300_single_piecewise(ul, func):
    # Piecewise function that calculates ul_per_mm for a p300 single
    # pipette model given a particular ul value
    if func == 'aspirate':
        if (ul > 0) and (ul < 36.19844973):
            return 0.043 * ul + 16.548
        elif (ul >= 36.19844973) and (ul < 54.98518519):
            return 0.012 * ul + 17.658
        elif (ul >= 54.98518519) and (ul < 73.90077516):
            return 0.008 * ul + 17.902
        elif (ul >= 73.90077516) and (ul < 111.8437953):
            return 0.004 * ul + 18.153
        elif (ul >= 111.8437953) and (ul <= 302.3895337):
            return 0.001 * ul + 18.23
    else:
        # Constant function for dispense
        return 0 * ul + 18.83156277


def _p300_multi_piecewise(ul, func):
    # Piecewise function that calculates ul_per_mm for a p300 multi
    # pipette model given a particular ul value
    if func == 'aspirate':
        if (ul > 0) and (ul < 57.25698968):
            return 0.017 * ul + 18.132
        elif (ul >= 57.25698968) and (ul <= 309.2612689):
            return 0.001 * ul + 19.03
    else:
        # Constant function for dispense
        return 0 * ul + 19.29389273


def _p1000_piecewise(ul, func):
    if func == 'aspirate':
        return 65
    else:
        return 65
