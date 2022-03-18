from pyperclip import copy, paste

def date(day: str, interval: str):
    begin_time, end_time = interval.split('-')
    return {
        'begin_time': '2022-02-' + day + 'T' + begin_time + ':00',
        'end_time': '2022-02-' + day + 'T' + end_time + ':00',
        'suffix': '2022_02_' + day + '_' + begin_time.replace(':', '_', -1) + '_00',
    }


def replace(s):
    s = s.replace(' *', '', -1)
    s = s.replace(' **', '', -1)
    s = s.replace('*', '', -1)
    s = s.replace('.', '', -1)
    s = s.replace('/', '', -1)
    s = s.replace('&', 'and', -1)
    s = s.replace('\r\n', ' ', -1)
    s = s.replace('-', '_', -1)
    s = s.replace(' + ', '_', -1)
    s = s.replace('+', '_', -1)
    s = s.replace('  ', ' ', -1)
    s = s.replace(' ', '_', -1)
    return s


def convert_to_clipboard():
    s = paste()
    copy(replace(s))


def convert(day: str, s: str):
    lines = s.split('\n')
    has_gold_medal = (lines[-2] == 'has_gold_medal')
    if has_gold_medal:
        lines = lines[:-2]
    type = ''
    times = []
    for line in lines:
        if line != '':
            if line[0] not in '0123456789':
                type += replace(line) + '_'
            else:
                times.append(date(day, line))
    type = type[:-1]
    result = ''
    for time in times:
        if has_gold_medal:
            result += f'''\n
    <!-- http://www.semanticweb.org/orangex4/ontologies/2022/2/beijing-2022-olympic-winter-games-schedule#{type}_{time['suffix']} -->

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/orangex4/ontologies/2022/2/beijing-2022-olympic-winter-games-schedule#{type}_{time['suffix']}">
        <rdf:type rdf:resource="http://www.semanticweb.org/orangex4/ontologies/2022/2/beijing-2022-olympic-winter-games-schedule#{type}"/>
        <begin_time rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">{time['begin_time']}</begin_time>
        <end_time rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">{time['end_time']}</end_time>
        <has_gold_medal rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</has_gold_medal>
    </owl:NamedIndividual>\n'''
        else:
            result += f'''\n
    <!-- http://www.semanticweb.org/orangex4/ontologies/2022/2/beijing-2022-olympic-winter-games-schedule#{type}_{time['suffix']} -->

    <owl:NamedIndividual rdf:about="http://www.semanticweb.org/orangex4/ontologies/2022/2/beijing-2022-olympic-winter-games-schedule#{type}_{time['suffix']}">
        <rdf:type rdf:resource="http://www.semanticweb.org/orangex4/ontologies/2022/2/beijing-2022-olympic-winter-games-schedule#{type}"/>
        <begin_time rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">{time['begin_time']}</begin_time>
        <end_time rdf:datatype="http://www.w3.org/2001/XMLSchema#dateTime">{time['end_time']}</end_time>
    </owl:NamedIndividual>\n'''
    return result


data = [
    {
        'day': '02',
        's_list': [
'''
Curling
Mixed Doubles
Round Robin
20:05-22:00
''',
        ]
    },
    {
        'day': '03',
        's_list': [
'''
Ice Hockey
W Preliminary Round
12:10-14:25
''',
'''
Ice Hockey
W Preliminary Round
12:10-14:25
16:40-18:55
21:10-23:25
''',
'''
Curling
Mixed Doubles
Round Robin
09:05-11:00
14:05-16:00
20:05-22:00
''',
'''
Freestyle Skiing
W Moguls
18:00-18:45
''',
'''
Freestyle Skiing
M Moguls
19:45-20:30
''',
        ]
    },
    {
    'day': '04',
    's_list': [
'''
Ice Hockey
W Preliminary Round
12:10-14:25
''',
'''
Ice Hockey
W Preliminary Round
12:10-14:25
''',
'''
Figure Skating
Team Event
M Short Program
Ice Dance Rhythm Dance
Pairs Short Program
09:30-14:55
''',
'''
Curling
Mixed Doubles
Round Robin
08:35-10:30
13:35-15:30
''',
        ]
    },
    {
    'day': '05',
    's_list': [
'''
Ice Hockey
W Preliminary Round
16:40-18:55
''',
'''
Ice Hockey
W Preliminary Round
12:10-14:25
16:40-18:55
21:10-23:25
''',
'''
Speed Skating
W 3000 m
16:30-18:05
has_gold_medal
''',
'''
Short Track
W 500 m Qual.
M 1000 m Qual.
Mixed Team Relay *
Quarter/Semi/Final
19:00-21:50
has_gold_medal
''',
'''
Curling
Mixed Doubles
Round Robin
09:05-11:00
14:05-16:00
20:05-22:00
''',
'''
Luge
M Heat 1 & 2
19:10-22:00
''',
'''
Ski Jumping
M Individual NH
Qual.
14:20-15:30
has_gold_medal
''',
'''
Ski Jumping
M Individual NH
Final
18:45-20:20
has_gold_medal
''',
'''
Cross-Country Skiing
W 7.5km + 7.5km
Skiathlon
15:45-16:45
has_gold_medal
''',
'''
Biathlon
Mixed Relay
17:00-18:30
has_gold_medal
''',
'''
Snowboard
W Snowboard Slopestyle
10:45-12:50
''',
'''
Freestyle Skiing
M Moguls
18:00-18:30
19:30-21:10
has_gold_medal
''',
        ]
    },
    {
    'day': '06',
    's_list': [
'''
Ice Hockey
W Preliminary Round
16:40-18:55
21:10-23:25
''',
'''
Speed Skating
M 5000 m
16:30-18:25
has_gold_medal
''',
'''
Figure Skating
Team Event
W Short Program
Pairs Free Skating
09:30-12:45
''',
'''
Curling
Mixed Doubles
Round Robin
09:05-11:00
14:05-16:00
20:05-22:00
''',
'''
Alpine Skiing
M Downhill
11:00-13:30
has_gold_medal
''',
'''
Luge
M Heat 3 & 4
19:30-22:10
has_gold_medal
''',
'''
Ski Jumping
M Individual NH
Final
19:00-20:45
has_gold_medal
''',
'''
Cross-Country Skiing
M 15km + 15km
Skiathlon
15:00-16:45
has_gold_medal
''',
'''
Snowboard
W Snowboard Slopestyle *
Final 09:30-11:00
M Snowboard Slopestyle
12:30-14:35
has_gold_medal
''',
'''
Freestyle Skiing
W Moguls
18:00-18:30
19:30-21:10
has_gold_medal
''',
        ]
    },
    {
    'day': '07',
    's_list': [
'''
Ice Hockey
W Preliminary Round
21:10-23:25
''',
'''
Ice Hockey
W Preliminary Round
12:10-14:25
16:40-18:55
21:10-23:25
''',
'''
Speed Skating
W 1500 m
16:30-18:00
has_gold_medal
''',
'''
Short Track **
W 500 m
Quarter/Semi/Final
M 1000 m
Quarter/Semi/Final
19:30-21:25
has_gold_medal
''',
'''
Figure Skating
Team Event
M Free Skating
Ice Dance Free Dance
W Free Skating
09:15-12:30
has_gold_medal
''',
'''
Curling
Mixed Doubles
09:05-11:00
20:05-22:00
''',
'''
Freestyle Skiing
W Freeski Big Air
Qual
09:30-11:45
''',
'''
Freestyle Skiing
M Freeski Big Air
Qual
13:30-15:45
''',
'''
Alpine Skiing
W Giant Slalom
Run 1 10:15-11:55
Run 2 13:45-15:50
has_gold_medal
''',
'''
Luge
W Heat 1 & 2
19:50-22:40
''',
'''
Ski Jumping
Mixed Team NH
19:45-21:45
has_gold_medal
''',
'''
Biathlon
W 15km Individual
17:00-18:50
has_gold_medal
''',
'''
Snowboard
M Snowboard Slopestyle
12:00-13:30
has_gold_medal
''',
        ]
    },
    {
    'day': '08',
    's_list': [
'''
Ice Hockey
M Preliminary Round
12:10-14:25
16:40-18:55
21:10-23:25
''',
'''
Ice Hockey
W Quarterfinals
12:10-14:25
16:40-18:55
''',
'''
Ice Hockey
M Preliminary Round
21:10-23:25
''',
'''
Speed Skating
W Team Pursuit Quarterfinals
M 500 m *
16:00-17:45
has_gold_medal
''',
'''
Figure Skating
Ice Dance
Rhythm Dance
19:00-22:40
''',
'''
Curling
M/W Round Robin
09:05-12:00
14:05-17:00
20:05-23:00
''',
'''
Skeleton
W Heat 3 & 4
20:20-22:50
has_gold_medal
''',
'''
Ski Jumping
M Individual LH
Final
19:00-20:45
has_gold_medal
''',
'''
Cross-Country Skiing
W 4x5km Relay
Classic/Free
15:30-17:00
has_gold_medal
''',
'''
Biathlon
M 10km Sprint
17:00-18:25
has_gold_medal
''',
'''
Snowboard
Mixed Team
Snowboard Cross
10:00-11:15
has_gold_medal
''',
        ]
    },
    {
    'day': '09',
    's_list': [
'''
Ice Hockey
M Preliminary Round
12:10-14:25
16:40-18:55
21:10-23:25
''',
'''
Ice Hockey
M Preliminary Round
21:10-23:25
''',
'''
Speed Skating
M Team Pursuit Quarterfinals
W 500 m *
21:00-22:50
has_gold_medal
''',
'''
Short Track **
M 500 m
Quarter/Semi/Final
W 3000 m Relay Final
19:00-20:40
has_gold_medal
''',
'''
Curling
M/W Round Robin
09:05-12:00
14:05-17:00
20:05-23:00
''',
'''
Alpine Skiing
M Giant Slalom
10:15-12:15
13:45-16:00
has_gold_medal
''',
'''
Bobsleigh
W Monobob Heat 1 & 2
09:30-11:45
''',
'''
Cross-Country Skiing
M 4x10km Relay
Classic/Free
15:00-16:55
has_gold_medal
''',
'''
Biathlon **
W 10km Pursuit
17:00-17:50
has_gold_medal
''',
'''
Biathlon **
M 12.5km Pursuit
18:45-19:35
has_gold_medal
''',
'''
Freestyle Skiing
W Freeski Slopestyle
10:00-12:00
''',
'''
Freestyle Skiing
W Aerials
19:00-20:15
''',
        ]
    },
    {
    'day': '10',
    's_list': [
'''
Ice Hockey
W Semifinals
12:10-14:25
21:10-23:25
''',
'''
Figure Skating
Ice Dance
Free Dance
09:15-12:50
has_gold_medal
''',
'''
Curling
M/W Round Robin
09:05-12:00
14:05-17:00
20:05-23:00
''',
'''
Snowboard
W Big Air
Qual
09:30-11:45
''',
'''
Snowboard
M Big Air
Qual
13:30-15:45
''',
'''
Bobsleigh
 W Monobob Heat 3 & 4
09:30-12:00
has_gold_medal
''',
'''
Bobsleigh
M Two-Man Heat 1 & 2
20:05-22:45
has_gold_medal
''',
'''
Ski Jumping
M Team LH
19:00-21:00
has_gold_medal
''',
'''
Freestyle Skiing
W Freeski Slopestyle *
09:30-11:00
has_gold_medal
''',
'''
Freestyle Skiing
M Freeski Slopestyle
12:30-14:35
has_gold_medal
''',
'''
Freestyle Skiing
W Aerials
19:00-20:30
has_gold_medal
''',
        ]
    },
    {
    'day': '11',
    's_list': [
'''
Ice Hockey
M Qualification Playoffs
12:10-14:25
16:40-18:55
21:10-23:25
''',
'''
Ice Hockey
M Qualification Playoffs
12:10-14:25
''',
'''
Speed Skating **
W/M Team Pursuit Finals
14:30-17:15
has_gold_medal
''',
'''
Figure Skating
W Short Program
18:00-22:25
''',
'''
Curling
M/W Round Robin
09:05-12:00
14:05-17:00
20:05-23:00
''',
'''
Snowboard **
W Big Air
Final
09:30-10:50
has_gold_medal
''',
'''
Snowboard **
M Big Air
Final
13:00-14:20
has_gold_medal
''',
'''
Alpine Skiing
W Downhill
11:00-13:10
has_gold_medal
''',
'''
Bobsleigh
M Two-Man Heat 3 & 4
20:15-22:45
has_gold_medal
''',
'''
Nordic Combined
M Individual LH
16:00-16:55
''',
'''
Nordic Combined
M Individual 10km
19:00-19:50
has_gold_medal
''',
'''
Biathlon
M 4x7.5km Relay
17:00-18:30
has_gold_medal
''',
'''
Freestyle Skiing
M Freeski Slopesyle
09:30-11:05
has_gold_medal
''',
'''
Freestyle Skiing
M Aerials
19:00-20:15
''',
        ]
    },
    {
    'day': '12',
    's_list': [
'''
Ice Hockey
M Quarterfinals
12:10-14:25
16:40-18:55
21:30-23:45
''',
'''
Ice Hockey
M Quarterfinals
14:00-16:15
''',
'''
Ice Hockey
W Bronze Medal
19:30-21:45
''',
'''
Short Track **
W 1500 m
Quarter/Semi/Final
M 5000m Relay Final
19:30-21:45
has_gold_medal
''',
'''
Curling
M/W Round Robin
09:05-12:00
14:05-17:00
20:05-23:00
''',
'''
Alpine Skiing
M Slalom
10:15-12:10
13:45-15:50
has_gold_medal
''',
'''
Cross-Country Skiing**
W/M Team Sprint Classic
Qual
17:00-18:30
has_gold_medal
''',
'''
Cross-Country Skiing**
W/M Team Sprint Classic
Final
19:00-20:20
has_gold_medal
''',
'''
Biathlon
W 4x6km Relay
15:45-17:15
has_gold_medal
''',
'''
Freestyle Skiing
M Aerials
19:00-20:30
has_gold_medal
''',
        ]
    },
    {
    'day': '13',
    's_list': [
'''
Ice Hockey
W Gold Medal
12:10-14:55
has_gold_medal
''',
'''
Speed Skating
W 1000 m
16:30-17:55
has_gold_medal
''',
'''
Figure Skating
W Free Skating
18:00-22:10
has_gold_medal
''',
'''
Curling
M/W Round Robin
09:05-12:00
14:05-17:00
20:05-23:00
''',
'''
Alpine Skiing
W Alpine Combined
Downhill segment
10:30-12:00
''',
'''
Alpine Skiing
W Alpine Combined
Slalom segment
14:00-15:30
has_gold_medal
''',
'''
Nordic Combined
M Team LH
16:00-16:40
''',
'''
Nordic Combined
M Team 4x5km
19:00-20:10
has_gold_medal
''',
'''
Freestyle Skiing
W Ski Cross
11:30-12:15
14:00-15:35
has_gold_medal
''',
'''
Freestyle Skiing
W Freeski Halfpipe
09:30-11:10
''',
'''
Freestyle Skiing
M Freeski Halfpipe
12:30-14:10
''',
        ]
    },
    {
    'day': '14',
    's_list': [
'''
Ice Hockey
M Semifinals
12:10-14:25
21:10-23:25
''',
'''
Speed Skating
M 1000 m
16:30-17:50
has_gold_medal
''',
'''
Figure Skating
Pairs
Short Program
18:30-21:45
''',
'''
Curling
M Bronze Medal
14:05-17:00
''',
'''
Curling
W Semifinal
20:05-23:00
''',
'''
Bobsleigh
Two-Woman Heat 1 & 2
20:00-22:15
''',
'''
Biathlon
M 15km Mass Start
17:00-17:55
has_gold_medal
''',
'''
Freestyle Skiing
M Ski Cross
11:45-12:30
14:00-15:35
has_gold_medal
''',
'''
Freestyle Skiing
W Freeski Halfpipe
09:30-11:00
has_gold_medal
''',
        ]
    },
    {
    'day': '15',
    's_list': [
'''
Ice Hockey
M Bronze Medal
21:10-23:40
''',
'''
Speed Skating **
M/W Mass Start
15:00-17:35
has_gold_medal
''',
'''
Figure Skating
Pairs
Free Skating
19:00-22:10
has_gold_medal
''',
'''
Curling
M Gold Medal
14:05-17:15
has_gold_medal
''',
'''
Curling
W Bronze Medal
20:05-23:00
has_gold_medal
''',
'''
Alpine Skiing
Team Event
11:00-13:10
has_gold_medal
''',
'''
Bobsleigh
Four-Man Heat 1 & 2
09:30-12:05
has_gold_medal
''',
'''
Bobsleigh
Two-Woman Heat 3 & 4*
20:00-22:30
has_gold_medal
''',
'''
Cross-Country Skiing
M 50km
Mass Start Free
14:00-16:55
has_gold_medal
''',
'''
Biathlon
W 12.5km Mass Start
17:00-17:55
has_gold_medal
''',
'''
Freestyle Skiing
M Freeski Halfpipe
09:30-11:00
has_gold_medal
''',
        ]
    },
    {
    'day': '16',
    's_list': [
'''
Ice Hockey
M Gold Medal
12:10-14:45
has_gold_medal
''',
'''
Figure Skating
Gala Exhibition
12:00-14:30
''',
'''
Curling
W Gold Medal
09:05-12:20
has_gold_medal
''',
'''
Bobsleigh
Four-Man Heat 3 & 4
09:30-12:25
has_gold_medal
''',
'''
Cross-Country Skiing
W 30km
Mass Start Free
14:30-16:40
has_gold_medal
''',
        ]
    },
]

result = ''
for item in data:
    for s in item['s_list']:
        result += convert(item['day'], s)

print(result)

