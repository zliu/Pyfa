# eliteBonusLogisticsTrackingLinkTrackingSpeedBonus1
#
# Used by:
# Ship: Scimitar
type = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Tracking Computer",
                                  "trackingSpeedBonus", ship.getModifiedItemAttr("eliteBonusLogistics1"),
                                  skill="Logistics Cruisers")
