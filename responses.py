import random
import json

#npcs_map = 

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '&oi':
        return 'Oie!'
    
    if p_message == '&npc': #criar motivacoes
        #with open("npcs.json", "r") as openfile:
            #npcs = 
        return str(random.randint(1, 20))
    
    if p_message == '&help':
        return '`Mensagem`'
    
    return 'Deu ruim, nao entendi'