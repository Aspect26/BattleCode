import battlecode as bc

_vision_range_map = {
    bc.UnitType.Worker: 50,
    bc.UnitType.Knight: 50,
    bc.UnitType.Ranger: 70,
    bc.UnitType.Mage: 30,
    bc.UnitType.Healer: 50
}


def get_unit_vision_range(unit_type: bc.UnitType) -> int:
    return _vision_range_map[unit_type]
