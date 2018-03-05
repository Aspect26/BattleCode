import battlecode as bc

class KarboniteDepositInfo:

    def __init__(self, location, initial_karbonite):
        self.location = location
        self.initial_karbonite = initial_karbonite
        self.observed_karbonite = initial_karbonite
        self.observed_owned_by_enemy = False
        self.being_harvested = False


class KarboniteDeposits:

    _deposits: [KarboniteDepositInfo] = []

    def __init__(self, game_controller):
        planet_map = game_controller.starting_map(bc.Planet.Earth)
        center_location = bc.MapLocation(bc.Planet.Earth, int(round(planet_map.width / 2)), int(round(planet_map.height / 2)))
        all_map_locations = game_controller.all_locations_within(center_location, max(planet_map.width ** 2, planet_map.height ** 2))

        for map_location in all_map_locations:
            location_karbonite_count = planet_map.initial_karbonite_at(map_location)
            if location_karbonite_count > 0:
                self._deposits.append(KarboniteDepositInfo(map_location, location_karbonite_count))

    def get_nearest(self, location) -> KarboniteDepositInfo:
        # TODO: use pathfinder here (iterate over all deposits, get nearest paths to them and choose the one with minimal nearest path
        # TODO: but watch out for owned by enemy and also those that are running out!
        # TODO: watch out also to not len all workers go to the same deposits!
        min_distance = 100000
        nearest_deposit = self._deposits[0]
        deposits_count = 0
        for deposit in self._deposits:
            if not deposit.observed_owned_by_enemy and deposit.observed_karbonite > 0 and not deposit.being_harvested:
                deposits_count += 1
                deposit_distance = abs(deposit.location.x - location.x) + abs(deposit.location.y - location.y)
                if deposit_distance < min_distance:
                    nearest_deposit = deposit
                    min_distance = deposit_distance

        print("DC: " + str(deposits_count))
        return nearest_deposit

    def _print_deposits_info(self):
        for info in self._deposits:
            print("K Deposit: " + str(info.location.x) + ":" + str(info.location.y) + " - " + str(info.initial_karbonite) + ", " + str(info.observed_owned_by_enemy))



