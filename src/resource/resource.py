from __future__ import annotations
import copy


class Resource:
    def __init__(
        self,
        name: str,
        visability: int,
        initial_amount: float,
        limit: float,
        renewable: bool,
        base_renewal_rate: float,
    ):
        self.name = name
        self.visability = visability
        self.amount = initial_amount
        self.limit = limit
        self.renewable = renewable
        self.renewal_rate = base_renewal_rate
        self.base_renewal_rate = base_renewal_rate

    def clone(self) -> Resource:
        return copy.deepcopy(self)

    def restore_renewal_rate(self) -> None:
        self.renewal_rate = self.base_renewal_rate

    def affect_renewal_rate(self, percent: float) -> None:
        self.renewal_rate *= 1 + percent

    def consume(self, amount: float) -> float:
        if self.amount < amount:
            amount = self.amount

        self.amount -= amount
        return amount

    def renew(self) -> None:
        self.amount += self.renewal_rate

        if self.amount > self.limit:
            self.amount = self.limit

    def visible_from(self, distance: int) -> bool:
        return distance <= self.visability

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Resource):
            return False
        return self.name == __value.name
