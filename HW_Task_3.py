casino_blacklist = {'Wolfgan Amadeus Mozart', 'Peter Griffin', 'Govard Lovekraft'}
poker_blacklist = {'Wolfgan Amadeus Mozart', 'Matt Groening', 'Jack Bleck'}
alcohol_blacklist ={'Wolfgan Amadeus Mozart', 'Spartak Subota', 'Govard Lovekraft'}
half_bingo = casino_blacklist.intersection(poker_blacklist)
bingo = half_bingo.intersection(alcohol_blacklist)
print(bingo)

