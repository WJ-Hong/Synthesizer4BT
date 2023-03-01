# --------------------------------------------------------------------
# source: IROS21 - Formalizing the Execution Context of Behavior Trees for Runtime Verification of Deliberative Policies
# description: save victim and put out a fire
# --------------------------------------------------------------------
# expected BT: ( ? ( -> Con0 ( ? Con1 Act0 ) ) ( ? Con2 Act1 ) )
# synthesized BT: ( ? ( -> Con0 Act0 ) Act1 )
# --------------------------------------------------------------------
# timecost:  173.69546008110046
# verification time ratio:  1.2722 (220.98/173.7)
# storing ratio:  0.879 (437[Verify]+544[NoVerify]/1116)
# pruning ratio:  0.121 (35[Com-V]+44[Incom-V]+56[Incom-S]/1116)
# pruning ratio in verification:  0.1531
# pruning number (structure):  351
# --------------------------------------------------------------------


actionMap = {'Act0': 'GotoRechargingPos',
             'Act1': 'GotoDestination'}
conditionMap = {'Con0': 'LowBattery',
                'Con1': 'AtRechargingPos',
                'Con2': 'AtDestinationPos'}
# semanticsRules Format: 'Act': [ [[PreCond1], [PostCond1]], [[PreCond2], [PostCond2]] ]
semanticsRules = {'Act0': [[['Con0', '!Con1'], ['!Con0', 'Con1', '!Con2']]],
                  'Act1': [[['!Con0', '!Con2'], ['!Con1', 'Con2']]]}
# initializationObservable Format: [[setTrue], [setFalse]]
initializationObservable = [[], ['Con1', 'Con2']]
ltlDeclaration = 'ltlDeclaration = Act0_s -> Act1_s -> Con0_s -> Con0_f -> Con1_s -> Con1_f -> Con2_s -> Con2_f -> Skip;'
ltlProperty = ['F (Con0_s || Con0_f)',
               'F (Act0_s || Act1_s)',
               'G (Con0_s -> ((!Act1_s U Con0_f) || G !Act1_s))']
# ltlProperty = ['F (Con0_s || Con0_f) '
#                '&& G Con0_s -> F Act0_s '
#                '&& G Con0_f -> F Act1_s']