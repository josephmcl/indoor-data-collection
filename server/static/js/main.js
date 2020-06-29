import { UI } from "./constants.js";
import { UIDashboard } from './dashboard.js';
import { UIDevices } from './devices.js';

const tagName = 'ui-main';
export class UIMain extends HTMLElement {
    constructor() {
        super();

        // create shadow root
        const shadowRoot = this.attachShadow({mode: 'open'});

        // load css
        this.linkElement      = document.createElement('link');
        this.linkElement.href = "static/css/web_components/main.css";
        this.linkElement.type = "text/css";
        this.linkElement.rel  = "stylesheet";
        shadowRoot.appendChild(this.linkElement);

        this.viewKey = '';
        this.views = { };
        this.views[UIDashboard.key] = UIDashboard;
        this.views[UIDevices.key]   = UIDevices;
    }  
    clearChildren() {
        while (this.shadowRoot.lastChild !== this.linkElement) 
            this.shadowRoot.removeChild(this.shadowRoot.lastChild);
    }
    async selectView(key) {
        if (this.viewKey !== key) {
            this.viewKey = key;
            this.clearChildren();
            this.appView = document.createElement(this.views[this.viewKey].tagName);
            this.shadowRoot.appendChild(this.appView);
        }   
    }
};
window.customElements.define(tagName, UIMain);