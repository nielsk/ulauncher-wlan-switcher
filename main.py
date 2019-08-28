from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


class WlanSwitcher(Extension):

    def __init__(self):
        super(WlanSwitcher, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        options = ['on', 'off']
        my_list = event.query.split(" ")
        if len(my_list) == 1:
            items.append(self.get_off_item())
            items.append(self.get_on_item())
        else:
            my_query = my_list[1]
            included = []
            for option in options:
                if my_query in options:
                    if option in ['on']:
                        items.append(self.get_on_item())
                    elif option in ['off']:
                        items.append(self.get_off_item())

        return RenderResultListAction(items)

    @staticmethod
    def get_on_item():
        return ExtensionResultItem(icon='images/icon.png',
                                   name='WLAN ON',
                                   description='Switch WLAN On',
                                   on_enter=RunScriptAction("nmcli radio wifi on", None))

    @staticmethod
    def get_off_item():
        return ExtensionResultItem(icon='images/icon.png',
                                   name='WLAN OFF',
                                   description='Switch WLAN Off',
                                   on_enter=RunScriptAction("nmcli radio wifi off", None))


if __name__ == '__main__':
    WlanSwitcher().run()
