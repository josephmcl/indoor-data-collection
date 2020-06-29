import { UI } from './constants.js';
import { UIDashboard } from './dashboard.js';
import { UIDevices } from './devices.js';


const tagName = 'ui-navigation';
export class UINavigation extends HTMLElement {
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

    this.dashboardButtonElement   = this.makeButton(
        UI.imageDir + '/circle.png', 'Dashboard');
    this.devicesButtonElement     = this.makeButton(
        UI.imageDir + '/circle.png', 'Devices');
    this.collectionsButtonElement = this.makeButton(
        UI.imageDir + '/circle.png', 'Collections');
    this.settingsButtonElement    = this.makeButton(
        UI.imageDir + '/circle.png', 'Settings');
    shadowRoot.appendChild(this.dashboardButtonElement);
    shadowRoot.appendChild(this.devicesButtonElement);
    shadowRoot.appendChild(this.collectionsButtonElement);
    shadowRoot.appendChild(this.settingsButtonElement);

    this.dashboardButtonElement.addEventListener('click', (e) => { 
        this.dispatchEvent(new CustomEvent('select-view', {'detail': 
            UIDashboard.key}));
    })
    this.devicesButtonElement.addEventListener('click', (e) => { 
        this.dispatchEvent(new CustomEvent('select-view', {'detail': 
            UIDevices.key}));
    })
    this.collectionsButtonElement.addEventListener('click', (e) => { 
        console.log('hello')
    })
    this.settingsButtonElement.addEventListener('click', (e) => { 
        console.log('hello')
    })
  }  

  makeButton(imagePath, description) {
    let buttonElement = document.createElement('div');
    let imageElement = document.createElement('img');
    let spanElement = document.createElement('span')
    imageElement.className = 'menu-icon';
    imageElement.src = imagePath;
    spanElement.innerHTML = description;
    buttonElement.appendChild(imageElement);
    buttonElement.appendChild(spanElement);
    return buttonElement;
  }

};
window.customElements.define(tagName, UINavigation);
