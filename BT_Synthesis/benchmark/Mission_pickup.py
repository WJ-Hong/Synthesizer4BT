# --------------------------------------------------------------------
# description:  pick up a cube from A and place it on B once
# --------------------------------------------------------------------
# expected BT: ( -> ( ? Con3 ( -> ( ? Con1 Act1 ) Act3 ) ) ( ? Con4 ( -> ( ? Con2 Act2 ) Act4 ) ) )
# synthesized BT: ( ? Act4 ( -> Act1 ( -> Act3 Act2 ) ) )
# --------------------------------------------------------------------
# timecost:  1101.5370717048645
# verification time ratio:  1.3345 (1469.99/1101.54)
# storing ratio:  0.929 (3114[Verify]+3639[NoVerify]/7269)
# pruning ratio:  0.071 (74[Com-V]+239[Incom-V]+203[Incom-S]/7269)
# pruning ratio in verification:  0.0913
# pruning number (structure):  1719
# --------------------------------------------------------------------

actionMap = {'Act1': 'GotoA',
             'Act2': 'GotoB',
             'Act3': 'Pickup',
             'Act4': 'Place'}
conditionMap = {'Con1': 'AtA',
                'Con2': 'AtB',
                'Con3': 'Picked',
                'Con4': 'Placed'}
# semanticsRules Format: 'Act': [ [[PreCond1], [PostCond1]], [[PreCond2], [PostCond2]] ]
semanticsRules = {'Act1': [[[], ['Con1', '!Con2']]],
                  'Act2': [[[], ['!Con1', 'Con2']]],
                  'Act3': [[['Con1', '!Con3'], ['Con3']]],
                  'Act4': [[['Con2', 'Con3'], ['!Con3', 'Con4']]]
                  }
# initializationObservable Format: [[setTrue], [setFalse]]
initializationObservable = [[], ['Con1', 'Con2', 'Con3', 'Con4']]
ltlDeclaration = 'ltlDeclaration = Act3_s -> Act4_s -> Skip;'
ltlProperty = ['F Act3_s',
               'F Act4_s']
# ltlProperty = ['F Act3_s '
#                '&& F Act4_s']