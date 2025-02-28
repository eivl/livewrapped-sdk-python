#  See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .ad_unit_minimal import AdUnitMinimal

__all__ = ["AdUnitRetrieveResponse"]

AdUnitRetrieveResponse: TypeAlias = List[AdUnitMinimal]
