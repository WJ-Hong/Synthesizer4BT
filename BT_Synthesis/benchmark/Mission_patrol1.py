# --------------------------------------------------------------------
# description: infinitely visit A, B and C
# --------------------------------------------------------------------
# expected BT: ( -> ( ? Con1 Act1 ) ( ? Con2 Act2 ) ( ? Con3 Act3 ) )
# synthesized BT: ( -> ( -> Act3 Act2 ) Act1 )
# --------------------------------------------------------------------
# timecost:  123.77410221099854
# verification time ratio:  1.3683 (169.36/123.77)
# storing ratio:  0.9215 (327[Verify]+389[NoVerify]/777)
# pruning ratio:  0.0785 (19[Com-V]+38[Incom-V]+4[Incom-S]/777)
# pruning ratio in verification:  0.1484
# pruning number (structure):  162
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
ltlProperty = ['G F Act1_s',
               'G F Act2_s ',
               'G F Act3_s']
# ltlProperty = ['G F Act1_s '
#                '&& G F Act2_s '
#                '&& G F Act3_s']