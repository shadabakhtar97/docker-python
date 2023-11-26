import asyncio
import random
import hashlib

from pymatgen.core.composition import Composition


async def fooness(formula: str) -> int:
    formula = Composition(formula, strict=True).reduced_formula

    sleep_time = random.uniform(0.5, 10)
    await asyncio.sleep(sleep_time)

    hash_object = hashlib.sha256(formula.encode())
    hex_dig = hash_object.hexdigest()
    fooness_value = int(hex_dig, 16) % 100

    return fooness_value