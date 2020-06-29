import { UI } from "./constants.js";
import { UINavigation } from "./navigation.js";
import { UIMain } from "./main.js";

const tagName = 'ui-app';
export class UIApp extends HTMLElement {
  constructor() {
    super();

    // create shadow root
    const shadowRoot = this.attachShadow({mode: 'open'});

    // load css
    this.linkElement      = document.createElement('link');
    this.linkElement.href = "static/css/web_components/app.css";
    this.linkElement.type = "text/css";
    this.linkElement.rel  = "stylesheet";
    shadowRoot.appendChild(this.linkElement);

    this.navigationElement = document.createElement('ui-navigation');
    let mainElement = document.createElement('ui-main');
    this.mainElement = mainElement;
    // this.mainElement = new UIMain();
    shadowRoot.appendChild(this.navigationElement);
    shadowRoot.appendChild(mainElement);
    /*
    this.actionsElement = document.createElement('div');
    this.actionsElement.id = 'actions';
    shadowRoot.appendChild(this.actionsElement);

    this.deviceListHeader = document.createElement('div');
    this.deviceListHeader.id = 'devices-list-header';
    */
    this.navigationElement.addEventListener('select-view', (e) => { 
        mainElement.selectView(e.detail);
    })
  }  
};
window.customElements.define(tagName, UIApp);
