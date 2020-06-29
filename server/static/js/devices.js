import { UI } from "./constants.js";
import { UIAppView } from "./app_view.js";

// for developing
let make_li = () => {
  let li = document.createElement('li');
  const name = document.createElement('div');
  const accessKey = document.createElement('div');
  const created = document.createElement('div');
  name.innerHTML = 'Name'
  accessKey.innerHTML = 'Access Key'
  created.innerHTML = '2020-01-01'
  name.className = 'devices-list-value'
  accessKey.className = 'devices-list-secret-value'
  created.className = 'devices-list-value'
  li.appendChild(name);
  li.appendChild(accessKey);
  li.appendChild(created);
  return li;
}

const tagName = 'ui-devices';
export class UIDevices extends UIAppView {
  constructor() {
    super();

    // create shadow root
    const shadowRoot = this.attachShadow({mode: 'open'});

    // load css
    this.linkElement      = document.createElement('link');
    this.linkElement.href = "static/css/web_components/devices.css";
    this.linkElement.type = "text/css";
    this.linkElement.rel  = "stylesheet";
    shadowRoot.appendChild(this.linkElement);

    this.actionsElement = document.createElement('div');
    this.actionsElement.id = 'actions'
    shadowRoot.appendChild(this.actionsElement);

    this.deviceListHeader = document.createElement('div');
    this.deviceListHeader.id = 'devices-list-header'
    
    shadowRoot.appendChild(this.deviceListHeader);
    const headerName = document.createElement('div');
    const headerAccessKey = document.createElement('div');
    const headerCreated = document.createElement('div');
    headerName.innerHTML = 'Device Name'
    headerAccessKey.innerHTML = 'Access Key'
    headerCreated.innerHTML = 'Date Created'
    headerName.className = 'devices-list-header-title'
    headerAccessKey.className = 'devices-list-header-title'
    headerCreated.className = 'devices-list-header-title'
    this.deviceListHeader.appendChild(headerName);
    this.deviceListHeader.appendChild(headerAccessKey);
    this.deviceListHeader.appendChild(headerCreated);

    this.deviceList = document.createElement('ul');
    this.deviceList.id = 'devices-list'
    this.deviceList.appendChild(make_li());
    this.deviceList.appendChild(make_li());
    this.deviceList.appendChild(make_li());
    shadowRoot.appendChild(this.deviceList);
  }  
};
UIDevices.key = 'devices';
UIDevices.tagName = 'ui-devices';
window.customElements.define(tagName, UIDevices);
