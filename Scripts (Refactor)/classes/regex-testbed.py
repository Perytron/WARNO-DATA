import re

# NOT USED ACTIVELY - ONLY REGEX TESTBED BESIDES https://regex101.com/

# pattern = r"export\s+(\w+)\s+is\s+TWeaponManagerModuleDescriptor\s*(([\s\S]*?)(\s+\)\n\s+\]\n\)))"
# pattern = r"(TTurretTwoAxisDescriptor).*?\n\s+([\s\S]*?\)(?![^)]+,)[\s\S]*?\))"
# pattern = r"(TMountedWeaponDescriptor).*?\n\s+([\s\S]*?\))"

# pattern = r"OutOfRangeTrackingDuration\s+=\s+(\S+)"
pattern = r"FlyingSpeed\s+=\s+\(\((\d+)\)\s*\*\s*Metre\)"

content = """$5$export WeaponDescriptor_2K12_KUB_DDR is TWeaponManagerModuleDescriptor
(
    DelayIdleAmmoSorting = DelayIdleAmmoSorting
    DefaultHoldFireState = False
    DefaultRiposteStance = False
    NeedsExplicitOrderToUseSmoke = True
    Salves               = [
        1,
        -1,
        -1,
        -1,
        -1,
        -1
    ]
    HasMainSalvo = False
    SalvoIsMainSalvo =
    [
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]
    AlwaysOrientArmorTowardsThreat = True
    TurretDescriptorList = [
        TTurretTwoAxisDescriptor
        (
            AngleRotationBase               = 0.0
            AngleRotationBasePitch          = 0.17453292519943275
            AngleRotationMax                = 6.283185307179586
            AngleRotationMaxPitch           = 1.3089969389957472
            AngleRotationMinPitch           = -0.2617993877991494
            MountedWeaponDescriptorList     = [
                TMountedWeaponDescriptor
                (
                    AmmoConsumption_ForInterface        = 1
                    Ammunition                          = ~/Ammo_SAM_9M336_x3
                    AnimateOnlyOneSoldier               = False
                    DispersionRadiusOffColor            = RGBA[0,0,0,0]
                    DispersionRadiusOffThickness        = -0.1
                    DispersionRadiusOnColor             = RGBA[0,0,0,0]
                    DispersionRadiusOnThickness         = -0.1
                    EffectTag                           = 'FireEffect_SAM_9M336_x3'
                    HandheldEquipmentKey                = 'MeshAlternative_1'
                    NbWeapons                           = 1
                    SalvoStockIndex                     = 0
                    ShowDispersion                      = False
                    ShowInInterface                     = True
                    ShowSplashRadius                    = False
                    SplashRadiusOffColor                = RGBA[0,0,0,0]
                    SplashRadiusOffThickness            = -0.1
                    SplashRadiusOnColor                 = RGBA[0,0,0,0]
                    SplashRadiusOnThickness             = -0.1
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_1'
                    WeaponIgnoredPropertyName           = 'WeaponIgnored_1'
                    WeaponShootDataPropertyName         = ["WeaponShootData_0_1", ]
                )
            ]
            NbFX                            = 2
            OutOfRangeTrackingDuration      = 3.5
            Tag                             = 'tourelle1'
            TurretIdleBehaviourDescriptor   = ~/TurretIdle_DCAAutoMoteur
            VitesseRotation                 = 2.0943951023931953
            YulBoneOrdinal                  = 1
        )
    ]
)
export WeaponDescriptor_AH64_Apache_US is TWeaponManagerModuleDescriptor
(
    DelayIdleAmmoSorting = DelayIdleAmmoSorting
    DefaultHoldFireState = False
    DefaultRiposteStance = False
    NeedsExplicitOrderToUseSmoke = True
    Salves               = [
        80,
        1,
        2,
        -1,
        -1,
        -1
    ]
    HasMainSalvo = False
    SalvoIsMainSalvo =
    [
        False,
        False,
        False,
        False,
        False,
    ]
    AlwaysOrientArmorTowardsThreat = True
    TurretDescriptorList = [
        TTurretTwoAxisDescriptor
        (
            AngleRotationBase               = 0.0
            AngleRotationBasePitch          = 0.0
            AngleRotationMax                = 3.839724354387525
            AngleRotationMaxPitch           = 0.17453292519943295
            AngleRotationMinPitch           = -1.3089969389957472
            MountedWeaponDescriptorList     = [
                TMountedWeaponDescriptor
                (
                    AmmoConsumption_ForInterface        = 1
                    Ammunition                          = ~/Ammo_AutoCanon_AP_30mm_M230
                    AnimateOnlyOneSoldier               = False
                    DispersionRadiusOffColor            = RGBA[0,0,0,0]
                    DispersionRadiusOffThickness        = -0.1
                    DispersionRadiusOnColor             = RGBA[0,0,0,0]
                    DispersionRadiusOnThickness         = -0.1
                    EffectTag                           = 'FireEffect_AutoCanon_AP_30mm_M230'
                    HandheldEquipmentKey                = 'MeshAlternative_1'
                    NbWeapons                           = 1
                    SalvoStockIndex                     = 0
                    ShowDispersion                      = False
                    ShowInInterface                     = True
                    ShowSplashRadius                    = False
                    SplashRadiusOffColor                = RGBA[0,0,0,0]
                    SplashRadiusOffThickness            = -0.1
                    SplashRadiusOnColor                 = RGBA[0,0,0,0]
                    SplashRadiusOnThickness             = -0.1
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_1'
                    WeaponIgnoredPropertyName           = 'WeaponIgnored_1'
                    WeaponShootDataPropertyName         = ["WeaponShootData_0_1", ]
                ),
                TMountedWeaponDescriptor
                (
                    AmmoConsumption_ForInterface        = 1
                    Ammunition                          = ~/Ammo_AutoCanon_HE_30mm_M230
                    AnimateOnlyOneSoldier               = False
                    DispersionRadiusOffColor            = RGBA[0,0,0,0]
                    DispersionRadiusOffThickness        = -0.1
                    DispersionRadiusOnColor             = RGBA[0,0,0,0]
                    DispersionRadiusOnThickness         = -0.1
                    EffectTag                           = 'FireEffect_AutoCanon_HE_30mm_M230'
                    HandheldEquipmentKey                = 'MeshAlternative_2'
                    NbWeapons                           = 1
                    SalvoStockIndex                     = 0
                    ShowDispersion                      = False
                    ShowInInterface                     = True
                    ShowSplashRadius                    = False
                    SplashRadiusOffColor                = RGBA[0,0,0,0]
                    SplashRadiusOffThickness            = -0.1
                    SplashRadiusOnColor                 = RGBA[0,0,0,0]
                    SplashRadiusOnThickness             = -0.1
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_2'
                    WeaponIgnoredPropertyName           = 'WeaponIgnored_2'
                    WeaponShootDataPropertyName         = ["WeaponShootData_0_2", ]
                )
            ]
            NbFX                            = 1
            Tag                             = 'tourelle1'
            TurretIdleBehaviourDescriptor   = ~/TurretIdle_WatchForwardNormal
            VitesseRotation                 = 2.0943951023931953
            YulBoneOrdinal                  = 1
        ),
        TTurretUnitDescriptor
        (
            AngleRotationMax            = 0.3490658503988659
            AngleRotationMaxPitch       = 0.3490658503988659
            AngleRotationMinPitch       = -0.2617993877991494
            MountedWeaponDescriptorList = [
                TMountedWeaponDescriptor
                (
                    AmmoConsumption_ForInterface        = 1
                    Ammunition                          = ~/Ammo_RocketAir_Hydra_70mm_x19
                    AnimateOnlyOneSoldier               = True
                    DispersionRadiusOffColor            = RGBA[0,0,0,0]
                    DispersionRadiusOffThickness        = -0.1
                    DispersionRadiusOnColor             = RGBA[0,0,0,0]
                    DispersionRadiusOnThickness         = -0.1
                    EffectTag                           = 'FireEffect_RocketAir_Hydra_70mm_x19'
                    HandheldEquipmentKey                = 'MeshAlternative_4'
                    NbWeapons                           = 1
                    SalvoStockIndex                     = 2
                    ShowDispersion                      = False
                    ShowInInterface                     = True
                    ShowSplashRadius                    = False
                    SplashRadiusOffColor                = RGBA[0,0,0,0]
                    SplashRadiusOffThickness            = -0.1
                    SplashRadiusOnColor                 = RGBA[0,0,0,0]
                    SplashRadiusOnThickness             = -0.1
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_4'
                    WeaponIgnoredPropertyName           = 'WeaponIgnored_4'
                    WeaponShootDataPropertyName         = ["WeaponShootData_0_4", ]
                )
            ]
            NbFX                        = 2
            Tag                         = 'tourelle2'
            YulBoneOrdinal              = 2
        ),
        TTurretUnitDescriptor
        (
            AngleRotationMax            = 1.3962634015954636
            AngleRotationMaxPitch       = 0.5235987755982988
            AngleRotationMinPitch       = -0.5235987755982988
            MountedWeaponDescriptorList = [
                TMountedWeaponDescriptor
                (
                    AmmoConsumption_ForInterface        = 1
                    Ammunition                          = ~/Ammo_AGM_AGM114A_x8
                    AnimateOnlyOneSoldier               = True
                    DispersionRadiusOffColor            = RGBA[0,0,0,0]
                    DispersionRadiusOffThickness        = -0.1
                    DispersionRadiusOnColor             = RGBA[0,0,0,0]
                    DispersionRadiusOnThickness         = -0.1
                    EffectTag                           = 'FireEffect_AGM_AGM114A_x8'
                    HandheldEquipmentKey                = 'MeshAlternative_3'
                    NbWeapons                           = 1
                    SalvoStockIndex                     = 1
                    ShowDispersion                      = False
                    ShowInInterface                     = True
                    ShowSplashRadius                    = False
                    SplashRadiusOffColor                = RGBA[0,0,0,0]
                    SplashRadiusOffThickness            = -0.1
                    SplashRadiusOnColor                 = RGBA[0,0,0,0]
                    SplashRadiusOnThickness             = -0.1
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_3'
                    WeaponIgnoredPropertyName           = 'WeaponIgnored_3'
                    WeaponShootDataPropertyName         = ["WeaponShootData_0_3", ]
                )
            ]
            NbFX                        = 2
            Tag                         = 'tourelle3'
            YulBoneOrdinal              = 3
        )
    ]
)
export WeaponDescriptor_A10_Thunderbolt_II_US is TWeaponManagerModuleDescriptor
(
    DelayIdleAmmoSorting = DelayIdleAmmoSorting
    DefaultHoldFireState = False
    DefaultRiposteStance = False
    NeedsExplicitOrderToUseSmoke = True
    Salves               = [
        16,
        1,
        2,
        -1,
        -1,
        -1
    ]
    HasMainSalvo = True
    SalvoIsMainSalvo =
    [
        False,
        True,
        False,
        False,
    ]
    AlwaysOrientArmorTowardsThreat = True
    TurretDescriptorList = [
        TTurretTwoAxisDescriptor
        (
            AngleRotationBase           = 0.0
            AngleRotationBasePitch      = 0.0
            AngleRotationMax            = 0.12217304763960307
            AngleRotationMaxPitch       = 0.12217304763960307
            AngleRotationMinPitch       = -0.12217304763960307
            MountedWeaponDescriptorList = [
                TMountedWeaponDescriptor
                (
                    AmmoConsumption_ForInterface        = 1
                    Ammunition                          = ~/Ammo_GatlingAir_GAU8_30mm
                    AnimateOnlyOneSoldier               = False
                    DispersionRadiusOffColor            = RGBA[0,0,0,0]
                    DispersionRadiusOffThickness        = -0.1
                    DispersionRadiusOnColor             = RGBA[0,0,0,0]
                    DispersionRadiusOnThickness         = -0.1
                    EffectTag                           = 'FireEffect_GatlingAir_GAU8_30mm'
                    HandheldEquipmentKey                = 'MeshAlternative_1'
                    NbWeapons                           = 1
                    SalvoStockIndex                     = 0
                    ShowDispersion                      = False
                    ShowInInterface                     = True
                    ShowSplashRadius                    = False
                    SplashRadiusOffColor                = RGBA[0,0,0,0]
                    SplashRadiusOffThickness            = -0.1
                    SplashRadiusOnColor                 = RGBA[0,0,0,0]
                    SplashRadiusOnThickness             = -0.1
                    TirContinu                          = True
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_1'
                    WeaponIgnoredPropertyName           = 'WeaponIgnored_1'
                    WeaponShootDataPropertyName         = ["WeaponShootData_0_1", ]
                ),
                TMountedWeaponDescriptor
                (
                    AmmoConsumption_ForInterface        = 1
                    Ammunition                          = ~/Ammo_GatlingAir_AP_GAU8_30mm
                    AnimateOnlyOneSoldier               = False
                    DispersionRadiusOffColor            = RGBA[0,0,0,0]
                    DispersionRadiusOffThickness        = -0.1
                    DispersionRadiusOnColor             = RGBA[0,0,0,0]
                    DispersionRadiusOnThickness         = -0.1
                    EffectTag                           = 'FireEffect_GatlingAir_AP_GAU8_30mm'
                    HandheldEquipmentKey                = 'MeshAlternative_2'
                    NbWeapons                           = 1
                    SalvoStockIndex                     = 0
                    ShowDispersion                      = False
                    ShowInInterface                     = True
                    ShowSplashRadius                    = False
                    SplashRadiusOffColor                = RGBA[0,0,0,0]
                    SplashRadiusOffThickness            = -0.1
                    SplashRadiusOnColor                 = RGBA[0,0,0,0]
                    SplashRadiusOnThickness             = -0.1
                    TirContinu                          = True
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_2'
                    WeaponIgnoredPropertyName           = 'WeaponIgnored_2'
                    WeaponShootDataPropertyName         = ["WeaponShootData_0_2", ]
                )
            ]
            NbFX                        = 1
            Tag                         = 'tourelle1'
            VitesseRotation             = 1.5707963267948966
            YulBoneOrdinal              = 1
        ),
        TTurretBombardierDescriptor
        (
            FlyingAltitude              = ((1500) * Metre)
            FlyingSpeed                 = ((910) * Metre)
            MountedWeaponDescriptorList = [
                TMountedWeaponDescriptor
                (
                    AmmoConsumption_ForInterface        = 1
                    Ammunition                          = ~/Ammo_Bomb_Mk82_250kg_x8
                    AnimateOnlyOneSoldier               = True
                    DispersionRadiusOffColor            = RGBA[0,0,0,0]
                    DispersionRadiusOffThickness        = -0.1
                    DispersionRadiusOnColor             = RGBA[0,0,0,0]
                    DispersionRadiusOnThickness         = -0.1
                    EffectTag                           = 'FireEffect_Bomb_Mk82_250kg_x8'
                    HandheldEquipmentKey                = 'MeshAlternative_3'
                    NbWeapons                           = 1
                    SalvoStockIndex                     = 1
                    ShowDispersion                      = False
                    ShowInInterface                     = True
                    ShowSplashRadius                    = False
                    SplashRadiusOffColor                = RGBA[0,0,0,0]
                    SplashRadiusOffThickness            = -0.1
                    SplashRadiusOnColor                 = RGBA[0,0,0,0]
                    SplashRadiusOnThickness             = -0.1
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_3'
                    WeaponIgnoredPropertyName           = 'WeaponIgnored_3'
                    WeaponShootDataPropertyName         = ["WeaponShootData_0_3", ]
                )
            ]
            NbFX                        = 2
            Tag                         = 'tourelle2'
            YulBoneOrdinal              = 2
        ),
        TTurretUnitDescriptor
        (
            AngleRotationMax                        = 1.3962634015954636
            AngleRotationMaxPitch                   = 0.5235987755982988
            AngleRotationMinPitch                   = -0.5235987755982988
            MountedWeaponDescriptorList             = [
                TMountedWeaponDescriptor
                (
                    AmmoConsumption_ForInterface        = 1
                    Ammunition                          = ~/Ammo_AA_AIM9M_Sidewinder
                    AnimateOnlyOneSoldier               = True
                    DispersionRadiusOffColor            = RGBA[0,0,0,0]
                    DispersionRadiusOffThickness        = -0.1
                    DispersionRadiusOnColor             = RGBA[0,0,0,0]
                    DispersionRadiusOnThickness         = -0.1
                    EffectTag                           = 'FireEffect_AA_AIM9M_Sidewinder'
                    HandheldEquipmentKey                = 'MeshAlternative_4'
                    NbWeapons                           = 1
                    SalvoStockIndex                     = 2
                    ShowDispersion                      = False
                    ShowInInterface                     = True
                    ShowSplashRadius                    = False
                    SplashRadiusOffColor                = RGBA[0,0,0,0]
                    SplashRadiusOffThickness            = -0.1
                    SplashRadiusOnColor                 = RGBA[0,0,0,0]
                    SplashRadiusOnThickness             = -0.1
                    WeaponActiveAndCanShootPropertyName = 'WeaponActiveAndCanShoot_4'
                    WeaponIgnoredPropertyName           = 'WeaponIgnored_4'
                    WeaponShootDataPropertyName         = ["WeaponShootData_0_4", ]
                )
            ]
            NbFX                                    = 2
            OwnerTurnHisChassisVerticallyToAttack   = True
            Tag                                     = 'tourelle3'
            YulBoneOrdinal                          = 3
        )
    ]
)"""

matches = re.findall(pattern, content)
matchR = re.search(pattern, content)

print(matchR.group(1))

for match in matches:
    print(match[1])