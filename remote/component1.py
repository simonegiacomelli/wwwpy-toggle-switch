import inspect
import wwwpy.remote.component as wpc
import js

import logging

logger = logging.getLogger(__name__)

class Component1(wpc.Component, tag_name='component-1'):
    input1: js.HTMLInputElement = wpc.element()
    slSwitch1: js.HTMLElement = wpc.element()
    def init_component(self):
        # language=html
        self.element.innerHTML = """
<div>component-1</div>
<input data-name="input1" placeholder="input1">
<hr>
<sl-switch data-name="slSwitch1">slSwitch1</sl-switch>
<hr>
<uc-toggle-switch></uc-toggle-switch>
<hr>
<uc-toggle-switch></uc-toggle-switch>
"""
