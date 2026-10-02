full_dot = '●'
empty_dot = '○'

def create_character(char_name, strength, intelligence, charisma):
    if not isinstance(char_name,str):
        return 'The character name should be a string'
    if char_name =='':
        return 'The character should have a name' 
    if len(char_name) > 10:
        return 'The character name is too long' 

    if " " in char_name:
        return 'The character name should not contain spaces'
    if not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
        return 'All stats should be integers'
    if strength<1 or intelligence <1 or charisma<1:
        return 'All stats should be no less than 1'  
    if strength>4 or intelligence>4 or charisma>4 :
        return 'All stats should be no more than 4' 
    if (strength+intelligence+charisma)!= 7 :
        return 'The character should start with 7 points' 
    
    strength_stat = 'STR '+ full_dot*strength+empty_dot*(10-strength)
    intelligence_stat = 'INT '+full_dot*intelligence+ empty_dot*(10-intelligence)
    charisma_stat = 'CHA '+ full_dot*charisma + empty_dot*(10-charisma)

    return f"{char_name}\n{strength_stat}\n{intelligence_stat}\n{charisma_stat}"



# Test:
print(create_character("ren", 4, 1, 2))
print()
print(create_character("seba", 1, 3, 3))
print()
print(create_character("", 4, 2, 1))       # Error: no name
print(create_character("abcdefghijklmnop", 4, 2, 1))  # Error: too long
print(create_character("ren", 5, 8, 1))    # Error: stat too high
print(create_character("ren", 2, 2, 2))    # Error: total not 7
