from project.supply.food import Food
from project.supply.drink import Drink
from project.player import Player

class Controller:
    def __init__(self):
        self.players = [] # players as obj.
        self.supplies = [] # supplies as obj.

    def add_player(self, *players):
        for player in players:
            if player not in self.players:
                self.players.append(player)

        player_names = [p.name for p in self.players]
        return f"Successfully added: {', '.join(player_names)}"


    def add_supply(self, *supplies):
        for sup in supplies:
            if sup not in self.supplies:
                self.supplies.append(sup)

    def sustain(self, player_name: str, sustenance_type: str):
            player = [p for p in self.players if p.name == player_name]
            if not player:
                return

            if sustenance_type == "Drink":
                drinks = [d for d in self.supplies if d.__class__.__name__ == "Drink"]
                if not drinks:
                    raise Exception("There are no drink supplies left!")
                else:

                    supply = drinks[-1]
                    energy_from_supply = supply.energy

                    if player[0]:
                        player = player[0]
                        if player.stamina == 100:
                            return f"{player_name} have enough stamina."

                        elif player.stamina < 100:
                            if player.stamina + energy_from_supply > 100:
                                player.stamina = 100
                            else:
                                player.stamina += energy_from_supply

                            self.supplies.remove(supply)
                            return f"{player_name} sustained successfully with {supply.name}."

                if sustenance_type == "Food":
                    food = [f for f in self.supplies if f.__class__.__name__ == "Food"]
                    if not food:
                        raise Exception("There are no food supplies left!")
                    else:

                        supply = food[-1]
                        energy_from_supply = supply.energy

                        if player[0]:
                            player = player[0]
                            if player.stamina == 100:
                                return f"{player_name} have enough stamina."

                            elif player.stamina < 100:
                                if player.stamina + energy_from_supply > 100:
                                    player.stamina = 100
                                else:
                                    player.stamina += energy_from_supply

                                self.supplies.remove(supply)
                                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = [p for p in self.players if p.name == first_player_name][0]
        player2 = [p for p in self.players if p.name == second_player_name][0]

        if player1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif player2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."
        elif player1.stamina == 0 and player2.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                    f"Player {second_player_name} does not have enough stamina."


        if player1.stamina > player2.stamina:
            stamina_to_reduce = player2.stamina / 2
            player1.stamina -= stamina_to_reduce
            if player1.stamina <= 0:
                winner = player2
                return f"Winner: {winner}"
            else:
                stamina_to_reduce = player1.stamina / 2
                player2.stamina -= stamina_to_reduce
                if player2.stamina <= 0:
                    winner = player1
                    return f"Winner: {winner}"

    def next_day(self):
        pass

    def __str__(self):
        info = []
        for p in self.players:
            info.append(p.__str__())
        for s in self.supplies:
            info.append(s.details())
        result = "\n".join(info)
        return result



