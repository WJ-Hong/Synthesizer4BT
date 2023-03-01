# --------------------------------------------------------------------
# description: infinitely visit A, B and C in order
# --------------------------------------------------------------------
# expected BT: ( -> ( ? Con1 Act1 ) ( ? Con2 Act2 ) ( ? Con3 Act3 ) )
# synthesized BT: ( -> ( -> Act1 Act2 ) Act3 )
# --------------------------------------------------------------------
# timecost:  182.22315382957458
# verification time ratio:  1.3146 (239.55/182.22)
# storing ratio:  0.914 (479[Verify]+563[NoVerify]/1140)
# pruning ratio:  0.086 (23[Com-V]+55[Incom-V]+20[Incom-S]/1140)
# pruning ratio in verification:  0.14
# pruning number (structure):  242
# --------------------------------------------------------------------

actionMap = {'Act1': 'GotoA',
             'Act2': 'GotoB',
             'Act3': 'GotoC'}
conditionMap = {'Con1': 'AtA',
                'Con2': 'AtB',
                'Con3': 'AtC'}
# semanticsRules Format: 'Act': [ [[PreCond1], [PostCond1]], [[PreCond2], [PostCond2]] ]
semanticsRules = {'Act1': [[[], ['Con1', '!Con2', '!Con3']]],
                  'Act2': [[[], ['!Con1', 'Con2', '!Con3']]],
                  'Act3': [[[], ['!Con1', '!Con2', 'Con3']]]
                  }
# initializationObservable Format: [[setTrue], [setFalse]]
initializationObservable = [[], ['Con1', 'Con2', 'Con3']]
ltlDeclaration = 'ltlDeclaration = Act1_s -> Act2_s -> Act3_s -> Skip;'
ltlProperty = ['G (F (Act1_s && (F (Act2_s && F Act3_s))))',
               '(!Act2_s && !Act3_s) U Act1_s',
               '!Act3_s U Act2_s']
# ltlProperty = ['G (F (Act1_s && (F (Act2_s && F Act3_s)))) '
#                '&& ((!Act2_s && !Act3_s) U Act1_s) '
#                '&& (!Act3_s U Act2_s)']