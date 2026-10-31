import pytest

from recycling_rewards import (
    reward_points,
    collection_accepted,
    slot_status,
)


@pytest.mark.parametrize(
    "material, weight, bonus, expected",
    [
        ("paper", 3, False, 0),
        ("paper", 6, True, 12),
        ("metal", 23, False, 378),
    ],
)
def test_reward_points(material, weight, bonus, expected):
    assert reward_points(material, weight, bonus) == expected


def test_unknown_material():
    with pytest.raises(ValueError, match="unknown material"):
        reward_points("glass", 5, False)


def test_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        reward_points("paper", -1, False)


@pytest.mark.parametrize(
    "weight, bags, hazardous, expected",
    [
        (4, 1, True, True),
        (51, 1, False, False),
        (20, 2, False, True),
    ],
)
def test_collection_accepted(weight, bags, hazardous, expected):
    assert collection_accepted(weight, bags, hazardous) is expected


@pytest.mark.parametrize(
    "minutes, morning, holiday, expected",
    [
        (35, True, True, "open"),
        (0, False, False, "late"),
        (-6, False, False, "missed"),
    ],
)
def test_slot_status(minutes, morning, holiday, expected):
    assert slot_status(minutes, morning, holiday) == expected