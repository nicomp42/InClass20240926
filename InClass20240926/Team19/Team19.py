# Team 19

def Team19():
    '''
    A funnction that lists AFC North and AFC East
    @return dict: list of football divisions
    members: Greyson and Henry
    '''
    
    Football_AFC_North = {"Cincinnati":"Bengals", "Baltimore":"Ravens", "Cleveland":"Browns", "Pittsburgh":"Steelers"}
    
    Football_AFC_East = {"New York":"Jets", "Miami":"Dolphins", "Buffalo":"Bills", "New England":"Patriots"}
    
    Football_AFC_North.update(Football_AFC_East)
    
    return Football_AFC_North
    

