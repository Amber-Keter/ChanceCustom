'''
_________ ___________________ ____  __.
\_   ___ \\_   ___ \______   \    |/ _|
/    \  \//    \  \/|     ___/      <  
\     \___\     \___|    |   |    |  \ 
 \______  /\______  /____|   |____|__ \
        \/        \/                 \/
@File      :   main.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL
@Copyright :   (C) 2020-2022, OlivOS-Team
@Desc      :   None
'''

import OlivOS
import ChanceCustom

import platform

class Event(object):
    def init(plugin_event:OlivOS.API.Event, Proc:OlivOS.pluginAPI.shallow):
        pass

    def init_after(plugin_event:OlivOS.API.Event, Proc:OlivOS.pluginAPI.shallow):
        ChanceCustom.load.listPlugin = Proc.get_plugin_list()
        ChanceCustom.load.dictBotInfo = Proc.Proc_data['bot_info_dict']
        ChanceCustom.load.initCustomData(ChanceCustom.load.dictBotInfo)

    def private_message(plugin_event:OlivOS.API.Event, Proc:OlivOS.pluginAPI.shallow):
        ChanceCustom.replyCore.unity_reply(plugin_event, Proc, 'private_message')

    def group_message(plugin_event:OlivOS.API.Event, Proc:OlivOS.pluginAPI.shallow):
        ChanceCustom.replyCore.unity_reply(plugin_event, Proc, 'group_message')

    def poke(plugin_event:OlivOS.API.Event, Proc:OlivOS.pluginAPI.shallow):
        pass

    def save(plugin_event:OlivOS.API.Event, Proc:OlivOS.pluginAPI.shallow):
        ChanceCustom.load.saveCustomData()

    def menu(plugin_event:OlivOS.API.Event, Proc:OlivOS.pluginAPI.shallow):
        if(platform.system() == 'Windows'):
            if plugin_event.data.namespace == 'ChanceCustom':
                if plugin_event.data.event == 'ChanceCustom_001':
                    if not ChanceCustom.load.flag_open:
                        ChanceCustom.load.flag_open = True
                        ChanceCustom.GUI.ConfigUI(
                            Model_name = 'shallow_menu_plugin_manage',
                            logger_proc = Proc.Proc_info.logger_proc.log
                        ).start()
