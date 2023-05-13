from __future__ import annotations

import src.utils as utils
from src.resource import Resource, Resources


class Square:
    def __init__(self, coords: tuple[int, int]):
        self.coords = coords
        self.connections: list[Square] = []
        self.resources: dict[str, Resource] = {
            resource.name: resource.value.clone() for resource in Resources
        }

    def add_connection(self, square: Square) -> None:
        self.connections.append(square)

    def consume(self, consumption: dict[str, float]) -> dict[str, float]:
        consumed: dict[str, float] = {}

        for name, amount in consumption.items():
            consumed[name] = self.resources[name].consume(amount)

        return consumed

    def restore_renewal_rates(self) -> None:
        for resource in self.resources.values():
            resource.restore_renewal_rate()

    def affect_renewal_rates(self, renewal_rates: dict[str, float]) -> None:
        for name, rate in renewal_rates.items():
            self.resources[name].affect_renewal_rate(rate)

    def visible_resources(
        self,
        square: Square,
        resources: list[str],
    ) -> dict[str, float]:
        visability: dict[str, float] = {}
        dist = utils.manhattan_distance(self.coords, square.coords)

        for name in resources:
            visability[name] = self.resources[name].visible_from(dist)

        return visability
