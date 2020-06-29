import { UI } from "./constants.js";
import { UIAppView } from "./app_view.js";


const tagName = 'ui-dashboard';
export class UIDashboard extends UIAppView {
  constructor() {
    super();

    // create shadow root
    const shadowRoot = this.attachShadow({mode: 'open'});

    // load css
    this.linkElement      = document.createElement('link');
    this.linkElement.href = "static/css/web_components/navigation.css";
    this.linkElement.type = "text/css";
    this.linkElement.rel  = "stylesheet";
    shadowRoot.appendChild(this.linkElement);
  }  
};
UIDashboard.key = 'dashboard';
UIDashboard.tagName = 'ui-dashboard';
window.customElements.define(tagName, UIDashboard);