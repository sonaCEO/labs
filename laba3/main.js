function toggleMenuVisibility() {
    console.log('its working'); 
    show = !show;
  if (show) {
    document.getElementById('hiddenContent').style.display = 'flex';
  } else {
    document.getElementById('hiddenContent').style.display = 'none';
  }
}

let show = false;

function secondToggleMenuVisibility() {
  showw = !showw;
  if (showw) {
    document.getElementById('secondHiddenContent').style.display = 'flex';
  } else {
    document.getElementById('secondHiddenContent').style.display = 'none';
  }
}

let showw = false;