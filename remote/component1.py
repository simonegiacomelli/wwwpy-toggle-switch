import inspect
import wwwpy.remote.component as wpc
import js

import logging

from remote.uc_toggle_switch import UcToggleSwitchComponent

logger = logging.getLogger(__name__)

class Component1(wpc.Component, tag_name='component-1'):
    input1: js.HTMLInputElement = wpc.element()
    slSwitch1: js.HTMLElement = wpc.element()
    button1: js.HTMLButtonElement = wpc.element()
    sw1: UcToggleSwitchComponent = wpc.element()
    sw2: UcToggleSwitchComponent = wpc.element()
    def init_component(self):
        # language=html
        self.element.innerHTML = """
<div>component-1</div>
<input data-name="input1" placeholder="input1">
<hr>
<sl-switch data-name="slSwitch1">slSwitch1</sl-switch>
<button data-name="button1">button1</button>
<hr>
<uc-toggle-switch data-name='sw1' checked text='ccc'></uc-toggle-switch>
<hr>
<uc-toggle-switch data-name='sw2' text='changes the above'></uc-toggle-switch>
"""
    
    async def sw1__input(self, event):
        logger.debug(f'sw1={self.sw1.checked_bool} ')

    async def sw2__input(self, event):
        logger.debug(f'sw2={self.sw1.checked_bool} ')
        self.sw1.checked_bool = self.sw2.checked_bool

    
    async def button1__click(self, event):
        logger.debug(f'{inspect.currentframe().f_code.co_name} event fired %s', event)
    
    


