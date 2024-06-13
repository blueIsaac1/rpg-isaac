import time
from random import randint
from loading import loading
tempo = True
done = False
rounds = 0

def tmp(tempo):    #temporazidor para cada round
    if tempo == True:
        time.sleep(3)
    elif tempo == False:
        time.sleep(0.1)

def reset_player():    #reset player
    player['hp'] = player['hp_max']

def reset_npc(npc):    #reset npc
    npc['hp'] = npc['hp_max']
    
def level_up():    #level up player
    if player['exp'] >= player['exp_max']:
        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] = player['exp_max'] * 1.2
        player['hp_max'] += 20
        player['damage'] += 5

lista_npcs = []    #lista para armazenar os npcs

player = {    #stats player
    "name": "Aventureiro",
    "level": 1,
    "exp": 0,
    "exp_max": 50,
    "hp": 100,
    "hp_max": 100,
    "damage": 20,
} 
def criar_npc(level):    #criar npcs uniratios
    novo_monstro = {
        "name": f"Monstro #{level}",
        "level": level,
        "damage": 5 * level,
        "hp": 50 * level,
        "hp_max": 50 * level,
        "exp_own": 10 * level
    }
    return novo_monstro


def gerar_npcs(n_npcs):    #gerar npcs
    for x in range(n_npcs):
        npc = criar_npc(x+1)
        lista_npcs.append(npc)


def exibir_npcs():    #exibição de todos os npcs gerados
    for dados in lista_npcs:
        print(f"NOME: {dados['name']} // LEVEL: {dados['level']} // DANO: {dados['damage']} // HP: {dados['hp']} // EXP: {dados['exp_own']}")

def exibir_player():    #exibiçaõ dos dados do Player
    nextup = player['exp_max'] - player['exp']
    print(f"NOME: {player['name']} // LEVEL: {player['level']} // HP: {player['hp']}/{player['hp_max']} // NEXT UPGRADE: {nextup} // DAMAGE: {player['damage']} ")
    print("-"*34)

def exibir_npc_singular(npc):    #exibir npc singular
    print(f"NOME: {npc['name']} // LEVEL: {npc['level']} // HP: {npc['hp']} // DAMAGE: {npc['damage']}")
    print("-"*34)


def iniciar_batalha(npc):    #while para a batalha
    global rounds
    while player['hp'] > 0 and npc['hp'] > 0:
        chance_critico()
        chance_critico2()
        atacar_npc(npc)
        ataque_player(npc)
        exibir_info_batalha(npc)
        tmp(tempo)
    
    if npc['hp'] > player['hp']:    #definição de quem ganhou a batalha e reset no npc
        print(f"NPC HP: {npc['hp']}")
        print("Npc Wins")
        exibir_npc_singular(npc)    
    elif player['hp'] > npc['hp']:    #distribuição de exp para o player e reset do player
        player['exp'] += npc['exp_own']
        print(f"{player['name']} Wins")
        exibir_player()
    
    level_up()
    reset_player()
    reset_npc(npc)
    rounds = 0


def atacar_npc(npc):    #condição de critico ou ataque normal do player
    if chance_critico() == True:
        critico(npc)
    else:
        npc['hp'] -= player['damage']


def ataque_player(npc):    #condição de critico ou ataque normal do npc
    if chance_critico2() == True:
        critico_npc(npc)
    else:
        player['hp'] -= npc['damage']

def critico(npc):    #dano com critico do player
    dano = player['damage'] * 2    
    npc['hp'] -= dano
    print(f"Critico do {player['name']}!")


def critico_npc(npc):    #dano do critico do npc
    dano = npc['damage'] * 1.3  
    player['hp'] -= dano
    print("Critico do Npc!")


def chance_critico():    #chance critico do player
    chance = randint(1, 100)
    if chance > 90:
        return True
    else:
        pass


def chance_critico2():    #chance de critico do npc
    chance = randint(1, 100)
    if chance > 90:
        return True
    else:
        pass

def exibir_info_batalha(npc):    #print dos dados
    global rounds
    rounds += 1
    print(f"ROUND: {rounds}")
    print(f"{player['name']} HP: {player['hp']} / {player['hp_max']}")
    print(f"NPC: {npc['name']}, NPC HP: {npc['hp']} / {npc['hp_max']}")
    print("-"*34)



gerar_npcs(5)
npc_selecionado = lista_npcs[2]    #npc selecionado para o combate   #lista_npcs[randint(0, len(lista_npcs)-1)] = caso voce queria gerar um npc aleatorio
loading(done)    #mensagem do loading
iniciar_batalha(npc_selecionado)    #aqui se inicia uma batalha individual, mas voce pode chamar mais de uma batalha repetindo essa função, uma ótima maneira de voce visualizar o distribuimento de exp e levelup.
exibir_player()
