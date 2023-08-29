#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Dict

from android.modinfo import ModInfo
from sims.sim_info import SimInfo
from sims4communitylib.utils.sims.common_buff_utils import CommonBuffUtils
from sims4communitylib.utils.sims.common_trait_utils import CommonTraitUtils
from ts4lib.utils.tuning_helper import TuningHelper

from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()
log.debug(f"Starting {ModInfo.get_identity().name}")


class MakeAndroid:
    def __init__(self):
        th = TuningHelper()
        self.android_trait_ids = th.get_tuning_ids(None, [
            "trait_GenderOptions_Pregnancy_CanNotImpregnate",
            "trait_GenderOptions_Pregnancy_CanNot_BeImpregnated",
            "trait_Cauldron_Potion_Immortality",
            "trait_Hidden_ChildCannotAgeUp_DoesNotPersist",
        ])
        self.android_buff_ids = th.get_tuning_ids(None, [
            "Buff_NoGreetings",
            "buff_NPC_Suppress_All_Motive_Decay",
            "buff_Suntan_LockDecay",
            "Buff_Trait_SpeedCleaner",
            "Buff_Trait_SpeedReader",
        ])
        _suppress_android_buff_ids = th.get_tuning_ids(None, ['buff_Suppress_*', ])
        rm_suppress_android_buff_ids = th.get_tuning_ids(None, [
            'buff_Suppress_Visible_Motives_Exclude_Energy',
            # 'buff_SuppressFrontPagePieMenu',
        ])
        buff_suppress_ids = _suppress_android_buff_ids.difference(rm_suppress_android_buff_ids)
        self.android_buff_ids.update(_suppress_android_buff_ids)

        self.android_undo_control_ids = th.get_tuning_ids(None, [
            "buff_SuppressFrontPagePieMenu", "buff_Suppress_All_Interaction", "buff_Suppress_AllAutonomy",
        ])

        self.androids: Dict = {}

    # Android Spawn Location

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.android.add', 'Convert active Sim to Android')
    def cheat_o19_android_add(output: CommonConsoleCommandOutput):
        ma = MakeAndroid()
        sim_info: SimInfo = CommonSimUtils.get_active_sim_info()
        CommonBuffUtils().add_buffs(sim_info, ma.android_buff_ids)
        CommonTraitUtils().add_traits(sim_info, ma.android_trait_ids)

        # set spawn-location
        ma.androids.update({sim_info: None})
        output(f"{ ma.android_buff_ids}")
        output(f"{ma.android_trait_ids}")
        output("ok")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.android.control', 'Control Android')
    def cheat_o19_android_control(output: CommonConsoleCommandOutput):
        ma = MakeAndroid()
        sim_info: SimInfo = CommonSimUtils.get_active_sim_info()
        if sim_info in ma.androids.keys():
            CommonBuffUtils.remove_buffs(sim_info, ma.andoid_control_buff_ids)
            output("ok")

'''
<I c="Buff" i="buff" m="buffs.buff" n="Buff_NoGreetings" s="123741">
<I c="Buff" i="buff" m="buffs.buff" n="buff_NPC_Suppress_All_Motive_Decay" s="121359">
<I c="Buff" i="buff" m="buffs.buff" n="buff_Suntan_LockDecay" s="206066">
<I c="Trait" i="trait" m="traits.traits" n="trait_GenderOptions_Pregnancy_CanNotImpregnate" s="137717">
<I c="Trait" i="trait" m="traits.traits" n="trait_GenderOptions_Pregnancy_CanNot_BeImpregnated" s="137716">
<I c="Buff" i="buff" m="buffs.buff" n="Buff_Trait_SpeedCleaner" s="26620">
<I c="Buff" i="buff" m="buffs.buff" n="Buff_Trait_SpeedReader" s="32627">
<I c="Trait" i="trait" m="traits.traits" n="trait_Cauldron_Potion_Immortality" s="214389"> ==> replace
<I c="Trait" i="trait" m="traits.traits" n="trait_Hidden_ChildCannotAgeUp_DoesNotPersist" s="116617"> -> replace


<I c="Buff" i="buff" m="buffs.buff" n="buff_SuppressFrontPagePieMenu" s="121942">
<I c="Buff" i="buff" m="buffs.buff" n="buff_SuppressFrontPagePieMenu" s="115761">
<I c="Buff" i="buff" m="buffs.buff" n="buff_Suppress_All_Interaction" s="24732">
<I c="Buff" i="buff" m="buffs.buff" n="buff_Suppress_AllAutonomy" s="169901">

<I c="Buff" i="buff" m="buffs.buff" n="buff_Suppress_Emotion_Idle" s="129126">
<I c="Buff" i="buff" m="buffs.buff" n="Buff_Suppress_Reaction_SmellsBad" s="99740">
<I c="Buff" i="buff" m="buffs.buff" n="buff_Suppress_Visible_Motives" s="27833">
<I c="Buff" i="buff" m="buffs.buff" n="buff_Suppress_Trait_Idle" s="334350">
<I c="Buff" i="buff" m="buffs.buff" n="buff_Suppress_InLabor" s="256302">
<I c="Buff" i="buff" m="buffs.buff" n="buff_Suppress_LoveLetter" s="100870">
'''

