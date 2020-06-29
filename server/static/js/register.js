

let get_fields = () => {
    return { 
        username : document.getElementById('username'),
        password : document.getElementById('password'),
        confirm : document.getElementById('confirm'),
        hostkey : document.getElementById('hostkey'),
        error : document.getElementById('field-error'),
        errorvalue : document.getElementById('error-value')};};

let unhide_and_set = (fields, str) => {
    fields.errorvalue.innerHTML = str;
    fields.errorvalue.style.padding = '10px';
    fields.errorvalue.style.maxHeight = '400px';};

let validate = () => {
    fields = get_fields()
    empty = [];
    if (!fields.username.value) {
        empty.push('Username');
    }
    if (!fields.password.value) {
        empty.push('Password');
    }
    if (!fields.confirm.value) {
        empty.push('Confirm Password');
    }
    if (!fields.hostkey.value) {
        empty.push('Host Key');
    }
    if (empty.length > 0) {
        names = empty.join(', ');
        field = (empty.length > 1)? 'Fields': 'Field';
        unhide_and_set(fields, `${field} "${names}" cannot be empty.`);
        return false;
    }
    if (fields.password.value.localeCompare(fields.confirm.value) !== 0) {
        unhide_and_set(fields, `Password fields must match.`);
    }
    if (fields.password.value.length < 8) {
        unhide_and_set(fields, `Password must be at least 8 characters.`);
    }

    return true;
}

let post_register = () => {
    fields = get_fields()
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/accounts/', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (this.readyState != 4) return;

        if (this.status == 400) {
            let data = JSON.parse(this.responseText);
            unhide_and_set(fields, data.status);
        }
        else if (this.status == 409) {
            let data = JSON.parse(this.responseText);
            unhide_and_set(fields, data.status);
        }
        if (this.status == 201) {
            let data = JSON.parse(this.responseText);
            unhide_and_set(fields, data.status); // here maybe redirect?
        }
    };
    xhr.send(JSON.stringify({
        username : fields.username.value,
        password : fields.password.value
    }));
}

let validate_then_submit = () => {
    if (validate()) {
        post_register()
    }
 }
