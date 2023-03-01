# --------------------------------------------------------------------
# description: periodically do taskA (if Alarm) or do taskB (if no alarm)
# --------------------------------------------------------------------
# expected BT: ( ? ( -> Con5 ( ? Con3 ( -> ( ? Con1 Act1 ) Act3 ) ) )
#                  ( ? Con4 ( -> ( ? Con2 Act2 ) Act4 ) )
#              )
# synthesized BT: ( ? ( -> ( -> Act2 ( -> Con5 Act1 ) ) Act3 ) Act4 )
# --------------------------------------------------------------------
# timecost:  2534.806505203247
# verification time ratio:  1.2958 (3284.66/2534.81)
# storing ratio:  0.9476 (6825[Verify]+7561[NoVerify]/15181)
# pruning ratio:  0.0524 (116[Com-V]+237[Incom-V]+442[Incom-S]/15181)
# pruning ratio in verification:  0.0492
# pruning number (structure):  3905
# --------------------------------------------------------------------

actionMap = {'Act1': 'GotoA',
             'Act2': 'GotoB',
             'Act3': 'DoTaskA',
             'Act4': 'DoTaskB'}
conditionMap = {'Con1': 'AtA',
                'Con2': 'AtB',
                'Con3': 'TaskFinishedA',
                'Con4': 'TaskFinishedB',
                'Con5': 'Alarm'}
# semanticsRules Format: 'Act': [ [[PreCond1], [PostCond1]], [[PreCond2], [PostCond2]] ]
semanticsRules = {'Act1': [[[], ['Con1', '!Con2']]],
                  'Act2': [[[], ['!Con1', 'Con2']]],
                  'Act3': [[['Con1', '!Con3', 'Con5'], ['Con3']]],
                  'Act4': [[['Con2', '!Con4', '!Con5'], ['Con4']]]
                 }
# initializationObservable Format: [[setTrue], [setFalse]]
initializationObservable = [[], ['Con1', 'Con2', 'Con3', 'Con4']]
ltlDeclaration = 'ltlDeclaration = Act1_s -> Act2_s -> Act3_s -> Act4_s -> Con5_s -> Con5_f -> Skip;'
ltlProperty = ['F (Act3_s || Act4_s)',
               'F (Con5_s || Con5_f)',
               'G (Con5_s -> ((!Act4_s U Con5_f) || G !Act4_s))',
               'G (Con5_f -> ((!Act3_s U Con5_s) || G !Act3_s))']
# ltlProperty = ['F (Act3_s || Act4_s) '
#                '&& F (Con5_s || Con5_f) '
#                '&& G (Con5_s -> ((!Act4_s U Con5_f) || G !Act4_s)) '
#                '&& G (Con5_f -> ((!Act3_s U Con5_s) || G !Act3_s))']