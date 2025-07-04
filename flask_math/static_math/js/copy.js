function copy() {
    const element = document.querySelector('#targetID');
    const selection = window.getSelection();
    const range = document.createRange();

    range.selectNodeContents(element);
    selection.removeAllRanges();
    selection.addRange(range);
    const succeeded = document.execCommand('copy');

    if (succeeded) {
        alert('Copy successful!');
    } else {
        alert('Copy failed!');
    }
    selection.removeAllRanges();
}
