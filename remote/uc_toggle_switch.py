import logging

import js
import wwwpy.remote.component as wpc
from wwwpy.remote import dict_to_js

logger = logging.getLogger(__name__)


class UcToggleSwitchComponent(wpc.Component, tag_name='uc-toggle-switch'):
    checked: str = wpc.attribute()
    _checkbox: js.HTMLInputElement = wpc.element()

    def init_component(self):
        self.element.attachShadow(dict_to_js({'mode': 'open'}))
        # language=html
        self.element.shadowRoot.innerHTML = """<style>
    :host {
        --width: 2.5em;
        --height: 1.42em;
        --offset: 0.17em;
        --slider-size: calc(var(--height) - 0.33em);
    }

    .switch {
        position: relative;
        display: inline-block;
        width: var(--width);
        height: var(--height);
    }

    .switch input {
        opacity: 0;
        width: 0;
        height: 0;
    }

    .slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #ccc;
        transition: .4s;
    }

    .slider:before {
        position: absolute;
        content: "";
        height: var(--slider-size);
        width: var(--slider-size);
        left: var(--offset);
        bottom: var(--offset);
        background-color: white;
        transition: .4s;
    }

    input:checked + .slider {
        background-color: #2196F3;
    }

    input:focus + .slider {
        box-shadow: 0 0 1px #2196F3;
    }

    input:checked + .slider:before {
        transform: translateX(calc(var(--width) - var(--height)));
    }

    .slider.round {
        border-radius: var(--height);
    }

    .slider.round:before {
        border-radius: 50%;
    }
</style>
<!--
<label class="switch">
    <input type="checkbox">
    <span class="slider"></span>
</label>
-->

<label class="switch">
    <input type="checkbox" data-name="_checkbox">
    <span class="slider round"></span>
</label>
        """

        self._update_attributes()

    def attributeChangedCallback(self, name: str, oldValue: str, newValue: str):
        self._update_attributes()

    def _update_attributes(self):
        self._checkbox.checked = self.checked is not None
